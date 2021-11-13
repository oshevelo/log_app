from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from .models import Message, GroupChat
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

class ValidateUser(serializers.ModelSerializer):
    def validate_user(self, data, field_name):
        if not User.objects.filter(pk=data.get('id')).exists():
            raise serializers.ValidationError({field_name: f'User doesn\'t exist by {data.get("id")}'})
        return data


class UserNestedSerializer(serializers.ModelSerializer): # Todo: Will move to Profile
    id = serializers.IntegerField()
    email = serializers.CharField(read_only=True)
    username = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'username']


class MessageListSerializer(ValidateUser, serializers.ModelSerializer):
    sender = UserNestedSerializer()
    recipient = UserNestedSerializer()

    class Meta:
        model = Message
        fields = ('id', 'group_chat', 'sender', 'recipient', 'body', 'timestamp', 'is_read')

    def validate_recipient(self, data):
        return self.validate_user(data, 'recipient')

    def notify_ws_clients(self):
        notification = {
            'type': 'receive_group_message',
            'message': '{}'.format(self.id)
        }

        channel_layer = get_channel_layer()
        print("user.id {}".format(self.user.id))
        print("user.id {}".format(self.recipient.id))

        async_to_sync(channel_layer.group_send)("{}".format(self.user.id), notification)
        async_to_sync(channel_layer.group_send)("{}".format(self.recipient.id), notification)

    def create(self, validated_data):
        sender = self.context['request'].user
        recipient = get_object_or_404(User, id=validated_data['recipient']['id'])

        validated_data['sender'] = sender
        validated_data['recipient'] = recipient

        new = self.id
        if new is None:
            self.notify_ws_clients()

        return super().create(validated_data)


class GroupChatListSerializer(ValidateUser, serializers.ModelSerializer):
    owner = UserNestedSerializer()
    participants = UserNestedSerializer(many=True)

    class Meta:
        model = GroupChat
        fields = ('id', 'name', 'description', 'owner', 'participants',  'image')

    def validate_owner(self, data):
        return self.validate_user(data, 'owner')

    def validate_participants(self, data):
        print('LOL', data.get('participants') ) # ???
        if data.get('participants').len() < 2:
            raise serializers.ValidationError({f'Please add more than one'})
        return data

    def create(self, validated_data):
        owner_id = validated_data.get('owner', {}).get('id')
        owner = get_object_or_404(User, pk=owner_id)
        validated_data['owner'] = owner

        data = validated_data.copy()
        participants = data.pop('participants', [])
        instance = self.Meta.model.objects.create(**data)

        for participant in participants:
            participant = get_object_or_404(User, pk=participant['id'])
            instance.participants.add(participant)
        return instance


class GroupChatDetailsSerializer(ValidateUser, serializers.ModelSerializer):
    owner = UserNestedSerializer(read_only=True)
    participants = UserNestedSerializer(many=True)

    class Meta:
        model = GroupChat
        fields = ('id', 'name', 'description', 'owner', 'participants',  'image')

    def validate_owner(self, data):
        return self.validate_user(data, 'owner')

    def update(self, instance, validated_data):
        owner_id = validated_data.get('owner', {}).get('id')
        owner = get_object_or_404(User, pk=owner_id)
        validated_data['owner'] = owner

        data = validated_data.copy()
        participants = data.pop('participants', [])

        for participant in participants:
            participant_id = participant['id']
            participant = get_object_or_404(User, pk=participant_id)
            instance.participants.add(participant)

        return super().update(instance, validated_data)

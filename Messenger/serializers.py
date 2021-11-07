from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from .models import Message, GroupChat


class UserNestedSerializer(serializers.ModelSerializer): # Todo: Will move to Profile
    id = serializers.IntegerField()
    email = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name']


class MessageListSerializer(serializers.ModelSerializer):
    sender = UserNestedSerializer()
    recipient = UserNestedSerializer()

    class Meta:
        model = Message
        fields = ('id', 'group_chat', 'sender', 'recipient', 'body', 'timestamp', 'is_read')

    def create(self, validated_data):
        sender = get_object_or_404(User, id=validated_data['sender']['id'])
        recipient = get_object_or_404(User, id=validated_data['recipient']['id'])

        validated_data['sender'] = sender
        validated_data['recipient'] = recipient

        return super().create(validated_data)


class GroupChatListSerializer(serializers.ModelSerializer):
    owner = UserNestedSerializer()
    participants = UserNestedSerializer(many=True)

    class Meta:
        model = GroupChat
        fields = ('id', 'name', 'description', 'owner', 'participants',  'image')

    def create(self, validated_data):
        owner_id = validated_data.get('owner', {}).get('id')
        owner = get_object_or_404(User, pk=owner_id)
        validated_data['owner'] = owner

        data = validated_data.copy()
        participants = data.pop('participants', [])
        instance = self.Meta.model.objects.create(**data)

        for participant in participants:
            participant_id = participant['id']
            participant = get_object_or_404(User, pk=participant_id)
            instance.participants.add(participant)
        return instance


class GroupChatDetailsSerializer(serializers.ModelSerializer):
    owner = UserNestedSerializer(read_only=True)
    participants = UserNestedSerializer(many=True)

    class Meta:
        model = GroupChat
        fields = ('id', 'name', 'description', 'owner', 'participants',  'image')


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

class ValidateUser(serializers.ModelSerializer):

    def validate(self, data):
        if not User.objects.filter(pk=data.get('id')).exists():
            raise serializers.ValidationError({'User': f'User doesn\'t exist by {data.get("id")}'})
            # raise serializers.ValidationError({data.get('name_field'): f'Wrong {data.get("name_field")}'}) ???
        return data
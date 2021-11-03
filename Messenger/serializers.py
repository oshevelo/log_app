from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Message, GroupChat
from rest_framework import serializers


class UserNestedSerializer(serializers.ModelSerializer): # Todo: Will move to Profile
    id = serializers.IntegerField()
    email = serializers.CharField(read_only=True)
    first_name = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name']


class MessageListSerializer(serializers.ModelSerializer):
    sender = UserNestedSerializer(read_only=True)
    recipient = UserNestedSerializer(read_only=True)

    class Meta:
        model = Message
        fields = ('id', 'sender', 'recipient', 'body', 'timestamp', 'is_read')

    def create(self, validated_data):
        recipient = get_object_or_404(User, username=validated_data['recipient']['username'])
        group_chat = get_object_or_404(GroupChat, group_chat=validated_data['group_chat'])
        msg = Message(
            group_chat=group_chat,
            sender=sender,
            recipient=recipient,
            body=validated_data['body'],
            is_read=False
        )
        msg.save()
        return msg


class GroupChatListSerializer(serializers.ModelSerializer):
    owner = UserNestedSerializer()
    participants = UserNestedSerializer(many=True)

    class Meta:
        model = GroupChat
        fields = ('id', 'name', 'description', 'owner', 'participants',  'image')


    # def validate_owner(self, data):
    #     owner_id = data.get('id')
    #     if not User.objects.filter(pk=owner_id).exists():
    #         raise serializers.ValidationError({'owner_id': 'wrong id'})
    #     return data

    def create(self, validated_data):
        if 'owner' in validated_data:
            owner_id = validated_data.get('owner', {}).get('id')
            owner = get_object_or_404(User, pk=owner_id)
            validated_data['owner'] = owner

        if 'participants' in validated_data:
            for participant in validated_data.get('participants', {}):
                participant_id = participant['id']
                participant = get_object_or_404(User, pk=participant_id)
                print(participant)
                validated_data['participants'] = validated_data.get('participants', {})

        # image = self.context['request'].image #add Valid .png / size / pixel 100x100
        group_chat = GroupChat(
            name=validated_data['name'],
            description=validated_data['description'],
            owner=owner,
            participants=validated_data.get('participants'),
            image=validated_data.get('image'),
        )
        group_chat.save()
        return group_chat

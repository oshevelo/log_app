from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Message, GroupChat
from rest_framework.serializers import ModelSerializer, CharField


class UserNestedSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class MessageListSerializer(ModelSerializer):
    user = UserNestedSerializer()
    recipient = UserNestedSerializer()

    def create(self, validated_data):
        sender = self.context['request'].user
        recipient = get_object_or_404(User, username=validated_data['recipient']['username'])
        msg = Message(recipient=recipient, body=validated_data['body'], user=sender, is_received=False, is_read=False)
        msg.save()
        return msg

    class Meta:
        model = Message
        fields = ('id', 'sender', 'recipient', 'body', 'timestamp', 'is_received', 'is_read')


class GroupChatListSerializer(ModelSerializer):

    class Meta:
        model = GroupChat
        fields = ('id', 'owner', 'participants', 'name',  'description', 'image')



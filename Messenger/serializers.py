from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Message
from rest_framework.serializers import ModelSerializer, CharField


class UserNestedSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class RecipientNestedSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class MessageListSerializer(ModelSerializer):
    user = UserNestedSerializer()
    recipient = RecipientNestedSerializer()

    def create(self, validated_data):
        user = self.context['request'].user
        recipient = get_object_or_404(User, username=validated_data['recipient']['username'])
        msg = Message(recipient=recipient, body=validated_data['body'], user=user, is_received=False, is_read=False)
        msg.save()
        return msg

    class Meta:
        model = Message
        fields = ('id', 'user', 'recipient', 'body', 'timestamp', 'is_received', 'is_read')


class MessageDetailsSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'user', 'recipient', 'body', 'timestamp', 'is_received', 'is_read')


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class UserDetailsSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'date_joined')

from rest_framework import serializers
from .models import Room, Message


class RoomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'pub_date', 'room_text', 'was_published_recently']


class RoomDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'pub_date', 'room_text']


class MessageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'room']


class MessageDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'room', 'message_text', 'votes']

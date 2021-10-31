from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import generics, pagination

from .serializers import MessageListSerializer, GroupChatListSerializer, UserNestedSerializer
from .models import Message, GroupChat


class MessageList(generics.ListCreateAPIView):
    pagination_class = pagination.LimitOffsetPagination
    queryset = Message.objects.all()
    serializer_class = MessageListSerializer


class GroupChatList(generics.ListCreateAPIView):
    pagination_class = pagination.LimitOffsetPagination
    queryset = GroupChat.objects.all()
    serializer_class = GroupChatListSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserNestedSerializer
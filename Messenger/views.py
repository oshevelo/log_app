from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import generics, pagination

from .serializers import MessageListSerializer, GroupChatListSerializer, UserNestedSerializer, \
    GroupChatDetailsSerializer
from .models import Message, GroupChat


class MessageList(generics.ListCreateAPIView):
    pagination_class = pagination.LimitOffsetPagination
    queryset = Message.objects.all()
    serializer_class = MessageListSerializer


class GroupChatList(generics.ListCreateAPIView):
    pagination_class = pagination.LimitOffsetPagination
    queryset = GroupChat.objects.all()
    serializer_class = GroupChatListSerializer


class GroupChatDetails(generics.ListCreateAPIView):
    serializer_class = GroupChatDetailsSerializer

    def get_queryset(self):
        return GroupChat.objects.filter(pk=self.kwargs.get('group_chat_id'))

    def get_object(self):
        return get_object_or_404(GroupChat, pk=self.kwargs.get('group_chat_id'))


class UserList(generics.ListCreateAPIView): # Todo: Will move to Profile
    pagination_class = pagination.LimitOffsetPagination
    queryset = User.objects.all()
    serializer_class = UserNestedSerializer

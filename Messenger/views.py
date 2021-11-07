from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import generics, pagination

from .serializers import MessageListSerializer, GroupChatListSerializer, UserNestedSerializer, \
    GroupChatDetailsSerializer
from .models import Message, GroupChat


class MessageList(generics.ListCreateAPIView):
    pagination_class = pagination.LimitOffsetPagination
    serializer_class = MessageListSerializer

    def get_queryset(self):
        group_chat_id = self.request.query_params.get('group_chat_id')
        if group_chat_id:
            group_chat = get_object_or_404(GroupChat, pk=group_chat_id)
            return Message.objects.filter(group_chat=group_chat)
        # TODO: Create Group Chat


class GroupChatList(generics.ListCreateAPIView):
    pagination_class = pagination.LimitOffsetPagination
    queryset = GroupChat.objects.all()
    serializer_class = GroupChatListSerializer

    def get_queryset(self):
        user = self.request.user
        return GroupChat.objects.filter(owner=user)


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

from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import generics, pagination
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from .filters import FilterMessage

from .serializers import MessageListSerializer, GroupChatListSerializer, UserNestedSerializer, \
    GroupChatDetailsSerializer
from .models import Message, GroupChat


class MessageList(generics.ListCreateAPIView):
    pagination_class = pagination.LimitOffsetPagination
    serializer_class = MessageListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = FilterMessage

    def get_queryset(self):
        group_chat_id = self.request.query_params.get('group_chat_id')

        if group_chat_id:
            group_chat = get_object_or_404(GroupChat, pk=group_chat_id)
            return Message.objects.filter(group_chat=group_chat)


class GroupChatList(generics.ListCreateAPIView):
    pagination_class = pagination.LimitOffsetPagination
    queryset = GroupChat.objects.all()
    serializer_class = GroupChatListSerializer

    def get_queryset(self):
        user = self.request.user
        return GroupChat.objects.filter(participants=user)


class GroupChatDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GroupChatDetailsSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return get_object_or_404(GroupChat, pk=self.kwargs.get('group_chat_id'))

    def put(self, request, *args, **kwargs):
        if request.user.id == request.data['owner']['id']:
            return self.update(request, *args, **kwargs)
        return Response({'error': 'This user can\'t edit this group'}, status=404)


class UserList(generics.ListCreateAPIView): # Todo: Will move to Profile
    pagination_class = pagination.LimitOffsetPagination
    queryset = User.objects.all()
    serializer_class = UserNestedSerializer

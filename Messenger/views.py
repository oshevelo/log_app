from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import generics, pagination

from LogApp import settings
from .serializers import MessageListSerializer, UserModelSerializer, MessageDetailsSerializer, UserDetailsSerializer
from .models import Message


class MessageList(generics.ListCreateAPIView):
    pagination_class = pagination.LimitOffsetPagination
    queryset = Message.objects.all()
    serializer_class = MessageListSerializer


class MessageDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MessageDetailsSerializer

    def get_object(self):
        return get_object_or_404(Message, pk=self.kwargs.get('message_id'))


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer


class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailsSerializer

    def get_object(self):
        return get_object_or_404(User, pk=self.kwargs.get('user_id'))
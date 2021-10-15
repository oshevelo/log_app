from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import SessionAuthentication

from LogApp import settings
from .serializers import MessageListSerializer, UserModelSerializer, MessageDetailsSerializer, UserDetailsSerializer
from .models import Message


from rest_framework import generics


class CsrfExemptSessionAuthentication(SessionAuthentication):
    """
    SessionAuthentication scheme used by DRF. DRF's SessionAuthentication uses
    Django's session framework for authentication which requires CSRF to be
    checked. In this case we are going to disable CSRF tokens for the API.
    """

    def enforce_csrf(self, request):
        return


class MessagePagination(PageNumberPagination):
    page_size = settings.MESSAGES_TO_LOAD


class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageListSerializer
    # allowed_methods = ('GET', 'POST', 'HEAD', 'OPTIONS')
    # authentication_classes = (CsrfExemptSessionAuthentication,)
    # pagination_class = MessagePagination
    #
    # def list(self, request, *args, **kwargs):
    #     self.queryset = self.queryset.filter(Q(recipient=request.user) |
    #                                          Q(user=request.user))
    #     target = self.request.query_params.get('target', None)
    #     if target is not None:
    #         self.queryset = self.queryset.filter(
    #             Q(recipient=request.user, user__username=target) |
    #             Q(recipient__username=target, user=request.user))
    #     return super(Message, self).list(request, *args, **kwargs)
    #
    # def retrieve(self, request, *args, **kwargs):
    #     msg = get_object_or_404(
    #         self.queryset.filter(Q(recipient=request.user) |
    #                              Q(user=request.user),
    #                              Q(pk=kwargs['pk'])))
    #     serializer = self.get_serializer(msg)
    #     return Response(serializer.data)


class MessageDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MessageDetailsSerializer

    def get_object(self):
        return get_object_or_404(Message, pk=self.kwargs.get('message_id'))


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    # allowed_methods = ('GET', 'HEAD', 'OPTIONS')
    # pagination_class = None  # Get all user
    #
    # def list(self, request, *args, **kwargs):
    #     # Get all users except yourself
    #     self.queryset = self.queryset.exclude(id=request.user.id)
    #     return super(UserList, self).list(request, *args, **kwargs)


class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailsSerializer

    def get_object(self):
        return get_object_or_404(User, pk=self.kwargs.get('user_id'))
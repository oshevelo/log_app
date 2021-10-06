from django.http import HttpResponse
from .models import Room, Message
from .serializers import RoomListSerializer, RoomDetailsSerializer, MessageListSerializer,\
    MessageDetailsSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics


class RoomList(generics.ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomListSerializer


class RoomDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RoomDetailsSerializer

    def get_object(self):
        return get_object_or_404(Room, pk=self.kwargs.get('room_id'))


class MessageList(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageListSerializer


class MessageDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MessageDetailsSerializer

    def get_object(self):
        return get_object_or_404(Message, pk=self.kwargs.get('message_id'))


def index(request):
    latest_room_list = Room.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.room_text for q in latest_room_list])
    return HttpResponse(output)


def detail(request, room_id):
    return HttpResponse("You're looking at room %s." % room_id)


def results(request, room_id):
    response = "You're looking at the results of room %s."
    return HttpResponse(response % room_id)


def vote(request, room_id):
    return HttpResponse("You're voting on room %s." % room_id)

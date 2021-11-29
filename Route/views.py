
# from django.shortcuts import render

from rest_framework import pagination
from rest_framework import generics

from .models import Route
from .serializers import RouteListSerializer, RouteDetailsSerializer


class RouteList(generics.ListCreateAPIView):
    queryset = Route.objects.all()
    pagination_class = pagination.LimitOffsetPagination
    serializer_class = RouteListSerializer


class RouteDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RouteDetailsSerializer

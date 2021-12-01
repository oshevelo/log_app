
# from django.shortcuts import render

from rest_framework import pagination
from rest_framework import generics
from rest_framework.generics import get_object_or_404

from .models import Route
from .serializers import RouteListSerializer, RouteDetailsSerializer


class RouteList(generics.ListCreateAPIView):
    queryset = Route.objects.all()
    pagination_class = pagination.LimitOffsetPagination
    serializer_class = RouteListSerializer

    def get_queryset(self):
        if not self.request.user.is_superuser:
            return Route.objects.filter(respondent=self.request.user)
        return Route.objects.all()


class RouteDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RouteDetailsSerializer

    def get_object(self):
        if not self.request.user.is_superuser:
            get_object_or_404(Route, pk=self.kwargs.get('route_id'), respondent=self.request.user)
        return get_object_or_404(Route, pk=self.kwargs.get('route_id'))
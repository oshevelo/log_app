from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Route


class RouteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['name_route', 'start_point_lat', 'start_point_long', 'end_point_lat', 'end_point_long']


class RouteDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['name_route', 'journey_dist', 'journey_time', 'journey_rating']




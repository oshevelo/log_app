from rest_framework import serializers
from .models import PricePlan
from django.contrib.auth.models import User

class UserNestedPays(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "first_name"]


class BasicPlanListSerializer(serializers.ModelSerializer):
    payer = UserNestedPays(read_only=True)
    class Meta:
        model = PricePlan
        fields = ["pk", 'payment_time', 'payer', "plan_type"]


class BasicDetailSerializer(serializers.ModelSerializer):
    payer = UserNestedPays(read_only=True)
    class Meta:
        model = PricePlan
        fields = "__all__"
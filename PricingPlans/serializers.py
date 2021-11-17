from rest_framework import serializers
from .models import BasicPlan, ProPlan, VipPlan
from django.contrib.auth.models import User

class UserNestedPays(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "first_name"]


class BasicPlanListSerializer(serializers.ModelSerializer):
    payer = UserNestedPays(read_only=True)
    class Meta:
        model = BasicPlan
        fields = ["pk", 'payment_time', 'payer', "plan_cost"]


class ProPlanListSerializer(serializers.ModelSerializer):
    payer = UserNestedPays(read_only=True)
    class Meta:
        model = ProPlan
        fields = ["pk", 'payment_time', 'payer', "plan_cost"]

class VipPlanListSerializer(serializers.ModelSerializer):
    payer = UserNestedPays(read_only=True)
    class Meta:
        model = VipPlan
        fields = ["pk", 'payment_time', 'payer', "plan_cost"]


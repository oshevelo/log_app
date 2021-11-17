from rest_framework import serializers
from .models import PayCheck
from django.contrib.auth.models import User

class UserNestedPays(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "first_name"]


class PaysListSerializer(serializers.ModelSerializer):
    payer = UserNestedPays(read_only=True)
    class Meta:
        model = PayCheck
        fields = ["pk", 'pay_time', 'payer', "sum", "email"]


class PaysDetailsSerializer(serializers.ModelSerializer):
    payer = UserNestedPays(read_only=True)
    class Meta:
        model = PayCheck
        fields = ["pk", 'pay_time', 'payer', "sum", "email"]






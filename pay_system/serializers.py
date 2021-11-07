from rest_framework import serializers
from .models import pay_check


class PaysListSerializer(serializers.ModelSerializer):
    class Meta:
        model = pay_check
        fields = ["pk", 'pay_time', 'payer', "sum", "email"]


class PaysDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = pay_check
        fields = ["pk", 'pay_time', 'payer', "sum", "email"]
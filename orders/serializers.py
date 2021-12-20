from django.utils import timezone
from rest_framework import serializers
from rest_framework.serializers import ValidationError, UniqueTogetherValidator

from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:

        model = OrderItem
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=model.objects.all(), fields=['order', 'product']
            )
        ]


class OrderItemNestedSerializer(serializers.ModelSerializer):

    class Meta:

        model = OrderItem
        fields = ['product', 'amount']


class OrderListSerializer(serializers.ModelSerializer):

    receiver = serializers.PrimaryKeyRelatedField(
        queryset=Order.objects.all(), default = serializers.CurrentUserDefault()
    )

    class Meta:

        model = Order
        fields = '__all__'

    def validate_sender(self, sender):
        """ Check sender and receiver are not the same person """
        if sender == self.initial_data.get('receiver'):
            raise ValidationError('can not perform this action')
        return sender

    def validate_courier(self, courier):
        """ Check courier is staff """
        if not courier.is_staff:
            raise ValidationError('courier must be staff')
        return courier


class OrderDetailSerializer(serializers.ModelSerializer):

    items = OrderItemNestedSerializer(read_only=True, many=True)

    class Meta:

        model = Order
        fields = '__all__'

    def update(self, instance, validated_data):
        """ Set delivery finish time """
        if validated_data.get('status') == Order.Status.done:
            instance.delivered_on = timezone.now()
            instance.save()
        return super().update(instance, validated_data)

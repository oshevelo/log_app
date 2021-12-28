from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import serializers
from rest_framework.serializers import ValidationError

from .models import Order, OrderItem


class OrderFromURL:

    requires_context = True

    def __call__(self, order_field):
        order_id = order_field.context.get('request').parser_context.get(
            'kwargs').get('order_id')
        order = get_object_or_404(Order, pk=order_id)
        return order


class OrderItemSerializer(serializers.ModelSerializer):

    order = serializers.PrimaryKeyRelatedField(
        queryset=OrderItem.objects.all(), default = OrderFromURL()
    )

    class Meta:

        model = OrderItem
        fields = '__all__'

    def validate(self, data):
        """ Check products in order are not duplicating """
        if OrderItem.objects.filter(
            order=data.get('order'), product=data.get('product')
        ).exists():
            raise ValidationError('duplicating products in order')
        return data


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

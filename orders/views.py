from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend

from .models import Order, OrderItem
from .permissions import IsOrderReceiverOrSuperuser
from .serializers import OrderListSerializer, OrderDetailSerializer, \
    OrderItemSerializer


class OrderList(generics.ListCreateAPIView):

    serializer_class = OrderListSerializer
    pagination_class = LimitOffsetPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status']

    def get_queryset(self):
        user = self.request.user
        if not user.is_superuser:
            return Order.objects.filter(receiver=user)
        return Order.objects.all()


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = OrderDetailSerializer
    permission_classes = [IsOrderReceiverOrSuperuser]

    def get_object(self):
        return get_object_or_404(Order, pk=self.kwargs.get('order_id'))


class OrderItemCreate(generics.CreateAPIView):

    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsOrderReceiverOrSuperuser]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'order': self.kwargs.get('order_id')})
        return context

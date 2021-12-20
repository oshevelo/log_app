from django.shortcuts import get_object_or_404
from rest_framework.permissions import BasePermission

from .models import Order


class IsOrderReceiver(BasePermission):

    def has_permission(self, request, view):
        obj = get_object_or_404(Order, pk=view.kwargs.get('order_id'))
        return request.user == obj.receiver


class IsSuperuser(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser

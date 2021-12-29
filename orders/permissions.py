from django.shortcuts import get_object_or_404
from rest_framework.permissions import BasePermission

from .models import Order


class IsOrderReceiverOrSuperuser(BasePermission):

    def has_permission(self, request, view):
        obj = get_object_or_404(Order, pk=view.kwargs.get('order_id'))
        return request.user == obj.receiver or request.user.is_superuser

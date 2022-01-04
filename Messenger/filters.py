import django_filters
from django_filters.rest_framework import FilterSet

from Messenger.models import Message


class FilterMessage(FilterSet):

    body = django_filters.filters.CharFilter(field_name="body", lookup_expr='icontains')

    class Meta:
        model = Message
        fields = ['body']

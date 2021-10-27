import django_filters
from django_filters.rest_framework import FilterSet

from demo.models import Question


class FilterQuestion(FilterSet):

    def filter_questions(self, qs, name, value):
        #1/0
        return qs.filter(question_text=value)

    type = django_filters.filterset.CharFilter(method='filter_questions')
    question_text = django_filters.filters.CharFilter(field_name="question_text", lookup_expr='icontains')
    class Meta:
        model = Question
        fields = ['question_text', 'type']

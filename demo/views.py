from django.http import HttpResponse
from .models import Question
from django_filters import rest_framework as filters
from .serializers import QuestionListSerializer, QuestionDetailsSerializer
from .filters import FilterQuestion
from django.shortcuts import get_object_or_404
from rest_framework import generics, pagination


class QuestionList(generics.ListCreateAPIView):
    pagination_class = pagination.LimitOffsetPagination
    serializer_class = QuestionListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = FilterQuestion
    
    def get_queryset(self):
        if not self.request.user.is_superuser:
            return Question.objects.filter(respondent=self.request.user)
        return Question.objects.all()
    
    
class QuestionDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionDetailsSerializer
    
    def get_object(self):
        if not self.request.user.is_superuser:
            return get_object_or_404(Question, pk=self.kwargs.get('question_id'), respondent=self.request.user)
        return get_object_or_404(Question, pk=self.kwargs.get('question_id'))
        

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
        print(self.request.query_params)
        #question_text = self.request.query_params.get('question_text')
        #if question_text:
        #    return Question.objects.filter(question_text=question_text)    
        return Question.objects.all()
    
    
class QuestionDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionDetailsSerializer
    
    def get_object(self):
        return get_object_or_404(Question, pk=self.kwargs.get('question_id'))

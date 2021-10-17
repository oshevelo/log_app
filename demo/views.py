from django.http import HttpResponse
from .models import Question
from .serializers import QuestionListSerializer, QuestionDetailsSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer
    
    
class QuestionDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = QuestionDetailsSerializer
    
    def get_object(self):
        return get_object_or_404(Question, pk=self.kwargs.get('question_id'))

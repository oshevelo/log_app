from django.http import HttpResponse
from .models import pay_check
from .serializers import PaysListSerializer, PaysDetailsSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView

class PaysList(generics.ListCreateAPIView):
    queryset = pay_check.objects.all()
    serializer_class = PaysListSerializer

class PaysDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PaysDetailsSerializer

    def get_object(self):
        return get_object_or_404(pay_check, pk=self.kwargs.get('pk'))



from django.http import HttpResponse
from .models import PayCheck
from .serializers import PaysListSerializer, PaysDetailsSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView

class PaysList(generics.ListCreateAPIView):
    queryset = PayCheck.objects.all()
    serializer_class = PaysListSerializer

class PayDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PaysDetailsSerializer

    def get_object(self):
        return get_object_or_404(PayCheck, pk=self.kwargs.get('pk'))
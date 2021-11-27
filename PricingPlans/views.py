from django.http import HttpResponse
from .models import BasicPlan, ProPlan, VipPlan
from .serializers import BasicPlanListSerializer, ProPlanListSerializer, VipPlanListSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from paypal.standard.forms import PayPalPaymentsForm

class BasicPlanList(generics.ListCreateAPIView):
    queryset = BasicPlan.objects.all()
    serializer_class = BasicPlanListSerializer


class ProPlanList(generics.ListCreateAPIView):
    queryset = ProPlan.objects.all()
    serializer_class = ProPlanListSerializer

class VipPlanList(generics.ListCreateAPIView):
    queryset = VipPlan.objects.all()
    serializer_class = VipPlanListSerializer




# class PayDetails(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = BasicDetailsSerializer
#
#     def get_object(self):
#         return get_object_or_404(BasicPlan, pk=self.kwargs.get('pk'))

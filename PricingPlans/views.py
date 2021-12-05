from decimal import Decimal

from django.http import HttpResponse
from django.template import loader
from django.template.loader import get_template

from .models import PricePlan
from .serializers import BasicPlanListSerializer, BasicDetailSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from django.views.generic import FormView
from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm
from paypal.pro.views import PayPalPro
from django.conf import settings

class PricePlanList(generics.ListCreateAPIView):
    queryset = PricePlan.objects.all()
    serializer_class = BasicPlanListSerializer
    def get_queryset(self):
        if not self.request.user.is_superuser:
            return PricePlan.objects.filter(payer=self.request.user)
        return PricePlan.objects.all()

class PayDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BasicDetailSerializer

    def get_object(self):
        return get_object_or_404(PricePlan, pk=self.kwargs.get('pay_id'))



def BasePlan(request):
    return render(request, "PricingPlans/BasePlan.html")

def ProPlan(request):
    return render(request, "PricingPlans/ProPlan.html")

def VipPlan(request):
    return render(request, "PricingPlans/VipPlan.html")
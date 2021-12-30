from decimal import Decimal
import requests
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.template.loader import get_template
from django.views import View
from requests import post
from .forms import PricePlanUserForm
from .models import PricePlan
from .serializers import BasicPlanListSerializer, BasicDetailSerializer
from django.shortcuts import get_object_or_404, redirect
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
        return get_object_or_404(PricePlan.objects.filter(payer=self.request.user), pk=self.kwargs.get('pay_id'))

def choicen_plan(request):#тут проходит оплата
    return render(request, "PricingPlans/BasicPageForAllPlans.html")

def testy(request):
    if request.method == 'POST':
        form = PricePlanUserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('Pay/')
    form = PricePlanUserForm()
    return render(request,'PricingPlans/confirmation.html', context={'form': form})
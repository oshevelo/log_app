from decimal import Decimal

from django.http import HttpResponse
from django.template import loader
from django.template.loader import get_template

from .models import PricePlan
from .serializers import BasicPlanListSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from django.views.generic import FormView
from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm

from django.conf import settings

class PricePlanList(generics.ListCreateAPIView):
    queryset = PricePlan.objects.all()
    serializer_class = BasicPlanListSerializer


#def paypal(requests):

    #return render(requests, "PricingPlans/paypal_form.html", { "title" : "Pays", "form" : "PayPalPaymentsForm" })

def process_payment(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(PricePlanList, id=order_id)
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '%.2f' % order.plan_type.quantize(
            Decimal('.01')),
        'item_name': 'Order {}'.format(order.id),
        'invoice': str(order.id),
        'currency_code': 'USD',
        #'notify_url': 'http://{}{}'.format(host,
                                           #reverse('paypal-ipn')),
        #'return_url': 'http://{}{}'.format(host,
                                          # reverse('payment_done')),
        #'cancel_return': 'http://{}{}'.format(host,
                                              #reverse('payment_cancelled')),
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'paypal_form.html', {'order': order, 'form': form})

# class PayDetails(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = BasicDetailsSerializer
#
#     def get_object(self):
#         return get_object_or_404(BasicPlan, pk=self.kwargs.get('pk'))

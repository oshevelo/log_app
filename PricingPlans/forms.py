from django.forms import ModelForm
from .models import PricePlan

class PricePlanUserForm(ModelForm):
    class Meta:
        model = PricePlan
        fields = ['payment_time', 'payer', 'plan_type']

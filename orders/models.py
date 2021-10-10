from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):

    STATUS_CHOICES = [
        ('inactive', 'inactive order'),
        ('active', 'order in progress'),
        ('complete', 'order delivered')
    ]

    PAYMENT_CHOICES = [
        ('cash', 'cash payment'),
        ('cashless', 'cashless payment')
    ]
    # General info.
    status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=STATUS_CHOICES.inactive
    )
    products = models.ManyToManyField('products.Product')
    description = models.CharField(max_length=500, blank=True)
    # Participants info.
    sender = models.ForeignKey(User, on_delete=models.SET_NULL)
    courier = models.ForeignKey(User, on_delete=models.SET_NULL)
    receiver = models.ForeignKey(User, on_delete=models.SET_NULL)
    vehicle = models.ForeignKey('vehicles.Vehicle', on_delete=models.SET_NULL)
    # Delivery time info.
    added = models.DateTimeField(auto_now_add=True)
    delivery_time = models.DurationField()
    delivered = models.DateTimeField()
    # Route info.
    start_point = models.ForeignKey('points.Point', on_delete=models.SET_NULL)
    finish_point = models.ForeignKey('points.Point', on_delete=models.SET_NULL)
    # Payment info.
    total_cost = models.DecimalField(max_digits=20, decimal_places=2)
    payment_type = models.CharField(max_length=50, choices=PAYMENT_CHOICES)

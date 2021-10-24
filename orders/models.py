from django.db import models
from django.contrib.auth.models import User


class Order(models.Model):

    class Status:

        active = 'active'
        done = 'done'
        canceled = 'canceled'

    STATUS_CHOICES = [
        (Status.active, 'order in progress'),
        (Status.done, 'order delivered'),
        (Status.canceled, 'order canceled')
    ]
    # General info.
    status = models.CharField(
        choices=STATUS_CHOICES, default=Status.active, max_length=50
    )
    description = models.TextField(max_length=2500, blank=True)
    # Participants info.
    sender = models.ForeignKey(User, null=True, on_delete=models.SET_NULL,
        related_name='sender'
    )
    courier = models.ForeignKey(User, null=True, on_delete=models.SET_NULL,
        related_name='courier'
    )
    receiver = models.ForeignKey(User, null=True, on_delete=models.SET_NULL,
        related_name='receiver'
    )
    # vehicle = models.ForeignKey(
    #     'vehicles.Vehicle', null=True, on_delete=models.SET_NULL
    # )
    # Delivery time info.
    created_on = models.DateTimeField(auto_now_add=True)
    delivered_on = models.DateTimeField()
    # Route info.
    # start_point = models.ForeignKey(
    #     'points.Point', null=True, on_delete=models.SET_NULL
    # )
    # finish_point = models.ForeignKey(
    #     'points.Point', null=True, on_delete=models.SET_NULL
    # )
    # Payment info.
    # payment_info = models.ForeignKey(
    #     'payment.Payment', null=True, on_delete=models.SET_NULL
    # )


class OrderItem(models.Model):
    # Delivered items info.
    # order = models.ForeignKey(Order, on_delete=models.CASCADE)
    # product = models.ForeignKey(
    #     'products.Product', null=True, on_delete=models.SET_NULL
    # )
    amount = models.PositiveSmallIntegerField(default=1)

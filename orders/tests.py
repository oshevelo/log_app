from django.test import TestCase
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APIClient

from orders.models import Order, OrderItem
from Vehicles.models import Vehicle
from Route.models import Route
from PricingPlans.models import PricePlan
from Products.models import Product

from utils.helpers_for_tests import create_user, login_user, dump


class TestOrders(TestCase):

    def setUp(self):
        self.client = APIClient()

        self.receiver = create_user('test_receiver')
        self.sender = create_user('test_sender')
        self.courier = create_user(
            'test_courier', user_kwargs_dict={'is_staff': True}
        )
        self.vehicle = Vehicle.objects.create(id=1)
        self.product = Product.objects.create(id=1)
        self.payment = PricePlan.objects.create(
            plan_type=PricePlan.PricePlanTypes.base,
            payer=self.receiver
        )
        self.route = Route.objects.create(
            name='test_route',
            start_point_x=0.111,
            start_point_y=0.222,
            end_point_x=0.333,
            end_point_y=0.444,
            distance=4,
            date_time=timezone.now(),
            rating=5
        )
        self.order = Order.objects.create(
            description='test description',
            receiver=self.receiver,
            sender=self.sender,
            courier=self.courier,
            vehicle=self.vehicle,
            route=self.route,
            payment=self.payment
        )

    def test_unauth_get_list(self):
        response = APIClient().get('/orders/list/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unauth_get_detail(self):
        response = APIClient().get(f'/orders/{self.order.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_unauth_create_items(self):
        response = APIClient().post(
            f'/orders/{self.order.id}/items/', 
            data={'product': '1', 'amount': '2'}, 
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_empty_list(self):
        login_user(self.client, self.sender)
        response = self.client.get('/orders/list/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [])

    def test_get_list(self):
        login_user(self.client, self.receiver)
        response = self.client.get('/orders/list/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [
            {
                'id': self.order.id,
                'receiver': self.receiver.id,
                'status': "active",
                'description': "test description",
                'created_on': response.data[0]['created_on'],
                'delivered_on': None,
                'sender': self.sender.id,
                'courier': self.courier.id,
                'vehicle': self.vehicle.id,
                'route': self.route.id,
                'payment': self.payment.id
            }
        ]
    )

    def test_get_detail(self):
        login_user(self.client, self.receiver)
        response = self.client.get(f'/orders/{self.order.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            'id': self.order.id,
            'items': [],
            'status': "active",
            'description': "test description",
            'created_on': response.data['created_on'],
            'delivered_on': None,
            'sender': self.sender.id,
            'courier': self.courier.id,
            'receiver': self.receiver.id,
            'vehicle': self.vehicle.id,
            'route': self.route.id,
            'payment': self.payment.id
        }
    )

    def test_create_order(self):
        login_user(self.client, self.receiver)
        response = self.client.post(
            '/orders/list/',
            data={
                'description': "test description 2",
                'created_on': timezone.now(),
                'sender': self.sender.id,
                'courier': self.courier.id,
                'vehicle': self.vehicle.id,
                'route': self.route.id,
                'payment': self.payment.id
            }
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_items(self):
        login_user(self.client, self.receiver)
        response = self.client.post(
            f'/orders/{self.order.id}/items/',
            data={
                'product': self.product.id, 'amount': 5
            }, 
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {
                'id': 1,
                'order': self.order.id,
                'amount': 5,
                'product': self.product.id

            }
        )

from django.conf import settings
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from datetime import datetime
from utils.helpers_for_tests import create_user, dump, login_user
from demo.models import Question
#from products.models import Manufacturer, Product


class ProductsAPITest(TestCase):
    
    def setUp(self):
        self.c = APIClient()
        
        self.admin = create_user('admin@staff')
        self.question = Question.objects.create(
            question_text='test', 
            pub_date=datetime.now(),
            description='asd',
            respondent=self.admin
        )
        pass
        
    def test_empty_get(self):
        self.assertEqual(1, 1)
        
    def test_unauth_restriction(self):
        response = self.c.get('/demo/')
        #print(dir(status))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
    def test_auth_list(self):
        login_user(self.c, self.admin)
        response = self.c.get('/demo/')
        #print(dir(status))
        #dump(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [
            {
                'id': self.question.id,
                'pub_date': response.data[0]['pub_date'],
                'question_text': "test",
                'author': None
            }
        ])

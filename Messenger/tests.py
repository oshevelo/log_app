from django.conf import settings
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from utils.helpers_for_tests import create_user, dump, login_user
from Messenger.models import GroupChat

class GroupChatTest(TestCase):

    def setUp(self):
        self.c = APIClient()

        self.adminMax = create_user('admin@max')
        self.adminKoly = create_user('admin@koly')
        self.groupChat = GroupChat.objects.create(
            name='test group chat',
            description='description test',
            owner=self.adminMax,
            participants=[self.adminMax, self.adminKoly],
            image=None
        )

    def test_empty_get(self):
        self.assertEqual(1, 1)

    def test_unauth_restriction(self):
        response = self.c.get('/messenger/')
        # print(dir(status))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_auth_list(self):
        login_user(self.c, self.adminMax)
        response = self.c.get('/group-chat/')
        # print(dir(status))
        # dump(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [
            {
                'id': self.groupChat.id,
                'name': 'test group chat',
                'description': "description test",
                'owner': self.adminMax,
                'participants': [self.adminMax, self.adminKoly],
                'image': None
            }
        ])

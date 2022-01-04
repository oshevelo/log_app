from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from utils.helpers_for_tests import create_user, dump, login_user
from Messenger.models import GroupChat, Message
from datetime import datetime

class GroupChatTest(TestCase):

    def setUp(self):
        self.c = APIClient()
        self.adminMax = create_user('admin@max')
        self.adminKoly = create_user('admin@koly')
        self.groupChat = GroupChat.objects.create(
            name='test group chat',
            description='description test',
            owner=self.adminMax,
            image=None
        )
        self.groupChat.participants.set([self.adminMax, self.adminKoly])

    def test_empty_get(self):
        self.assertEqual(1, 1)

    def test_unauth_restriction(self):
        response = self.c.get('/messenger/group-chat/')
        print(dir(status))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_group_chat_list(self):
        login_user(self.c, self.adminMax)
        response = self.c.get('/messenger/group-chat/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['owner']['id'], self.adminMax.id)
        self.assertEqual(response.data[0]['participants'][0]['id'], self.adminKoly.id)
        self.assertEqual(response.data[0]['participants'][1]['id'], self.adminMax.id)
        self.assertEqual(response.data, [
            {
                'id': self.groupChat.id,
                'name': 'test group chat',
                'description': "description test",
                'owner': response.data[0]['owner'],
                'participants': response.data[0]['participants'],
                'image': None
            }
        ])


class MessageTest(TestCase):

    def setUp(self):
        self.c = APIClient()
        self.adminMax = create_user('admin@max')
        self.adminKoly = create_user('admin@koly')
        self.groupChat = GroupChat.objects.create(
            name='test group chat',
            description='description test',
            owner=self.adminMax,
            image=None
        )
        self.groupChat.participants.set([self.adminMax, self.adminKoly])
        self.message = Message.objects.create(
            group_chat=self.groupChat,
            sender=self.adminMax,
            recipient=self.adminKoly,
            timestamp=datetime.now(),
            body='Hello friend',
            is_read=False
        )

    def test_message_list(self):
        login_user(self.c, self.adminMax)
        response = self.c.get(f'/messenger/message/?group_chat_id={self.message.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['sender']['id'], self.adminMax.id)
        self.assertEqual(response.data[0]['recipient']['id'], self.adminKoly.id)

        self.assertEqual(response.data, [
            {
                'id': self.message.id,
                'group_chat': self.groupChat.id,
                'sender': response.data[0]['sender'],
                'recipient': response.data[0]['recipient'],
                'timestamp': response.data[0]['timestamp'],
                'body': 'Hello friend',
                'is_read': False
            }
        ])

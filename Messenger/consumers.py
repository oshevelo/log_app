from datetime import datetime
from channels.generic.websocket import WebsocketConsumer
import json
from urllib.parse import urlparse, parse_qs
from .models import Message, GroupChat
from django.shortcuts import get_object_or_404
from asgiref.sync import async_to_sync
from django.contrib.auth.models import User


class ChatConsumer(WebsocketConsumer):

    def connect(self):
        # Join room group
        # self.group_id = self.scope['url_route']['kwargs']['chat_group_id']   Q: lol? chat_group_id = name url
        parsed_url = urlparse(f'www.lol.com?${self.scope["query_string"]}')
        self.group_id = parse_qs(parsed_url.query)['chat_group_id'][0]

        async_to_sync(self.channel_layer.group_add)(self.group_id, self.channel_name)
        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(self.group_id, self.channel_name)

    # Receive message from WebSocket
    def receive(self, text_data=None, bytes_data=None):
        print('WS Send message to room group')

        text_data_json = json.loads(text_data)
        # Send message to room group
        group_chat = get_object_or_404(GroupChat, id=self.group_id)
        sender = get_object_or_404(User, id=self.scope['session']['_auth_user_id'])
        recipient = get_object_or_404(User, id=text_data_json['recipient']['id'])

        async_to_sync(Message.objects.create(
            group_chat=group_chat,
            sender=sender,
            recipient=recipient,
            body=text_data_json['body'])
        )
        # Q: return Message_id send to receive_group_message?

        async_to_sync(self.channel_layer.group_send)(
            self.group_id,
            {
                'type': 'receive_group_message',
                'sender': self.scope['session']['_auth_user_id'],         # Q: send {id:, name, avatar}
                'recipient': text_data_json['recipient']['id'],
                'body': text_data_json['body']
            }
        )

    def receive_group_message(self, event):
        print('Send message to WebSocket')

        # Send message to WebSocket
        self.send(
            text_data=json.dumps(
                {
                    'sender': event['sender'],
                    'recipient': event['recipient'],
                    'body': event['body'],
                    'timestamp': f'{datetime.now()}',
                }
            )
        )

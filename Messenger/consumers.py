from channels.generic.websocket import AsyncWebsocketConsumer
import json


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        # Join room group

        # user_id = self.scope["session"]["_auth_user_id"]
        self.group_id = self.scope['url_route']['kwargs']['chat_group_id']
        await self.channel_layer.group_add(
            self.group_id,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.group_id,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data=None, bytes_data = None):
        print('WS Send message to room group')

        text_data_json = json.loads(text_data)
        recipient = text_data_json['recipient']
        body = text_data_json['body']
        # Send message to room group
        await self.channel_layer.group_send(
            self.group_id,
            {
                'type': 'receive_group_message',
                'recipient': recipient,
                'body': body
            }
        )

    async def receive_group_message(self, event):
        recipient = event['recipient']
        body = event['body']
        print('Send message to WebSocket')

        # Send message to WebSocket
        await self.send(
             text_data=json.dumps({
                'recipient': recipient,
                'body': body
        }))
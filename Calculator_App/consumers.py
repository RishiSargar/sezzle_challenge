import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer


class CalcConsumer(WebsocketConsumer):
    def connect(self):
        self.session_name = self.scope['url_route']['kwargs']['session_name']
        self.session_group_name = 'session_%s' % self.session_name

        # Join session group
        async_to_sync(self.channel_layer.group_add)(
            self.session_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.session_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.session_group_name,
            {
                'type': 'calc_message',
                'message': message
            }
        )

    # Receive message from session group
    def calc_message(self, event):
        message = event['message']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message
        }))
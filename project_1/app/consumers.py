from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
import json

class TestWebsocket(WebsocketConsumer):
    def connect(self):
        self.room_name = "test_room_name"
        self.room_group_name = "test_room_group_name"
        async_to_sync(self.channel_layer.group_add)(
            self.room_name, self.room_group_name
        )
        self.accept()
        self.send(json.dumps({'text_data':'web socket connected'}))
    
    def receive(self, text_data):
        print(text_data, 'text data')
        self.send(json.dumps({'status':'msg received'}))

    def disconnect(self, *args, **kwargs):
        print("disconnected")

    def send_notification(self, event):
        print('send_notification')
        print(event)
        data = json.loads(event.get('value'))
        self.send(text_data=json.dumps({'payload':data}))
        print("NOTIFICAION SEND")
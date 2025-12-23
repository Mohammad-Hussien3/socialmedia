from channels.generic.websocket import AsyncWebsocketConsumer
import json
from channels.db import database_sync_to_async
import asyncio

class ChatConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.senderId = int(self.scope['url_route']['kwargs']['senderId'])
        self.receiverId = int(self.scope['url_route']['kwargs']['receiverId'])
        self.room_group_name = f'chat_{self.room_name}_{min(self.senderId, self.receiverId)}_{max(self.senderId, self.receiverId)}'
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        
        await self.accept()
    

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)

        await self.channel_layer.group_send(
            
        )

    async def chat_message(self, event):
        
        await self.send(text_data=json.dumps({
            
        }))

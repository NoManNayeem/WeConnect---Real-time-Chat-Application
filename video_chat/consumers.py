import json
import logging
from channels.generic.websocket import AsyncWebsocketConsumer

logger = logging.getLogger(__name__)

class VideoChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        try:
            self.room_name = self.scope['url_route']['kwargs']['room_name']
            self.room_group_name = f'video_chat_{self.room_name}'

            # Join the room group
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )

            await self.accept()
        except Exception as e:
            logger.error(f"Error during WebSocket connection: {str(e)}")

    async def disconnect(self, close_code):
        try:
            # Leave the room group
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )
        except Exception as e:
            logger.error(f"Error during WebSocket disconnection: {str(e)}")

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            message_type = data['message']['type']

            # Depending on the message type, handle signaling messages
            if message_type in ['offer', 'answer', 'candidate']:
                # Broadcast the signaling message to the other peer
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'signal_message',
                        'message': data['message'],
                        'sender': self.channel_name,
                    }
                )
        except Exception as e:
            logger.error(f"Error during message handling: {str(e)}")

    async def signal_message(self, event):
        try:
            message = event['message']
            sender = event['sender']

            # Prevent sending the message back to the original sender
            if self.channel_name != sender:
                await self.send(text_data=json.dumps({
                    'message': message,
                }))
        except Exception as e:
            logger.error(f"Error during signaling message handling: {str(e)}")

from channels.generic.websocket import AsyncWebsocketConsumer

import json


class QuizProcessor(AsyncWebsocketConsumer):

    async def connect(
        self
        ) -> None:

        # print(self.scope['url_route'])
        self._quiz_room = self.scope['url_route']['kwargs']
        self._group = 'vegax'

        await self.channel_layer.group_add(
            self._group,
            self.channel_name
        )
        
        await self.accept()


    async def disconnect(
        self,
        code
        ) -> None:

        await self.channel_layer.group_discard(
            self._group,
            self.channel_name
        )


    async def receive(
        self,
        text_data
        ) -> None:

        json_data = json.loads(text_data)
        msg = json_data['msg']

        await self.channel_layer.group_send(
            self._group,
            {
                'type': 'chat_message',
                'msg': msg
            }
        )
        

    async def chat_message(
        self,
        event
        ) -> None:

        msg = event['msg']

        await self.send(text_data=json.dumps({
            'msg': msg
        }))
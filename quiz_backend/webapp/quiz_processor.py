import json
import datetime as dt
from pprint import pprint

from channels.generic.websocket import AsyncWebsocketConsumer


class QuizProcessor(AsyncWebsocketConsumer):

    async def connect(
        self
        ) -> None:

        # print(self.scope['url_route'])
        # self._quiz_room = self.scope['url_route']['kwargs']
        self._group = 'vegax'

        await self.channel_layer.group_add(
            self._group,
            self.channel_name
        )
        print('connect', self.channel_name)

        await self.accept()


    async def disconnect(
        self,
        code
        ) -> None:

        print('disconnect', self.channel_name)

        await self.channel_layer.group_discard(
            self._group,
            self.channel_name
        )


    async def receive(
        self,
        text_data
        ) -> None:

        json_data = json.loads(text_data)
        # msg = json_data['msg']
        msg = "now is " + str(dt.datetime.now())
        print('receive')

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
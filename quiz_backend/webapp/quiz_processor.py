import json
import datetime as dt
from pprint import pprint

from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Answer
from collections import Counter
from asgiref.sync import sync_to_async


class QuizProcessor(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_quiz()

    def init_quiz(self):
        self.cnt_o = 0
        self.cnt_x = 0

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
        select = json_data["msg"]
        msg = f"{dt.datetime.now()} msg:{json_data}"
        print(f'receive {msg}')

        counter = await self.count_peoples({"q_id": 1})
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

    @sync_to_async
    def count_peoples(self, event) -> None:
        # Not stateful work
        q_id = event["q_id"]
        answers = Answer.objects.filter(question=q_id)

        counter = Counter(
            [x.selection for x in answers]
        )
        print(f"{q_id} : {counter}")
        return counter

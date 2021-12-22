import json
import datetime as dt
from .logger import get_logger

import time
import pickle
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Answer
from collections import Counter, OrderedDict
from asgiref.sync import sync_to_async


logger = get_logger()


class Quiz:
    def __init__(self, question, correct_answer, explanation, image_url, create_time):
        self.question = question
        self.correct_answer = correct_answer
        self.explanation = explanation
        self.image_url = image_url
        self.create_time = create_time

        # k : user_id, v: select('o' or 'x')
        self.users = OrderedDict()

    def update_user(self, user_id, select, submit_time):
        self.users[user_id] = {"select": select, "submit_time": submit_time}

    def calculate_scores(self):
        sorted_times = OrderedDict(sorted(
            self.users.items(),
            key=lambda item: item[1]["submit_time"]
        ))

        cur_extra = 63
        for user_id, user in sorted_times.items():
            self.users[user_id]["score"] = int(user["select"] == self.correct_answer)
            self.users[user_id]["extra_score"] = cur_extra
            cur_extra = max(cur_extra // 2, 0)

    def show_answer(self):
        """show answer and explanation

        Returns:
            user ox list
        """
        pass


class QuizQuizConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.quizs = {}
        self.cur_q_id = 1

    async def connect(self) -> None:
        # print(self.scope['url_route'])
        # self._quiz_room = self.scope['url_route']['kwargs']
        self._group = 'vegax'

        await self.channel_layer.group_add(
            self._group,
            self.channel_name
        )
        logger.info(f"Connect channel_name:{self.channel_name}")
        await self.accept()

    async def disconnect(self, code) -> None:
        logger.info(f"Disconnect channel_name:{self.channel_name}")
        await self.channel_layer.group_discard(
            self._group,
            self.channel_name
        )

    async def receive_submit(self, data) -> None:
        submit_time = time.time()
        user_id = data["user_id"]
        q_id = data["q_id"]
        select = data["select"]

        quiz = self.quizs[q_id]
        quiz.update_user(user_id, select, submit_time)

        counter = dict(Counter([
            x["select"] for x in quiz.users.values()
        ]))

        msg = f"{dt.datetime.now()} msg:{data} {counter}"
        logger.info(f"Broadcast msg:{msg}")

        await self.channel_layer.group_send(
            self._group,
            {'type': 'chat_message', 'msg': msg}
        )

    async def create_question(self, question):
        q_id = question.pop("number")

        if q_id != 1:
            self.quizs[self.cur_q_id].calculate_scores()
            logger.info(f"Dump Q : {self.quizs}")
            # with open(f"dump_quiz.pkl", 'w') as f:
            #     pickle.dump(self.quizs, f)

        if q_id in self.quizs:
            raise ValueError()

        self.cur_q_id = q_id
        self.quizs[q_id] = Quiz(**question)

        msg = f"Create q_id:{q_id} Q:{question}"
        logger.info(msg)
        await self.channel_layer.group_send(
            self._group,
            {'type': 'chat_message', 'msg': msg}
        )

    async def receive(self, text_data) -> None:
        data = json.loads(text_data)
        logger.info(f"Receive data:{data}")
        type_ = data.pop("type")

        if type_ == "question":
            await self.create_question(data)
        elif type_ == "submit":
            await self.receive_submit(data)

    async def chat_message(self, event) -> None:
        await self.send(text_data=json.dumps({
            'msg': event['msg']
        }))

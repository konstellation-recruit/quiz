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
    def __init__(self, q_id, question, correct_answer, explanation, image_url, create_time):
        self.q_id = q_id
        self.question = question
        self.correct_answer = correct_answer
        self.explanation = explanation
        self.image_url = image_url
        self.create_time = create_time

        # k : user_id, v: select('o' or 'x')
        self.users = OrderedDict()

    def update_user(self, user_id, name, select, submit_time):
        self.users[user_id] = {"select": select, "name": name, "submit_time": submit_time}

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

    def get_quiz(self):
        quiz_data = {
            "msg_type": "create_question",
            "q_id": self.q_id,
            "question": self.question,
            "image_url": self.image_url
        }
        return quiz_data

    def show_answer(self):
        """show answer and explanation

        Returns:
            user ox list
        """
        select_o, select_x = [], []
        print(list(self.users.values()))

        for user in self.users.values():
            if user["select"] == "o":
                select_o.append(user["name"])
            elif user["select"] == "x":
                select_x.append(user["name"])

        quiz_data = {
            "msg_type": "show_answer",
            "q_id": self.q_id,
            "correct_answer": self.correct_answer,
            "explanation": self.explanation,
            "question": self.question,
            "image_url": self.image_url,
            "select_o": select_o,
            "select_x": select_x,
        }
        return quiz_data


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
        name = data["name"]
        q_id = data["q_id"]
        select = data["select"]

        quiz = self.quizs[q_id]
        quiz.update_user(user_id, name, select, submit_time)

        data = dict(Counter([
            x["select"] for x in quiz.users.values()
        ]))

        logger.info(f"OX Submit data:{data}")

        await self.channel_layer.group_send(
            self._group,
            {'type': 'chat_message', 'data': data}
        )

    async def create_question(self, question):
        q_id = question.pop("number")
        if q_id in self.quizs:
            raise ValueError()

        self.cur_q_id = q_id
        self.quizs[q_id] = Quiz(q_id, **question)

        quiz_data = self.quizs[q_id].get_quiz()

        logger.info(f"Create Q : {quiz_data}")
        await self.channel_layer.group_send(
            self._group,
            {'type': 'chat_message', 'data': quiz_data}
        )

    async def show_answer(self, q_id):
        self.quizs[q_id].calculate_scores()
        answer_data = self.quizs[q_id].show_answer()
        logger.info(f"Show A : {answer_data}")
        await self.channel_layer.group_send(
            self._group,
            {'type': 'chat_message', 'data': answer_data}
        )

    async def receive(self, text_data) -> None:
        data = json.loads(text_data)
        logger.info(f"Receive data:{data}")
        msg_type = data.pop("msg_type")

        if msg_type == "create_question":
            await self.create_question(data)
        elif msg_type == "show_answer":
            await self.show_answer(data["q_id"])
        elif msg_type == "submit":
            await self.receive_submit(data)
        else:
            raise ValueError(f"Check msg_type {msg_type}")

    async def chat_message(self, event) -> None:
        await self.send(text_data=json.dumps(event['data']))

import asyncio
import json

import websockets

from global_utils import init_django
init_django()

from webapp.utils import update_scores

# NOTE with this example, you cannot experiment scoring. so use this only
# for the first development phase

questions = [
    {
        'number': 1,
        'question': 'You are awesome',
        'correct_answer': 'o',
        'explanation': 'Because you are goodlooking',
        'image_url': 'https://www.w3schools.com/css/img_lights.jpg'
    },
    {
        'number': 2,
        'question': 'You are bad',
        'correct_answer': 'o',
        'explanation': 'Because you are a badass',
        'image_url': 'https://www.w3schools.com/css/img_forest.jpg'
    }
]


async def hello():
    async with websockets.connect("ws://localhost:8000/ws/quiz/") as websocket:
        while True:
            for q in questions:
                await websocket.send(json.dumps({'msg': "Hello world!"}))
                await websocket.recv() ## is this needed?
                await asyncio.sleep(1)

                # TODO
                """
                Repeat the below for each question

                1. send the number, question, and image_url
                2. on update on user answers
                    - broadcast new states to all users (o/x counts and all)
                3. 20 seconds after sending question, compute scores and (use `update_scores`)
                  send the new scores to the users. also send the correct answer
                """

asyncio.run(hello())

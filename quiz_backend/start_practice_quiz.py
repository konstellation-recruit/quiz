import asyncio
import json
import time

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


async def send_user_ox(ws, q_id):
    await ws.send(json.dumps({
        "msg_type": "submit",
        "user_id": "qwer@svn.com",
        "name": "foo",
        "q_id": q_id,
        "select": 'o' # select is must be 'o' or 'x'
    }))
    await ws.recv() # is this needed?
    await asyncio.sleep(1)

    await ws.send(json.dumps({
        "msg_type": "submit",
        "user_id": "qwer@svn.com",
        "name": "foo",
        "q_id": q_id,
        "select": 'x' # select is must be 'o' or 'x'
    }))
    await ws.recv() # is this needed?
    await asyncio.sleep(1)

    await ws.send(json.dumps({
        "msg_type": "submit",
        "user_id": "asdf@svn.com",
        "name": "bar",
        "q_id": q_id,
        "select": 'o' # select is must be 'o' or 'x'
    }))
    await ws.recv() # is this needed?
    await asyncio.sleep(1)

    await ws.send(json.dumps({
        "msg_type": "submit",
        "user_id": "asdf@svn.com",
        "name": "bar",
        "q_id": q_id,
        "select": 'o' # select is must be 'o' or 'x'
    }))
    await ws.recv() # is this needed?
    await asyncio.sleep(1)


async def create_question(ws, question):
    create_q_time = time.time()
    data = {"msg_type": "create_question", **question, "create_time": create_q_time}
    await ws.send(json.dumps(data))
    await ws.recv() # is this needed?
    # await asyncio.sleep(1)
    return create_q_time

async def show_answer(ws, q_id):
    data = {"msg_type": "show_answer", "q_id": q_id}
    await ws.send(json.dumps(data))
    await ws.recv() # is this needed?
    await asyncio.sleep(5)


async def main():
    submit_time = 15 # sec
    answer_time = 10
    async with websockets.connect("ws://localhost:8000/ws/quiz/") as ws:
        for q in questions:
            create_q_time = await create_question(ws, q)

            await asyncio.sleep(submit_time)
            # while (time.time() - create_q_time <= submit_time):
                
            # await send_user_ox(ws, q["number"])

            await show_answer(ws, q["number"])
            await asyncio.sleep(answer_time)


asyncio.run(main())

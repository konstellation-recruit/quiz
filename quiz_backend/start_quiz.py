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
        'question': 'Bitcoin was invented in 2008 by an unknown person or group of people using the name Natoshi Sakamoto.',
        'correct_answer': 'x',
        'explanation': 'The correct name is Satoshi Nakamoto.',
        'image_url': 'http://3.34.250.24:8001/1.png'
    },
    {
        'number': 2,
        'question': 'The most expensive nft sold ever was ‘Everydays: The First 5000 Days’.',
        'correct_answer': 'o',
        'explanation': 'it was sold for $69.3 million. The second most expensive nft ever sold was Human One and its price was $28.9 million.',
        'image_url': 'http://3.34.250.24:8001/2.png'
    },
    {
        'number': 3,
        'question': 'The name of the model dog in Dogecoin’s meme is Kaboshu',
        'correct_answer': 'o',
        'explanation': "Din't you know?",
        'image_url': 'http://3.34.250.24:8001/3.png'
    },
    {
        'number': 4,
        'question': 'The most widely used token standard of Ethereum is ERC-02',
        'correct_answer': 'x',
        'explanation': "The correct name is ERC-20.",
        'image_url': 'http://3.34.250.24:8001/4.png'
    },
    {
        'number': 5,
        'question': 'Solana is the name of a beach located in Miami',
        'correct_answer': 'x',
        'explanation': "Solana beach is located in California.",
        'image_url': 'http://3.34.250.24:8001/5.png'
    },
    {
        'number': 6,
        'question': 'Bitcoin’s genesis block contains the following hidden messages: "The Times 03/Jan/2009 Chancellor on brink of second bailout for banks".',
        'correct_answer': 'o',
        'explanation': "Satoshi Nakamoto is a badass, right?",
        'image_url': 'http://3.34.250.24:8001/6.png'
    },
    {
        'number': 7,
        'question': 'ADA Coin’s blockchain network name is Cardano.',
        'correct_answer': 'o',
        'explanation': "Din't you know?",
        'image_url': 'http://3.34.250.24:8001/7.png'
    },
    {
        'number': 8,
        'question': 'NFT stands for Not For Trading.',
        'correct_answer': 'x',
        'explanation': "NFT stands for Non-Fungible Token and it is tradable.",
        'image_url': 'http://3.34.250.24:8001/8.png'
    },
    {
        'number': 9,
        'question': 'Ether is the oldest crypto currency among Ether, ADA, Doge and Tether.',
        'correct_answer': 'x',
        'explanation': "Dogecoin is the one with the longest history",
        'image_url': 'http://3.34.250.24:8001/9.png'
    },
    {
        'number': 10,
        'question': 'Bitcoin is the world’s most actively traded crypto currency in volume',
        'correct_answer': 'x',
        'explanation': "Tether is the most actively traded crypto currency.",
        'image_url': 'http://3.34.250.24:8001/10.png'
    },
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
    await asyncio.sleep(1)
    return create_q_time

async def show_answer(ws, q_id):
    data = {"msg_type": "show_answer", "q_id": q_id}
    await ws.send(json.dumps(data))
    await ws.recv() # is this needed?
    await asyncio.sleep(5)


async def main():
    submit_time = 16 # sec
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

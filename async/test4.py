# -*- coding: utf-8 -*-

import asyncio
import requests
import time


start = time.time()


async def get_url(url):

    return requests.get(url)


async def request():

    url = "http://127.0.0.1:5000"

    print("Waiting for :", url)
    # await 修饰 协程对象
    response = await get_url(url)

    print('Get response from', url, 'Result:', response.text)


tasks = [asyncio.ensure_future(request()) for _ in range(5)]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print("Cost time: ", end-start)
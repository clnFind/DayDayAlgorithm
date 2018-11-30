# -*- coding: utf-8 -*-

import asyncio
import aiohttp
import time


start = time.time()


async def get_url(url):
    """
    使用 aiohttp 达到异步并发 速度更快
    :param url:
    :return:
    """
    session = aiohttp.ClientSession()
    response = await session.get(url)
    result = await response.text()
    session.close()
    return result


async def request():
    url = "http://127.0.0.1:5000"
    print("Waiting for: ", url)
    result = await get_url(url)
    print("Get response from ", url, "Result: ", result)


# 请求5次 和 100次，时间均为 3.x 秒
# tasks = [asyncio.ensure_future(request()) for _ in range(5)]
tasks = [asyncio.ensure_future(request()) for _ in range(100)]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print("Cost time: ", end-start)

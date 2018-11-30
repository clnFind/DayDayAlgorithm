# -*- coding: utf-8 -*-

import asyncio



async def execute(x):
    print("Number: ", x)


coroutine = execute(1)
print('Coroutine:', coroutine)
print('After calling execute')

# 协程调用的三种方式
# loop = asyncio.get_event_loop()
# loop.run_until_complete(coroutine)
# print('After calling loop')

# loop = asyncio.get_event_loop()
# task = loop.create_task(coroutine)
# print('Task:', task)
# loop.run_until_complete(task)
# print('Task:', task)
# print('After calling loop')

task = asyncio.ensure_future(coroutine)
print('Task:', task)
loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print('Task:', task)
print('After calling loop')



# -*- coding: utf-8 -*-

import asyncio
import requests


async def request():
    url = "https://www.baidu.com"
    status = requests.get(url)
    return status


def callback(task):

    print("Status: ", task)


# 单任务协程
coroutine = request()
task = asyncio.ensure_future(coroutine)

# 绑定回调
task.add_done_callback(callback)
print("Task: ", task)

loop = asyncio.get_event_loop()
loop.run_until_complete(task)
print("Tasksssss: ", task)

print('Task Result:', task.result())

# 多任务协程
tasks = [asyncio.ensure_future(request()) for _ in range(5)]
print("Multi tasks...: ", tasks)

loops = asyncio.get_event_loop()
loops.run_until_complete(asyncio.wait(tasks))
for task in tasks:
    print("Tasksssss result: ", task.result())
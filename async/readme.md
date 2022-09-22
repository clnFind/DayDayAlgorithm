### 协程使用测试（代码借鉴于网络）

* python 版本：3.6.0
* 依赖库：flask 、aiohttp
    * pip install flask
    * pip install aiohttp
    
* test1.py、test2.py 测试协程单任务和多任务效率
* test3.py、test4.py 多任务测试， 使用await 和不使用 效率差不多
* test5.py 使用aiohttp 和 协程，效率是使用协程的大约1/5, 效率很高 


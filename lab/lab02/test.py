def simple_coroutine():
    print("Coroutine started")
    x = yield
    print(f"Received: {x}")

coro = simple_coroutine()
next(coro)  # 启动协程
coro.send(42)  # 恢复执行并发送值

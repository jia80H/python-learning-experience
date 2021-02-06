import multiprocessing

# 创建队列是，可以指定最大长度， 默认为0（无限长）
q = multiprocessing.Queue(5)

q.put('h')
q.put('l')
q.put('hl')
q.put('hk')
q.put('hg')

print(q.full())  # 判断队列是否满

# 进程不会停止，放不进去，等待
# q.put('hf')

# block: 队列满时阻塞与否
# timeout: 等待多久程序出错
q.put('how', block=True, timeout=1)

q.put_nowait('how')  # 等价于 q.put('how', block=False)

q.get(block=True, timeout=1)
q.get_nowait()

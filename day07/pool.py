"""
进程池使用演示
"""
from multiprocessing import Pool
from time import sleep, ctime


# 进程池事件函数
def worker(msg):
    sleep(2)
    print(ctime(), '------', msg)
    return 8888


# 创建进程池
pool = Pool(4)

# 向进程池中添加事件
for i in range(10):
    msg = "Tedu %d" % i
    r = pool.apply_async(func=worker,
                         args=(msg,))

# 关闭进程池
pool.close()

# 回收进程池
pool.join()
print(r.get())  # 获取进程池事件函数返回值

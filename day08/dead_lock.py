"""
模拟死锁的过程
"""
from time import sleep
from threading import Thread, Lock


# 账户类
class Account:
    def __init__(self, _id, balance, lock):
        self.id = _id  # 账户名
        self.balance = balance  # 存款
        self.lock = lock  # 锁

    # 取钱
    def withdraw(self, amount):
        self.balance -= amount

    # 存钱
    def deposit(self, amount):
        self.balance -= amount

    # 查看余额
    def get_balance(self):
        return self.balance


# 创建两个账户
Tom = Account('Tom', 5000, Lock())
Alex = Account('Alex', 8000, Lock())


def transfer(from_, to, amount):
    """

    :param from_:
    :param to:
    :param amount:
    :return:
    """
    from_.lock.acquire()  # from_上锁
    from_.withdraw(amount)  # from_减少
    to.lock.acquire()  # to上锁
    to.deposit(amount)  # to钱增加
    to.lock.release()  # to解锁
    from_.lock.release()  #


t1 = Thread(target=transfer, args=(Tom, Alex, 1500))
t1.start()
t1.join()

print("Tom:", Tom.get_balance())
print("Alex:", Alex.get_balance())

import time
import multiprocessing


def deposit(balance, amt,lock):
    for i in range(amt):
        lock.acquire()
        balance.value += i
        lock.release()


def withdraw(balance, amt,lock):
    for i in range(amt):
        lock.acquire()
        balance.value -= i
        lock.release()


if __name__ == '__main__':
    balance = multiprocessing.Value('i', 455554)
    lock = multiprocessing.Lock()
    p1 = multiprocessing.Process(target=deposit, args=(balance, 2344, lock))
    p2 = multiprocessing.Process(target=withdraw, args=(balance, 2344, lock))
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print(balance.value)
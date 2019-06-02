

class Person(object):
    __age = 11

    @property
    def age(self):
        return self.__age


# 进程池

from multiprocessing import Pool
import os, time, random


def worker(msg):
    t_start = time.time()
    print(f"{msg} begin, Pid: {os.getpgid()}")
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print(f"{msg} finish, time: {t_stop - t_start}")


# 多线程共同操作同一个数据互斥锁同步
import threading
import time

num = 0
mutex = threading.Lock()


class MyThread(threading.Thread):

    def run(self):
        global num
        time.sleep(1)

        if mutex.acquire():
            num += 1
            msg = self.name + " set num to " + str(num)
            print(msg)
            mutex.release()


def test():
    for i in range(5):
        t = MyThread()
        t.start()


if __name__ == '__main__':
    # p = Person()
    # print(p.age)
    # po = Pool(3)
    # for i in range(0, 10):
    #     po.apply_async(worker, args=(i,))
    # print("____start______")
    # po.close()
    # po.join()
    # print("________End______")
    test()


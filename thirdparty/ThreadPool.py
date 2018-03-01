# coding:utf-8
# 模拟一个进城池 线程池，可以向里面添加任务，

import threading
import time
import traceback
from lib.core.data import logger
import Queue
import random

class w8_threadpool:

    def __init__(self,threadnum,func_scan):
        self.thread_count = self.thread_nums = threadnum
        self.scan_count_lock = threading.Lock()
        self.thread_count_lock = threading.Lock()
        self.load_lock = threading.Lock()
        self.scan_count = 0
        self.isContinue = True
        self.func_scan = func_scan
        self.queue = Queue.Queue()

    def push(self,payload):
        self.queue.put(payload)

    def changeScanCount(self,num):
        self.scan_count_lock.acquire()
        self.scan_count += num
        self.scan_count_lock.release()

    def changeThreadCount(self,num):
        self.thread_count_lock.acquire()
        self.thread_count += num
        self.thread_count_lock.release()

    def run(self):
        th = []
        for i in range(self.thread_nums):
            t = threading.Thread(target=self.scan, name=str(i))
            t.setDaemon(True)
            t.start()
            th.append(t)
        
        for tt in th:
            tt.join()
        # It can quit with Ctrl-C
        # while 1:
        #     if self.thread_count > 0 and self.isContinue:
        #         time.sleep(0.01)
        #     else:
        #         break
    def stop(self):
        self.load_lock.acquire()
        self.isContinue = False
        self.load_lock.release()
        
    def scan(self):
        while 1:
            self.load_lock.acquire()
            if self.queue.qsize() > 0 and self.isContinue:
                payload = self.queue.get()

                self.load_lock.release()
            else:
                self.load_lock.release()
                break
            try:
                # POC在执行时报错如果不被处理，线程框架会停止并退出
                self.func_scan(payload)
            except KeyboardInterrupt:
                self.isContinue = False
                raise KeyboardInterrupt
            except Exception:
                errmsg = traceback.format_exc()
                self.isContinue = False
                logger.error(errmsg)

            self.changeScanCount(-1)
        self.changeThreadCount(-1)


if __name__ == '__main__':
    # def calucator(num):
    #     i = random.randint(1, 100)
    #     u = num
    #     a = i * u
    #     if (a % 6 == 0):
    #         for x in range(5):
    #             print "new thread"
    #             p.push(x)

    # p = w8_threadpool(3, calucator)
    # for i in range(100000):
    #     p.push(i)
    # p.run()
    pass


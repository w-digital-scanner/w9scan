# coding:utf-8

import random
from dummy import *

if __name__ == '__main__':
    def calucator(num):
        i = random.randint(1, 100)
        u = num
        a = i * u
        print a

    p = ThreadPool(3, calucator)
    for i in range(100):
        p.push(i)
    p.run()


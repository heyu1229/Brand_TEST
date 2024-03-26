# -*-coding:utf-8-*-

from time import ctime, sleep

import threading

loops = [4, 2,5,6]


class MyThread(object):

    def __init__(self, func, args, name=''):
        self.name = name

        self.func = func

        self.args = args

    def __call__(self):
        self.func(*self.args)


def loop(nloop, nsec):
    print('start loop', nloop, 'at :', ctime())

    sleep(nsec)

    print('done loop', nloop, 'at:', ctime())

def main():

    print('start at',ctime())

    threads = []

    nloops = range(len(loops))

    for i in nloops:

        t = threading.Thread(target=MyThread(loop, (i, loops[i]), loop.__name__))

        threads.append(t)

    for i in nloops:   # start threads 此处并不会执行线程，而是将任务分发到每个线程，同步线程。等同步完成后再开始执行start方法

        threads[i].start()

    for i in nloops:   # jion()方法等待线程完成

        threads[i].join()

    print('DONE AT:', ctime())

if __name__ == '__main__':

    main()
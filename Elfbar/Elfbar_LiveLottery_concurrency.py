# -*-coding:utf-8-*-


# -*- coding:UTF-8 -*-
import pytest,json,threading
import requests
import time,base64
#---------------elfbar周年庆直播抽奖   并发----------------------
import xlrd2



class MyThread(object):

    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)


def loop(code, nsec):
    print("lisa",code)
    Url = "http://test.elfbar.com/activity/liveLottery"   #

    headers = {"cookie": "authed=1"}
    payload = {
    }
    result = requests.post(Url, data=payload, headers=headers)  # 或者直接json=payload
    result = result.json()
    print(result)

    time.sleep(nsec)

    print('done loop', code, 'at:', time.ctime())

def main():

    #---------------------Excel表获得Code-----------------------------------
    # 打开文件
    workbook = xlrd2.open_workbook(r'/Users/lisa/python310/Other/Geekbar/verifycode.xlsx')
    # 获取所有sheet
    sheet_name = workbook.sheet_names()[0]
    # 根据sheet索引或者名称获取sheet内容
    sheet = workbook.sheet_by_index(0)  # sheet索引从0开始
    rows = sheet.row_values(0)  # 获取第1行内容
    i = 0
    code_list = []
    for i in range(182):
        code = sheet.cell_value(i, 0)
        code_list.append(code)
    # print("Excel获取Code：", code_list)
    print('start at', time.ctime())

    threads = []
    nloops = range(len(code_list))

    for i in nloops:
        t = threading.Thread(target=MyThread(loop, (code_list[i], 2), loop.__name__))
        threads.append(t)

    for i in nloops:   # start threads 此处并不会执行线程，而是将任务分发到每个线程，同步线程。等同步完成后再开始执行start方法

        threads[i].start()

    for i in nloops:   # jion()方法等待线程完成

        threads[i].join()

    print('DONE AT:', time.ctime())

if __name__ == '__main__':

    main()
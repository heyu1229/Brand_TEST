'''
@create : lisa
@file :hs_deliver.py
@Date :2021/7/27
@desc :

'''

# -*- coding:UTF-8 -*-
import unittest,json,threading
import requests,csv
import time,gc
import hashlib
from urllib.parse import urlencode
#---------------HG   hs发货并发----------------------
import xlrd2

tables = []
class hs_deliver():

    def __init__(self):

        self.Url = "https://beta.deepvaping.co.uk/api/hs/deliver"
        self.HGapi = "HeavengiftsAPI"

    def post1(self):

        # 打开文件
        workbook = xlrd2.open_workbook ( r'/Users/lisa/python310/Other/deliver.xlsx' )
        # 获取所有sheet
        sheet_name = workbook.sheet_names ()[0]

        # 根据sheet索引或者名称获取sheet内容
        sheet = workbook.sheet_by_index ( 0 )  # sheet索引从0开始
        rows = sheet.row_values ( 0 )  # 获取第1行内容
        a1 = {"requestId": "", "orderId": ""}
        a1["requestId"] = sheet.cell_value ( 0, 0 )
        a1["orderId"] = sheet.cell_value ( 0, 1 )
        print(a1)
        # for rown in range(rows):
        #     a1 = {"requestId":"","orderId":""}
        #     a1["requestId"]=str(sheet.cell_value(rown,0))
        #     a1["orderId"] = sheet.cell_value ( rown, 1 )
        #     tables.append ( a1 )

        try:
            #HG生成md5
            m = hashlib.md5 ()
            m.update ( self.HGapi.encode ( "utf8" ) )
            HG_api_md5 = m.hexdigest ()
            #时间戳转str
            t = time.time ()
            t = int(t)
            timestamp = str(t)
            print(t)

            data = {"requestId":a1["requestId"],"orderId":a1["orderId"],
                    "operator":"carol.yao","logiId":"bbbbbbbb","shippingId":"1","shipStatus":1,
                    "grossWeight":22,"memo":"","toUpdate":1,"amountInfo":{"costItems":69.08,"shippingFee":2,
                    "discountedAmount":0,"otherFee":30,"otherFeeDetail":{"handling_fee":10,"tax_fee":20}}}
            data_str = json.dumps(data)

            token1 = str(HG_api_md5)+timestamp+data_str
            # print(token1)
            m = hashlib.md5 ()
            m.update ( token1.encode ( "utf8" ) )
            token = m.hexdigest ()
            # print(token)
            #请求发货接口
            payload = {"token": token,"timestamp":timestamp,"data":data_str}

            headers = {"User-Agent":"PostmanRuntime/7.28.1","Accept": "*/*", "Accept-Encoding": "gzip, deflate, br", "Connection": "keep-alive",
                       "Content-Type": "application/x-www-form-urlencoded" }
            result = requests.post ( self.Url, data=payload,headers=headers )
            result = result.json ()
            print ( result )
        except Exception as e:
            print(e)

    def post2(self):

        # 打开文件
        workbook = xlrd2.open_workbook ( r'/Users/lisa/python310/Other/deliver.xlsx' )
        # 获取所有sheet
        sheet_name = workbook.sheet_names ()[0]

        # 根据sheet索引或者名称获取sheet内容
        sheet = workbook.sheet_by_index ( 0 )  # sheet索引从0开始
        rows = sheet.row_values ( 1 )  # 获取第2行内容
        a2 = {"requestId": "", "orderId": ""}
        a2["requestId"] = sheet.cell_value ( 1, 0 )
        a2["orderId"] = sheet.cell_value ( 1, 1 )
        print(a2)
        # for rown in range ( rows ):
        #     a1 = {"requestId": "", "orderId": ""}
        #     a1["requestId"] = str ( sheet.cell_value ( rown, 0 ) )
        #     a1["orderId"] = sheet.cell_value ( rown, 1 )
        #     tables.append ( a1 )

        try:
            # HG生成md5
            m = hashlib.md5 ()
            m.update ( self.HGapi.encode ( "utf8" ) )
            HG_api_md5 = m.hexdigest ()
            # 时间戳转str
            t = time.time ()
            t = int ( t )
            timestamp = str ( t )
            print ( t )

            data = {"requestId": a2["requestId"], "orderId": a2["orderId"],
                    "operator": "carol.yao", "logiId": "bbbbbbbb", "shippingId": "1", "shipStatus": 1,
                    "grossWeight": 22, "memo": "", "toUpdate": 1,
                    "amountInfo": {"costItems": 69.08, "shippingFee": 2,
                                   "discountedAmount": 0, "otherFee": 30,
                                   "otherFeeDetail": {"handling_fee": 10, "tax_fee": 20}}}
            data_str = json.dumps ( data )

            token1 = str ( HG_api_md5 ) + timestamp + data_str
            # print(token1)
            m = hashlib.md5 ()
            m.update ( token1.encode ( "utf8" ) )
            token = m.hexdigest ()
            # print(token)
            # 请求发货接口
            payload = {"token": token, "timestamp": timestamp, "data": data_str}

            headers = {"User-Agent": "PostmanRuntime/7.28.1", "Accept": "*/*",
                       "Accept-Encoding": "gzip, deflate, br", "Connection": "keep-alive",
                       "Content-Type": "application/x-www-form-urlencoded"}
            result = requests.post ( self.Url, data=payload, headers=headers )
            result = result.json ()
            print ( result )
        except Exception as e:
            print ( e )


# if __name__ == '__main__':
#     unittest.main()
def deliver1():
    deliver = hs_deliver()
    return deliver.post1()

def deliver2():
    deliver = hs_deliver()
    return deliver.post2()

try:
    i = 0
    # 开启线程数目
    tasks_number = 1
    print('测试启动')
    time1 = time.perf_counter()
    while i < tasks_number:
        t1 = threading.Thread(target=deliver1)
        t1.start()
        t2 = threading.Thread(target=deliver2)
        t2.start()
        i +=1
    time2 = time.perf_counter()
    times = time2 - time1
    print(times/tasks_number)
except Exception as e:
    print(e)

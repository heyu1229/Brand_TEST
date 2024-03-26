'''
@create : lisa
@file :hs_deliver.py
@Date :2021/7/27
@desc :

'''

# -*- coding:UTF-8 -*-
import unittest,json
import requests
import time,gc
import hashlib
from urllib.parse import urlencode
#---------------HG   hs发货----------------------
class hs_deliver(unittest.TestCase):

    def setUp(self):

        self.Url = "https://apibeta.heavengifts.com/hs/deliver"
        self.HGapi = "HeavengiftsAPI"


    def testcase_001(self):
        #HG生成md5
        m = hashlib.md5 ()
        m.update ( self.HGapi.encode ( "utf8" ) )
        HG_api_md5 = m.hexdigest ()
        #时间戳转str
        t = time.time ()
        t = int(t)
        timestamp = str(t)

        data = {"requestId":1003,"orderId":"20210723168400",
                "operator":"carol.yao","logiId":"bbbbbbbb","shippingId":"1","shipStatus":1,
                "grossWeight":22,"memo":"","toUpdate":1,"amountInfo":{"costItems":69.08,"shippingFee":2,
                "discountedAmount":0,"otherFee":30,"otherFeeDetail":{"handling_fee":10,"tax_fee":20}}}
        data_str = json.dumps(data)
        # data_str = str(data)
        # print(type(data_str))

        token1 = str(HG_api_md5)+timestamp+data_str
        # print(token1)
        m = hashlib.md5 ()
        m.update ( token1.encode ( "utf8" ) )
        token = m.hexdigest ()
        # print(token)
        #请求发货接口
        payload = {"token": token,"timestamp":timestamp,"data":data_str}
        print(payload)

        headers = {"User-Agent":"PostmanRuntime/7.28.1","Accept": "*/*", "Accept-Encoding": "gzip, deflate, br", "Connection": "keep-alive",
                   "Content-Type": "application/x-www-form-urlencoded" }
        result = requests.post ( self.Url, data=payload,headers=headers )
        result = result.json ()
        print ( result )

if __name__ == '__main__':
    unittest.main()
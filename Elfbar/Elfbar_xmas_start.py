'''
@create : lisa
@file :Elfbar
@Date :2022/11/24
@desc :

'''

# -*- coding:UTF-8 -*-
import pytest,json
import requests,allure
import time,gc
import hashlib
from urllib.parse import urlencode
#---------------elfbar圣诞节抓娃娃---游戏开始接口----------------------

@allure.feature("")
class Test_Xmas_start:

    def setup(self):
        self.Url ="http://test.elfbar.com/xmas/start"
        with allure.step(f"接口地址：{self.Url}"):
             print(self.Url)

    @allure.title("")
    def test_001(self):
        headers = {"Access-Control-Expose-Headers":"Authorization",
                   "Authorization":"Bearer 895dFcQC7EWP5r6N_1LiQTB4cyjmNxD9P7qfNneJJMErzDTh6MtbFC3RUomX89D7zjAXumq8_J4kAGIkFur6eGW5Na7xrO2LeidSyxizJh-7y4Qx",
                   "Content-Language":"en","Content-Type":"application/json",
                   "Cookie":"token=Bearer%20895dFcQC7EWP5r6N_1LiQTB4cyjmNxD9P7qfNneJJMErzDTh6MtbFC3RUomX89D7zjAXumq8_J4kAGIkFur6eGW5Na7xrO2LeidSyxizJh-7y4Qx; _gid=GA1.2.1170450732.1670230982; _gat_gtag_UA_48674434_15=1; PHPSESSID=jqg2pocjkbr89oroc04fa3k1sg; T_XMAS_CLAW_AUTH=895dFcQC7EWP5r6N_1LiQTB4cyjmNxD9P7qfNneJJMErzDTh6MtbFC3RUomX89D7zjAXumq8_J4kAGIkFur6eGW5Na7xrO2LeidSyxizJh-7y4Qx; __atuvc=2%7C49; __atuvs=638db3c3693c5928001; _ga=GA1.2.623706266.1670230982; _ga_8G02ZXM69R=GS1.1.1670230496.3.1.1670231029.0.0.0"}
        payload = {
        }
        result = requests.post( self.Url, data=payload,headers=headers)#或者直接json=payload
        result = result.json()
        print(result)


if __name__ == '__main__':
    pytest.main(['-s','Elfbar_xmas_start.py'])


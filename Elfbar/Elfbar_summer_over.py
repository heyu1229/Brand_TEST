'''
@create : lisa
@file :Elfbar
@Date :2022/11/24
@desc :

'''

# -*- coding:UTF-8 -*-
import pytest,json,base64
import requests,allure
import time,gc
import hashlib
from urllib.parse import urlencode
#---------------elfbar圣诞节抓娃娃---游戏开始接口----------------------

@allure.feature("")
class Test_summer_over:

    def setup(self):
        self.Url ="http://test2.elfbar.com/summer/over"
        with allure.step(f"接口地址：{self.Url}"):
             print(self.Url)

    @allure.title("")
    def test_001(self):
        headers = {"Access-Control-Expose-Headers":"Authorization",
                   "Authorization":"Bearer ef38kbiEE69zLlD32NxvHwW9LVCYY8LC0tzHEnueXz7w0ZwallPsIR72BnX1B3lzCEvl7baLKAF7c9dwnMZZYhp_IbiL3kTL-bUpoleMYck4acSY64Zhv5gFNSAZgJ277GRNREgJnVyTIw8ULXfdaDdHg9U8hZ9i1a9JLf4iGcHUKYEligX6zZfFGG2My1lOQw5ImCcv91T3HOiFoLLse86OSFxsYFbQTMnu5AJdHWnpmshohUo26GXCZZ7rA47Z3gJlYDBZPIGXqYBqdhrS8USVnUyos1xhCbG1ZzrE27BDb9zbjzz1y3D4D5Dbycn62rJSRJ_zXaKYhY7vpaEhvTi97dbpQtLV7KBHa1q7mTadxKEH4tS0BCCMK9Lh9t9yYOECy62DGtIvMQ",
                   "Content-Language":"en","Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
                   "Cookie":"__atuvc=1%7C16; __atuvs=643f7f3da9501c3a000; _ga_8G02ZXM69R=GS1.1.1681882944.1.1.1681882944.0.0.0; _ga=GA1.2.1268404092.1681882944; _gid=GA1.2.1036935313.1681882945; _gat_gtag_UA_48674434_15=1; token=Bearer+ef38kbiEE69zLlD32NxvHwW9LVCYY8LC0tzHEnueXz7w0ZwallPsIR72BnX1B3lzCEvl7baLKAF7c9dwnMZZYhp_IbiL3kTL-bUpoleMYck4acSY64Zhv5gFNSAZgJ277GRNREgJnVyTIw8ULXfdaDdHg9U8hZ9i1a9JLf4iGcHUKYEligX6zZfFGG2My1lOQw5ImCcv91T3HOiFoLLse86OSFxsYFbQTMnu5AJdHWnpmshohUo26GXCZZ7rA47Z3gJlYDBZPIGXqYBqdhrS8USVnUyos1xhCbG1ZzrE27BDb9zbjzz1y3D4D5Dbycn62rJSRJ_zXaKYhY7vpaEhvTi97dbpQtLV7KBHa1q7mTadxKEH4tS0BCCMK9Lh9t9yYOECy62DGtIvMQ"}


        payload = {
                   "gm_keys":"8d8fhKjf5mvl4fLEwUzLA3EcHDdk6ouI31_e8HkPifIDK_6KabI-iqJxBCrAc_-OYpLpf2LPwp6a7hCXvYRtTSL3e23F-ql7Q49f-gIBwuCFHNFhRLJL4B9pI3soJlOF1Yl5KR_ZXwTWBq_KEOr18kK1RrEBfpvUHqs4yZMu54h02NT0sRweScwuAgv9CRpQsO_W3VPsvMJz2kmzKZN8iobcDvr0ONKb",
                    "gm_grade":"1",
                    "cards_id":"5"

        }
        result = requests.post( self.Url, data=payload,headers=headers)#或者直接json=payload
        result = result.json()
        print(result)


if __name__ == '__main__':
    pytest.main(['-s','Elfbar_summer_over.py'])


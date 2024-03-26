'''
@create : lisa
@file :EBST
@Date :2022/2/15
@desc :

'''

# -*- coding:UTF-8 -*-
import allure
import pytest,json
import requests
import time,gc
import hashlib
from urllib.parse import urlencode
#---------------品牌站防伪码生成接口 (任务6435)----------------------

#接口参数的 brandId 如下对应：
#elfbar => 1
#lostmary => 2
#elfliq => 3

@allure.feature("")
class Test_C:

    def setup(self):
        self.Url ="http://test-code-center.heavengifts.com/api/security-code/generate-records"
        self.HGapi = "BrandSitesSecurityCodeVerifyAPI"
        with allure.step(f"接口地址：{self.Url}"):
             print(self.Url)

    @allure.title("")
    def test_001(self):
        m = hashlib.md5()
        m.update(self.HGapi.encode("utf8"))
        HG_api_md5 = m.hexdigest()
        # 时间戳转str
        t = time.time()
        t = int(t)
        timestamp = str(t)
        print(t)
        headers = {}
        data={"brandId":2,"page":2,"limit":1}
        data_str = json.dumps(data)
        token1 = str(HG_api_md5) + timestamp + data_str
        # print(token1)
        m = hashlib.md5()
        m.update(token1.encode("utf8"))
        token = m.hexdigest()
        print(token)

        payload = {"data":data_str,
            "timestamp":timestamp,
            "token": token
        }
        result = requests.post( self.Url, data=payload,headers=headers)#或者直接json=payload
        print(result.text)


if __name__ == '__main__':
    pytest.main(['-s','Security_code_generate_records.py'])


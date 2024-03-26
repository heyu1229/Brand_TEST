'''
@create : lisa
@file :dvuv_edit_order.py
@Date :2022/6/2
@desc :

'''

import unittest
import requests,threading,time,datetime

#---------------DVUK后台创建订单并发抢库存  需要替换heards下的cookie----------------------
class Create_order():

    def __init__(self):
        self.base_url = 'https://beta-backend.deepvaping.co.uk/backend/order-create/saveCreateOrder'
    #用户已登录
    def Create_order1(self):
        payload = {"products[0][id]":"31251","products[0][price]":"10.19","products[0][type]":"normal",
                   "products[0][quantity]": "50", "products[0][promotion_id]": "0", "paymentMethod": "1",
                   "shippingMethod": "4", "orderNote": " ", "addressId": "747",
                   "taxId": " ", "memberId": "1561", "currencyId": "5",
                   "isUseBrandPoint": "0 ", "isUseNormalPoint": "0", "billAddress[first_name]": "just","billAddress[last_name]": "test",
                   "billAddress[street]": "Unit 16, The Gateway Estate, Birmingham Cargo Airport,","billAddress[city]": "Birmingham",
                   "billAddress[country]": "3285","billAddress[province]": "Birmingham","billAddress[post_code]": "B26 3QD",
                   "billAddress[phone]": "+44 7943 868422","billAddress[tax_id]": " ","billAddress[company_name]": " ",
                   }

        headers = {"Accept-Language": "zh-CN,zh;q=0.9", "Cache-Control":"no-cache", "Connection": "keep-alive", "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
                   "Cookie":"PHPSESSID=i9flb6k8i92s691u0qi5cudrpm","Origin":"https://beta-backend.deepvaping.co.uk",
                   "Pragma":"no-cache","Referer":"https://beta-backend.deepvaping.co.uk/backend/order-create",
                   "Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin",
                   "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1",
                   }
        r = requests.post(self.base_url, params=payload, headers=headers)
        result = r.json()
        print(result)

def create_order():
    create_oder = Create_order().Create_order1()


try:
    i=0
    tasts_number=10
    print("测试启动")
    while i < tasts_number:
        t = threading.Thread(target=create_order)
        t.start()
        i+=1
    print(datetime.datetime.now())
except Exception as e:
    print(e)


# if __name__ == "__main__":
#     unittest.main()
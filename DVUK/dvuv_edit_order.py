'''
@create : lisa
@file :dvuv_edit_order.py
@Date :2022/6/2
@desc :

'''

import unittest
import requests,threading,time,datetime

#---------------DVUK编辑订单  ----------------------
class Edit_order():

    def __init__(self):
        self.base_url = 'https://beta-backend.deepvaping.co.uk/backend/order-detail/editOrder'
    #用户已登录
    def Edit_order1(self):

        payload = {"remove_promotion_products":" ","product[31251_normal_0][sample_type]":" ",
                   "product[31251_normal_0][deal_price]":"10.19","product[31251_normal_0][quantity]":"300",
                   "product[31251_normal_0][id]":"31251",
                   "product[31251_normal_0][type]": "normal", "products[31251_normal_0][promotion_id]": "0",
                   "order[shipping_id]": "4",
                   "order[pay_method_id]": "1", "order[real_shipping_fee]": "0", "order[po_no]": " ",
                   "ship[ship_name]": "just test", "ship[ship_address]": "Unit 16, The Gateway Estate, Birmingham Cargo Airport,",
                   "ship[ship_city]": "Birmingham",
                   "ship[ship_zip]": "B26 3QD", "ship[ship_region_id]": "3285", "ship[ship_province]": "Birmingham",
                   "ship[ship_phone]": "+44 7943 868422","order[tax_id]": " ",
                   "order[company_name]": " ","order_id": "20221104020982"
                   }

        headers = {"Accept-Language": "zh-CN,zh;q=0.9", "Cache-Control":"no-cache", "Connection": "keep-alive", "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
                   "Cookie":"PHPSESSID=i9flb6k8i92s691u0qi5cudrpm","Origin":"https://beta-backend.deepvaping.co.uk",
                   "Pragma":"no-cache",
                   "Referer":"https://beta-backend.deepvaping.co.uk/backend/order-detail/index?id=20221104020982&tab=edit",
                   "Sec-Fetch-Mode":"cors","Sec-Fetch-Site":"same-origin",
                   "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1",
                   }
        r = requests.post(self.base_url, data=payload, headers=headers)
        result = r.json()
        print(result)

def edit_order():
    create_oder = Edit_order().Edit_order1()


try:
    i=0
    tasts_number=5
    print("测试启动")
    while i < tasts_number:
        t = threading.Thread(target=edit_order)
        t.start()
        i+=1
    print(datetime.datetime.now())
except Exception as e:
    print(e)


# if __name__ == "__main__":
#     unittest.main()
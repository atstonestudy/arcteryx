# -*- coding:UTF-8 -*-

from timeloop import Timeloop
from datetime import timedelta
import requests
from dbutil import mongoagent
import pymongo
import json
from scrapy.cmdline import execute
import time
from tool import query_tool
from tool import loghandler
from tool.conf import baseconf



tl = Timeloop()

def get_highquality_goods():
    goods = ["Beta LT Jacket - Women's-PHANTASM-XL","Beta LT Jacket - Women's-MESMER-L","Beta LT Jacket - Women's-MESMER-M"]
    return goods

def notice_items(texts):
    data2 =    {
            "msgtype": "markdown",
            "markdown": {
                "content": texts
            }
        }
    headers = {'content-type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
    r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=f8bb7488-9f79-47e7-a808-4a4c42f53ef4', json=data2, headers=headers)
    return r

# 每三分钟执行一次查库
@tl.job(interval=timedelta(minutes=baseconf["appconf"]["noticefq"]))
def sample_job_every_2s():
    # print("2s job current time")
    loghandler.logger.warning("start notice----------")

    #查找所有在售状态的物件
    # query = {"ischange": 1, "_id": {"$in": get_highquality_goods()}}
    query = query_tool.get_highquality_goods_query()
    ret = mongoagent.arcteryx_collection.find(query)
    texts = ''
    n = 0
    dollar_rate = 6.5
    for item in ret:
        if "Women" in item['title']:
            item["gender"] = "women"
        elif "Men" in item['title']:
            item["gender"] = "man"
        else:
            item["gender"] = "other"

        item["price"] = item["price"] * dollar_rate
        # notice_item = item['title'] + " " + item["gender"] + " " + item['color_name'] + " " + item['size'] + " " + str(item['price']) + "["+str(100-item['savingsPercentage']) +"]" + " " + item['status']
        head = "有更新商品:\n"
        title = "<font color='warning'>型号：</font>" + item['title']
        gender = "<font color='warning'>性别：</font>" + item['gender']
        color_name = "<font color='warning'>颜色：</font>" + item['color_name']
        size = "<font color='warning'>尺码：</font>" + item['size']
        price = "<font color='warning'>价格：</font>" + str(item['price'])
        if item['savingsPercentage']:
            sale = 100 - item['savingsPercentage']
        else:
            sale = 0
        savingsPercentage = "<font color='warning'>折扣率：</font>" + str(sale)
        status = "<font color='warning'>状态：</font>" + item['status']
        link = "<font color='warning'>链接：</font>" + item['link']
        notice_item = head + "\n" + title + '\n' + gender + '\n' + color_name + '\n' + size + '\n' + price + '\n' + savingsPercentage + '\n' + status + '\n' + link
        texts += notice_item + '\n----\n'
        n = n+1
        if n >= 5:
            ret_text = notice_items(texts)
            print(ret_text)
            n = 0
            texts = ''
            time.sleep(5)
    # print(texts)
    loghandler.logger.warning(texts)
    if not texts:
        texts = "no changed item!"
    ret_text = notice_items(texts)
    # print(ret_text)
    loghandler.logger.warning(ret_text)

    # 已通知的物件全部已通知
    mongoagent.arcteryx_collection.update_many(
        query,
        { "$set": { "ischange": 0 } },
    )

#     data2 =    {
#         "msgtype": "markdown",
#         "markdown": {
#             "content": texts
#         }
#    }

#     data3 = {
#         "msgtype": "news",
#         "news": {
#         "articles" : [
#             {
#                 "title" : "中秋节礼品领取",
#                 "description" : "今年中秋节公司有豪礼相送",
#                 "url" : "www.qq.com",
#                 "picurl" : "http://res.mail.qq.com/node/ww/wwopenmng/images/independent/doc/test_pic_msg1.png"
#             }
#             ]
#         }
#     }



    
    # r = requests.post('https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=f8bb7488-9f79-47e7-a808-4a4c42f53ef4', json=data2, headers=headers)
    # print(r.text)


# # 爬取rei平台数据
# @tl.job(interval=timedelta(minutes=30))
# def sample_job_every_180s():
#     # print("sample_job_every_30m----")
#     loghandler.logger.warning("crawl rei data--------")

#     execute(['scrapy', 'crawl', 'rei_arcteryx'])
   

tl.start(block=True)
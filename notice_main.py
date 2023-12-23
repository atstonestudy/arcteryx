# -*- coding:UTF-8 -*-

from timeloop import Timeloop
from datetime import timedelta
import requests
from dbutil.mongoagent import mongo_agent
import time
from tool import queryhandler
from tool import loghandler
from tool.conf import baseconf



tl = Timeloop()

def notice_items(goods,ischange=False):

    headers = {'content-type': 'application/json',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
    def send_msg(texts):
        data =  {
            "msgtype": "markdown",
            "markdown": {
                "content": texts
            }
        }
        boturl = ''
        if ischange:
            boturl = baseconf["bot"]["qianduoduo"]
        else:
            boturl = baseconf["bot"]["qianchaoduo"]
        r = requests.post(boturl, json=data, headers=headers)
        return r

    texts = ''
    n = 0
    count = 0
    dollar_rate = baseconf["appconf"]["dollar_rate"]
    for item in goods:
        if "Women" in item['title']:
            item["gender"] = "women"
        elif "Men" in item['title']:
            item["gender"] = "man"
        else:
            item["gender"] = "other"

        item["price"] = item["price"] * dollar_rate
        # notice_item = item['title'] + " " + item["gender"] + " " + item['color_name'] + " " + item['size'] + " " + str(item['price']) + "["+str(100-item['savingsPercentage']) +"]" + " " + item['status']
        head = ''
        if ischange:
            head = "# <font color='warning'>有更新商品:</font>\n"
        else:
            head = "# <font color='warning'>全量商品:</font>\n"
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
        link = "<font color='warning'>链接：</font>" + "["+ item['link'] + "](" + item['link'] + ")"
        notice_item = head + "\n" + title + '\n' + gender + '\n' + color_name + '\n' + size + '\n' + price + '\n' + savingsPercentage + '\n' + status + '\n' + link
        texts += notice_item + '\n----\n'
        n = n+1
        if n >= 5:
            ret_text = send_msg(texts)
            n = 0
            texts = ''
            time.sleep(5)
        count = count + 1

    if not texts:
        texts = "no changed item!"
    loghandler.logger.warning(texts)
    loghandler.logger.warning(count)
    r = send_msg(texts)
    loghandler.logger.warning(r)
    return 

# 高优商品变更通知
@tl.job(interval=timedelta(minutes=baseconf["appconf"]["changednoticefq"]))
def notice_highquality_goods_changed():
    loghandler.logger.warning("notice_highquality_goods_changed！----------")

    # 获取高优变更商品
    query = queryhandler.get_hq_query(True)
    ret = mongo_agent.find(query)
    # 通知高优变更商品
    notice_items(ret,True)

    # 已通知的物件全部已通知
    mongo_agent.update_many(
        query,
        { "$set": { "ischange": 0 } },
    )


# 高优商品全量详细数据通知
@tl.job(interval=timedelta(minutes=baseconf["appconf"]["allnoticefq"]))
def notice_highquality_goods():
    loghandler.logger.warning("notice_highquality_goods！----------")

    # 获取所有高优商品
    query = queryhandler.get_hq_query()
    loghandler.logger.warning(query)
    ret = mongo_agent.find(query)
    # loghandler.logger.warning(ret)

    # 通知高优商品
    notice_items(ret)

    # # 已通知的物件全部已通知
    # mongo_agent.update_many(
    #     query,
    #     { "$set": { "ischange": 0 } },
    # )


# tl.start(block=True)

def main():

    mongo_agent.initdb(baseconf["db"]["dbhost"],baseconf["db"]["dbport"],baseconf["db"]["dbname"],baseconf["db"]["dbusername"],baseconf["db"]["dbpawsswd"])
    tl.start(block=True)


main()
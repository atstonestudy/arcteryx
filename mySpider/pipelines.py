# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymongo
from dbutil.mongoagent import mongo_agent
from tool.conf import baseconf

mongo_agent.initdb(baseconf["db"]["dbhost"],baseconf["db"]["dbport"],baseconf["db"]["dbname"],baseconf["db"]["dbusername"],baseconf["db"]["dbpawsswd"])

class MyspiderPipeline:
    def process_item(self, item, spider):
        if spider.name == 'gaoqing888':
            print("item", item)

            client = pymongo.MongoClient("10.0.1.30", 27017)
            db = client['test-db']
            collection = db['testitem']

            dbitem = {
                "title": item['name'],
                "info": item['info'],
                "score":item['score'],
                "desc": item['desc'],
                "url": item['url'],
                "id":item['serial'],
                "image_url":item['image_url']
            }
            x = collection.insert_one(dbitem)
            print(x.inserted_id)
        elif spider.name == 'rei_arcteryx':
            id = item['title'] + "-" + item['color_name'] + "-" + item['size']
            # dbitem = {
            #     "title": item['title'],
            #     "color": item['color'],
            #     "color_name":item['color_name'],
            #     "size": item['size'],
            #     "price": item['price'],
            #     "raw_price":item['raw_price'],
            #     "savingsPercentage":item['savingsPercentage'],
            #     "status":item['status'],
            # }
            # x = collection.insert_one(dbitem)

           
            # ret = collection.find_one({'_id': id})
            ret = mongo_agent.find_one({'_id': id})
            print("start item db op----------------------------------")
            print(id)

            gender = ''
            if "Women" in item['title']:
                gender = "woman"
            elif "Men" in item['title']:
                gender = "man"
            else:
                gender = "other"

            if ret and item['price']==ret["price"] and item['raw_price']==ret["raw_price"] and item['savingsPercentage']==ret["savingsPercentage"] and item['status']==ret["status"]:
                print("=================no changed============")
                return
            else:
                print("====================changed============")
                dbitem = {
                    "title": item['title'],
                    "color": item['color'],
                    "color_name":item['color_name'],
                    "size": item['size'],
                    "price": item['price'],
                    "raw_price":item['raw_price'],
                    "savingsPercentage":item['savingsPercentage'],
                    "status":item['status'],
                    "ischange":1,
                    "link":item['link'],
                    "gender": gender
                }
          
                # collection.update_one(
                #     {'_id': id},
                #     {'$set': dbitem},
                #     upsert=True
                # )
                mongo_agent.update_one(
                     {'_id': id},
                     {'$set': dbitem},
                     upsert=True
                )
          





        

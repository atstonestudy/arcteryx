import pymongo
from tool.conf import baseconf


# connstr = "mongodb://%s:%s@%s:%s/%s" % (baseconf["db"]["dbusername"],baseconf["db"]["dbpawsswd"],baseconf["db"]["dbhost"],baseconf["db"]["dbport"],baseconf["db"]["dbname"])
# # mongodb://arcteryx-hecter:123456@121.37.187.103:27017/arcteryx
# client = pymongo.MongoClient(connstr)
# arcteryx_db = client["arcteryx"]
# arcteryx_collection = arcteryx_db["arcteryx"]

class MongoAgent:

    def initdb(self,host,port,dbname,username,userpasswd):
        self.dbname = dbname
        self.collection = "arcteryx"
        connstr = "mongodb://%s:%s@%s:%s/%s" % (username,userpasswd,host,port,dbname)
        self.client = pymongo.MongoClient(connstr)
    
    def find(self,query):
        return self.client[self.dbname][self.collection].find(query)

    def count(self,query):
        return self.client[self.dbname][self.collection].count_documents(query)

    def find_one(self,query):
        return self.client[self.dbname][self.collection].find_one(query)

    def update_many(self,query,updatedict):
        return self.client[self.dbname][self.collection].update_many(query,updatedict)
    
    def update_one(self,query,updatedict,upsert):
        return self.client[self.dbname][self.collection].update_one(query,updatedict,upsert=upsert)


mongo_agent = MongoAgent()
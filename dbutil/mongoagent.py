import pymongo
from tool.conf import baseconf


connstr = "mongodb://%s:%s@%s:%s/%s" % (baseconf["db"]["dbusername"],baseconf["db"]["dbpawsswd"],baseconf["db"]["dbhost"],baseconf["db"]["dbport"],baseconf["db"]["dbname"])
# mongodb://arcteryx-hecter:123456@121.37.187.103:27017/arcteryx
client = pymongo.MongoClient(connstr)
arcteryx_db = client["arcteryx"]
arcteryx_collection = arcteryx_db["arcteryx"]
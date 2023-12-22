from tool import query_tool
from tool import loghandler
from tool.conf import baseconf

aa = query_tool.get_highquality_goods_query()
# loghandler.logger.error(aa)
connstr = "'mongodb://%s:%s@%s:%s/%s'" % (baseconf["db"]["dbusername"],baseconf["db"]["dbpawsswd"],baseconf["db"]["dbhost"],baseconf["db"]["dbport"],baseconf["db"]["dbname"])

print(connstr)
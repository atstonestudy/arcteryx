from tool import queryhandler
from tool import loghandler
from tool.conf import baseconf
from dbutil.mongoagent import mongo_agent
from tool import conf


print(conf.get_item_conf("Cerium Down Jacket - Men's"))

# aa = queryhandler.get_highquality_goods_query()
# # loghandler.logger.error(aa)
# connstr = "'mongodb://%s:%s@%s:%s/%s'" % (baseconf["db"]["dbusername"],baseconf["db"]["dbpawsswd"],baseconf["db"]["dbhost"],baseconf["db"]["dbport"],baseconf["db"]["dbname"])

# # print(connstr)
# mongo_agent.initdb(baseconf["db"]["dbhost"],baseconf["db"]["dbport"],baseconf["db"]["dbname"],baseconf["db"]["dbusername"],baseconf["db"]["dbpawsswd"])

 
# value1 = '^%s$' % 'Black Sapphire' #匹配data开头结尾
# re_value1 = re.compile(value1, re.IGNORECASE) #IGNORECASE 正则匹配忽略大小写

# value2 = '^%s$' % 'Black' #匹配data开头结尾
# re_value2 = re.compile(value2, re.IGNORECASE) #IGNORECASE 正则匹配忽略大小写

# value3 = '^%s$' % 'Habitat' #匹配data开头结尾
# re_value3 = re.compile(value3, re.IGNORECASE) #IGNORECASE 正则匹配忽略大小写

# value4 = '^%s$' % 'oracle' #匹配data开头结尾
# re_value4 = re.compile(value4, re.IGNORECASE) #IGNORECASE 正则匹配忽略大小写


# query = {
#         'size': {
#             '$in': ['M', 'L', 'XL']
#         },
#         'color_name': {
#             '$in': [re_value1, re_value2, re_value3, re_value4]
#         },
#         '$and': [{
#                 'title': {
#                     '$regex': 'Cerium',
#                     '$options': 'i'
#                 }
#             },
#             {
#                 'title': {
#                     '$regex': 'Jacket',
#                     '$options': 'i'
#                 }
#             }
#         ],
#         'gender': 'man',
#         'status': 'AVAILABLE'
#     }   
# ret = mongo_agent.count(query)
# print(ret)
# print(queryhandler.get_hq_query())
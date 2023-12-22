from tool import conf
from tool import loghandler

def get_highquality_goods_query():
    querys = []
    for index, row in conf.data.iterrows():
        # row是一个pandas的Series对象，表示csv文件的一行数据
        # print(row)
        if row["REI命名"]  == 6666 :
            # print("===============")
            continue

        sizelist,colorlist = [],[]
        if row["size"] != 6666:
            sizelist = sizelist + row["size"].split("/")
        if row["color_name"] != 6666:
            colorlist = colorlist + row["color_name"].split("/")
        if sizelist and colorlist:
            query = {"ischange": 1, "title": row["REI命名"],"size":{"$in": sizelist},"color_name":{"$in": colorlist}}
        elif sizelist and (not colorlist):
            query = {"ischange": 1, "title": row["REI命名"],"size":{"$in": sizelist}}
        elif (not sizelist) and colorlist:
            query = {"ischange": 1, "title": row["REI命名"],"color_name":{"$in": colorlist}}
        else:
            query = {"ischange": 1, "title": row["REI命名"]}
        
        querys.append(query)
    query = {"$or":querys}
    return query


if __name__ == '__main__':
    aa = get_highquality_goods_query()
    loghandler.logger.error('aa')
    # print(aa)
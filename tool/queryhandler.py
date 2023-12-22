from tool import conf
from tool import loghandler

def get_hq_query(ischange=False):
    querys = []
    for index, row in conf.data.iterrows():
        if row["REI命名"]  == 6666 :
            continue
        sizelist,colorlist = [],[]
        if row["size"] != 6666:
            sizelist = sizelist + row["size"].split("/")
        if row["color_name"] != 6666:
            colorlist = colorlist + row["color_name"].split("/")
        if sizelist and colorlist:
            if ischange:
                query = {"ischange": 1, "title": row["REI命名"],"size":{"$in": sizelist},"color_name":{"$in": colorlist}}
            else:
                query = {"title": row["REI命名"],"size":{"$in": sizelist},"color_name":{"$in": colorlist}}
        elif sizelist and (not colorlist):
            if ischange:
                query = {"ischange": 1, "title": row["REI命名"],"size":{"$in": sizelist}}
            else:
                query = {"title": row["REI命名"],"size":{"$in": sizelist}}
        elif (not sizelist) and colorlist:
            if ischange:
                query = {"ischange": 1, "title": row["REI命名"],"color_name":{"$in": colorlist}}
            else:
                query = {"title": row["REI命名"],"color_name":{"$in": colorlist}}
        else:
            if ischange:
                query = {"ischange": 1, "title": row["REI命名"]}
            else:
                query = {"title": row["REI命名"]}
        
        querys.append(query)
    query = {"$or":querys}
    return query


if __name__ == '__main__':
    aa = get_hq_query(True)
    loghandler.logger.error('aa')
    # print(aa)
    
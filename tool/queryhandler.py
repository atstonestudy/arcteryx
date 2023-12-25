from tool import conf
from tool import loghandler

def get_hq_query(ischange=False):
    querys = []
    for index, row in conf.data.iterrows():
        if row["title_keywords"]  == 6666 :
            continue
        sizelist,colorlist,titlekeywordslist = [],[],[]
        gender = ''
        if row["size"] != 6666:
            sizelist = sizelist + row["size"].split("/")
        if row["color_name"] != 6666:
            colorlist = colorlist + row["color_name"].split("/")
        if row["gender"] != 6666:
            gender =  row["gender"]
        titlekeywordslist = row["title_keywords"].split("/")
        if sizelist and colorlist:
            if ischange:
                query = {"ischange": 1,  "size":{"$in": sizelist},"color_name":{"$in": colorlist}}
            else:
                query = { "size":{"$in": sizelist},"color_name":{"$in": colorlist}}
                # query = {"title": {"$regex":row["REI命名"]},"$option":"i","size":{"$in": sizelist},"color_name":{"$in": colorlist}}

        elif sizelist and (not colorlist):
            if ischange:
                query = {"ischange": 1,  "size":{"$in": sizelist}}
            else:
                query = { "size":{"$in": sizelist}}
        elif (not sizelist) and colorlist:
            if ischange:
                query = {"ischange": 1,  "color_name":{"$in": colorlist}}
            else:
                query = { "color_name":{"$in": colorlist}}
        else:
            if ischange:
                query = {"ischange": 1}
        titlelist = []
        for keyword in titlekeywordslist:
            aa = {"title": {"$regex":keyword,"$options":"i"}}
            titlelist.append(aa)
        titlequery = {
            "$and":titlelist
        }
        query.update(titlequery)

        # 需要做性别过滤
        if gender:
            query.update({"gender":gender})

        # 需要做商品状态过滤
        if not ischange:
            query.update({"status":"AVAILABLE"})

        querys.append(query)
    query = {"$or":querys}
    return query


if __name__ == '__main__':
    aa = get_hq_query(True)
    loghandler.logger.error('aa')
    # print(aa)
    
import pandas as pd
import json

data = pd.read_csv('./conf/highquality_goods.csv', usecols=["title_keywords", "size","color_name","gender","dewu_price"])
# print(data)
data=data.fillna(6666)

with open('./conf/baseconf.json', 'r') as basejson:
    baseconf = json.load(basejson)


def get_item_conf(title):
    row_index = -1
    for index, row in data.iterrows():
        if row["title_keywords"]  == 6666 :
            continue
        titlekeywordslist = row["title_keywords"].split("/")
        flag = 1
        for title_key in titlekeywordslist:
            if title_key.lower() not in title.lower():
                flag = 0
                break
        if flag:
            row_index = index
    if row_index != -1:
        return data[row_index:row_index+1]
    final_df=pd.DataFrame() #create an empty dataframe
    return final_df
    
    

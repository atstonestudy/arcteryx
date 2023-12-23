import pandas as pd
import json

data = pd.read_csv('./conf/highquality_goods.csv', usecols=["title_keywords", "size","color_name"])
# print(data)
data=data.fillna(6666)

with open('./conf/baseconf.json', 'r') as basejson:
    baseconf = json.load(basejson)

    
    

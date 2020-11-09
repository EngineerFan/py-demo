# -*- coding: utf-8 -*-
# @Author      : Ryan
# @Time        : 2020/9/28 20:31
# @Software    : PyCharm
# @Description :

import pymongo

client = pymongo.MongoClient(host='192.168.79.103', port=27017)
db = client['test']
collection = db['test']

for x in collection.find():
    print(x)

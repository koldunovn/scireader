import pymongo
from pymongo import MongoClient
import json
from bson import json_util
import os
import re
from datetime import datetime, timedelta

def find_terms(terms):
    client = MongoClient()
    db = client.journals
    posts = db.posts
    
    tdel = timedelta(70)
    now = datetime.now()
    d = now-tdel

    print(terms)

    json_docs = []
    vv = posts.find({'$text': {'$search': terms }, "time": {"$gt": d}}).sort("time",pymongo.DESCENDING)
    for doc in vv:
        delt = datetime.now() - doc['time']
        doc['delta']=delt.days
        doc['time']=doc['time'].strftime("%Y-%m-%d")
        json_doc = doc
        json_docs.append(json_doc)

    return json_docs

    client.close()
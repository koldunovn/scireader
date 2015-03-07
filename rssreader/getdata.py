
# coding: utf-8

import feedparser as fp
from time import mktime
from datetime import datetime
import pymongo
from pymongo import MongoClient
import json
from bson import json_util
import os
import re

client = MongoClient()
db = client.journals
posts = db.posts
#posts.drop_indexes()


def add_journal(rss, journal):
    '''
    INPUT:
        rss - rss feed
        journal - name of the journal
    '''
    print(journal)

    a = fp.parse(rss)
    for m in  a['entries']:
        if m.has_key('summary'):
            have_abstract=True
            abstr = m['summary']
            abstr = abstr.replace("\n", " ")
            abstr = re.sub('<[^>]*>', ' ',abstr)
        
        const_dict ={'href':m['links'][0]['href'], 
                     'title':m['title'],
                     'source':journal,
                     'time':datetime.fromtimestamp(mktime(m['updated_parsed']))}
        
        if have_abstract:
            const_dict['abstract']= abstr
            
    
        ttitle = const_dict['title']
        print(ttitle)
        #print const_dict
        #check if we have already a record with this title
        bb = posts.find({'title':ttitle})
        if bb.count() == 0:
            #if not, just add new post
            #print('add new post')
            posts.insert(const_dict)
        else:
            #print('skip')
            pass


def find_terms(terms,outfile):
    
    json_docs = []
    vv = posts.find({'$text': {'$search': terms }}).sort("time",pymongo.DESCENDING)
    for doc in vv:
        delt = datetime.now() - doc['time']
        doc['delta']=delt.days
        doc['time']=doc['time'].strftime("%Y-%m-%d")
        json_doc = doc
        json_docs.append(json_doc)

    ofile = open(outfile,'w')
    out = json.dumps(json_docs, default=json_util.default)
    ofile.write(out)
    ofile.close()

    os.system('cp '+outfile+' ../FlaskApp/static/')


jfile = open('../FlaskApp/static/journal_list.json')
jnl_list = json.load(jfile)

for jrnl in jnl_list:
    add_journal(jrnl['rss'], jrnl['name'])

db.posts.ensure_index([('abstract', 'text'),('title', 'text')])


find_terms("\"sea ice\"",'sea_ice.json')
find_terms("\"arctic ocean\"",'arctic_ocean.json')
find_terms("glacier",'glacier.json')
find_terms("\"sea level\"",'sea_level.json')

client.close()


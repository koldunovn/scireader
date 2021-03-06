
# coding: utf-8

import feedparser as fp
from time import mktime
from datetime import datetime, timedelta
import pymongo
from pymongo import MongoClient
import json
from bson import json_util
import os
import re
import logging

logging.basicConfig(filename='getdata.log',level=logging.DEBUG, format='%(asctime)s %(message)s')
logging.getLogger().addHandler(logging.StreamHandler())

logging.info('Begin database update')

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
    logging.info(journal)

    a = fp.parse(rss)
    logging.info(str(len(a['entries']))+" entries retrieved")

    added_new = 0
    skipped   = 0

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
        #print(ttitle)
        #print const_dict
        #check if we have already a record with this title
        bb = posts.find({'title':ttitle})
        if bb.count() == 0:
            #if not, just add new post
            #print('add new post')
            posts.insert(const_dict)
            added_new = added_new+1
        else:
            #print('skip')
            skipped = skipped+1
            pass
    logging.info('added '+str(added_new)+' records')
    logging.info('skipped '+str(skipped)+' records\n')


def find_terms(terms,outfile):
    
    tdel = timedelta(70)
    now = datetime.now()
    d = now-tdel

    json_docs = []
    vv = posts.find({'$text': {'$search': terms }, "time": {"$gt": d}}).sort("time",pymongo.DESCENDING)
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

kfile = open('../FlaskApp/static/keyword_list.json')
kwrd_list = json.load(kfile)

for keyword in kwrd_list:
    find_terms(keyword['keyword'],keyword['output_file'])


client.close()


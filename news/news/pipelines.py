#-*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
import sys 
sys.path.insert(0, "..")

import database
import re

BaseUrl="http://news.hitwh.edu.cn/"
class NewsPipeline(object):
    #sql=database.CMySQL('localhost','root','','news')
    sql=''
    i=1
    #poster=poster.Poster()
    def __init__(self):
        self.sql=database.CMySQL('localhost','root','','news')
        self.sql.link()
    def process_item(self, item, spider):       
        values=[] 
        strtime=str((item['addtime'][0]).encode('UTF-8'))[1:]
        strtime=re.sub(r'年','.',strtime)
        strtime=re.sub(r'月','.',strtime)
        strtime=re.sub(r'日.*','',strtime)
        strid=str((item['link'][0]).encode('UTF-8'))
        strid=re.sub(r'.*\?id=','',strid)
        print item['link'][0].encode('UTF-8'),strid
        values.append((strid,item['school'],item['title'][0].encode('UTF-8'),BaseUrl+item['link'][0].encode('UTF-8'),strtime))
        #self.sql.sql_insert('newstb',values)
        #message="%s %s %s %s " %(item['school'],strtime,item['title'][0],BaseUrl+item['link'][0]) 
        print strid,item['school'],item['title'][0].encode('UTF-8'),BaseUrl+item['link'][0].encode('UTF-8'),strtime
        #print values
        try:
            #print message
            #self.sql.sql_insert('newstb',values)
            #self.post_status()
            pass
        except:
            print 'Error1'
        
        return item


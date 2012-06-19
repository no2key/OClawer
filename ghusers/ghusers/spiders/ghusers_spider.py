#-*- coding=utf-8 -*-
from scrapy.selector import HtmlXPathSelector
from ghusers.items import GhusersItem
from scrapy.spider import BaseSpider
import re
from pymysql import PyMysql
from config import HOST,USER,PASSWD,DATABASE
class ghusersSpider(BaseSpider):
    name='ghusers'#110460
    allowed_domains=['']
    start_urls=['http://bbs.ghtt.net/space-uid-'+str(x)+'.html' for x in range(1,110460)]
    db=PyMysql(HOST,USER,PASSWD,DATABASE)
    #def __init__(self):
        
    def insertdb(self,item):
        strsql="insert into users(prestige,usergroup,name,regtime,sex,topic,score,useronline,reply,coin,friends,id) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %tuple(item.values())
        self.db.update(strsql)
    def getstr(self,rawstr):
        '''得到我们想要字符串
        Keyword argument：
        rawstr 未处理的原始字符串
        Returns: string 返回处理后的字符串
        '''
        rawstr=rawstr.strip()
        liststr=re.findall(r'\d+', rawstr)
        if len(liststr)>0:
            if len(liststr)>1:
                return rawstr  
            else:
                return liststr[0]
        else:
            return rawstr    
                
        #if op=='friends':
        #    rawstr=re.sub('.* ','',rawstr)
        #    return rawstr
                        
            
    def parse(self,response):
        hxs=HtmlXPathSelector(response)
        sites=hxs.select('//div[@class="bm_c"]')
        items=[]
        for site in sites:
            item=GhusersItem()
            item['id']=(site.select('div[@class="pbm mbm bbda cl"]/h2[@class="mbn"]/span/text()').extract())[0]         
            item['name']=(site.select('div[@class="pbm mbm bbda cl"]/h2[@class="mbn"]/text()').extract())[0]         
            item['sex']=(site.select('div[@class="pbm mbm bbda cl"]/ul[2]/li/text()').extract())[0]   
            item['friends']=(site.select('div[@class="pbm mbm bbda cl"]/ul[@class="cl bbda pbm mbm"]/li/a/text()').extract())[0]
            item['reply']=(site.select('div[@class="pbm mbm bbda cl"]/ul[@class="cl bbda pbm mbm"]/li/a/text()').extract())[1]
            item['topic']=(site.select('div[@class="pbm mbm bbda cl"]/ul[@class="cl bbda pbm mbm"]/li/a/text()').extract())[2]
            try:
                item['group']=(site.select('div[@class="pbm mbm bbda cl"]/ul/li/span/a/text()').extract())[0]
            except:
                try:
                    item['group']=(site.select('div[@class="pbm mbm bbda cl"]/ul/li[2]/span/a/text()').extract())[0]                
                except:
                    item['group']=(site.select('div[@class="pbm mbm bbda cl"]/ul/li/span/a/font/text()').extract())[0]       
            item['online']=(site.select('div[@class="pbm mbm bbda cl"]/ul[@id="pbbs"]/li[1]/text()').extract())[0]  
            item['regtime']=(site.select('div[@class="pbm mbm bbda cl"]/ul[@id="pbbs"]/li[2]/text()').extract())[0]
            item['score']=(site.select('div[@class="cl"]/ul/li/text()').extract())[0]
            item['coin']=(site.select('div[@class="cl"]/ul/li/text()').extract())[1]
            item['prestige']=(site.select('div[@class="cl"]/ul/li/text()').extract())[2]
            
            for key,value in item.items():
                item[key]=self.getstr(value)
            
            for key,value in item.items():
                print key,value           
            self.insertdb(item)
            #raw_input('pause')
        return 

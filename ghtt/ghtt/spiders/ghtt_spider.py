#-*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from ghtt.items import GhttItem
from scrapy.http import Request
from time import sleep
BaseUrl='http://bbs.ghtt.net/'
class ghttSpider(BaseSpider):
    name="ghtt"
    allowed_domains=["bbs.ghtt.net"]
    start_urls=['http://bbs.ghtt.net/forum.php']
    module_urls=[]
    def claw_module_name(self,hxs):#爬取各个模块的名字
        sites=hxs.select('//tr/td/h2')
        items=[]
        for site in sites:
            item=GhttItem()
            item['title']=site.select('a/text()').extract()[0]#版块名
            item['link'] = site.select('a/@href').extract()[0]#版块链接         
            self.module_urls.append(item['link'])
            try:                
                print item['title'] ,item['link']
                items.append(item) 
                    
            except:
                print 'Error:list out of range'
        print 'The number of module name is :\t',len(items)    
    
    def claw_title_name(self,hxs):#爬取各个标题的名字
        sites=hxs.select('//table/tbody/tr')
        for site in sites:
            item=GhttItem()
            item['title']=site.select('th/a/text()').extract()#标题名
            item['link'] = site.select('th/a/@href').extract()
            item['reply']=site.select('td/a/text()').extract()#回复数
            item['check']=site.select('td/em/text()').extract()#查看数
            item['addtime']=site.select('td/em/span/text()').extract()#帖子发布日期          
            try:
                print item['title'][0],item['addtime'][0],item['check'][0],item['reply'][1]
                print item['link'][0]
            except:
                print 'Error:list out of range'

            #items.append(item)    
    def parse(self, response):
        sleep(5)#15秒爬一次,防止访问过快。
        hxs=HtmlXPathSelector(response)
        title=hxs.select('//title/text()').extract()[0]
        print title        
        if (title==u'哈尔滨工业大学威海校区-观海听涛 - 哈尔滨工业大学'):#如果当前是首页(各个模块的汇总页http://bbs.ghtt.net/forum.php)            
            
            self.claw_module_name(hxs)
            url=BaseUrl+self.module_urls[0]
            self.module_urls.pop(0)
            print '下一个模块地址: ',url
            return Request(url)
        else:#当前为版块的页面，则开始爬取每个帖子的标题
            sites=hxs.select('//div/a[@class="nxt"]')#获取下一页的链接
            try:
                url=sites[0].select('@href').extract()[0]#每页中有两个重复的下一页链接，选取第一个        
                url=BaseUrl+url
                print url
                self.claw_title_name(hxs)
                return  Request(url)
            except:
                self.claw_title_name(hxs)
                print '本版块已经扫描完毕'
                url=BaseUrl+self.module_urls[0]
                print url
                #sleep(10)
                self.module_urls.pop(0)
                return Request(url)

        

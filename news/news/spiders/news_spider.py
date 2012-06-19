#-*- coding: utf-8 -*-
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from news.items import NewsItem
from scrapy.http import Request
from time import sleep



class NewsSpider(BaseSpider):
    name="news"
    allowed_domains=["hitwh.edu.cn"]
    start_urls=['http://news.hitwh.edu.cn/news_more_list.asp?id=1']
    def parse(self,response):
        hxs=HtmlXPathSelector(response)
        sites=hxs.select('//div[@class="right"]/div/div/ul/li')
        items=[]
        for site in sites:
            item= NewsItem()
            
            
            item['addtime']=site.select('span/text()').extract()
            item['link'] = site.select('a/@href').extract()
            item['title']=site.select('a/text()').extract()
            item['school']='HIT'
            items.append(item)
            
        return items

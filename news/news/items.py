# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html
#-*- coding: utf-8 -*-
from scrapy.item import Item, Field

class NewsItem(Item):
    title=Field()
    link=Field()
    addtime=Field()
    school=Field()

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class GhttItem(Item):
    title=Field()
    link=Field()
    addtime=Field()
    reply=Field()
    check=Field()
    nextclaw=Field()

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class GhusersItem(Item):
    # define the fields for your item here like:
    # name = Field()
    id=Field()
    name=Field()
    sex=Field()
    group=Field()
    
    friends=Field()
    reply=Field()
    topic=Field()
    
    score=Field()
    coin=Field()
    prestige=Field()
    
    online=Field()
    regtime=Field()
    

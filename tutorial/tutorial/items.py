# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html


from scrapy.item import Item, Field

class DmozItem(Item):
    # defining attributes of DmozItem class as srapy.item.Field objects
    title = Field()
    link = Field()
    desc = Field()



# from scrapy.item import Item, Field

# class Item(Item):
#     # define the fields for your item here like:
#     # name = Field()
#     pass

# class DmozItem(Item):
#     title = Field()
#     link = Field()
#     desc = Field()

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item

class CostcoOnlineItem(Item):
    """コストコオンラインアイテム

    コストコオンラインショップの商品データ

    Args:
        Item (Item): Item基本データ
    """
    category = Field()
    child_category = Field()
    count = Field()
    pass

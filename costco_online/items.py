# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item

class CostcoOnlineItem(Item):
    """コストコオンラインアイテム

    商品一覧ページの総数の商品データ

    Args:
        Item (Item): Item基本データ
    """
    category = Field()
    child_category = Field()
    count = Field()
    pass

class CostcoProductItem(Item):
    """コストコオンライン商品詳細

    コストコオンラインショップの商品詳細データ

    Args:
        Item (Item): Item基本データ
    """
    Item_Number = Field()
    category = Field()
    sub_category = Field()
    title = Field()
    price = Field()
    description = Field()
    url = Field()
    img = Field()
    pass

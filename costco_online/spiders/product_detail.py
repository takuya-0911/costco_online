import scrapy
from costco_online.enums.categories import Categories, Sub_Categories
from costco_online.items import CostcoProductItem

class ProductDetailSpider(scrapy.Spider):
    name = 'product_detail'
    allowed_domains = ['www.costco.co.jp']
    start_urls = ['https://www.costco.co.jp/Tires-Automotive/c/cos_9']

    def parse(self, response):
        """カテゴリー別ページ解析処理

        カテゴリー別ページを解析する

        Args:
            response (Response): responseオブジェクト

        Yields:
            Response: 商品一覧ページ解析処理
        """
        # 子カテゴリー一覧取得（全ての...含む）
        child_categoryList = response.xpath('//div[@class="category-node ng-star-inserted"]')

        for child_category in child_categoryList:
            # 次ページ取得し、存在する場合商品一覧ページ解析
            next_page = child_category.xpath('.//a/@href').get()
            if next_page:
                # タイヤ検索ページと全商品ページは除去
                if 'Online-Tires' not in next_page and 'All-' not in next_page:
                    yield scrapy.Request(url=next_page, callback=self.parse_productsList)

    def parse_productsList(self, response):
        """商品一覧ページ解析処理

        商品一覧ページの総数を取得

        Args:
            response (Response): Responseオブジェクト

        Yields:
            CostcoProductItem: 商品個別ページ解析処理
        """
        # 商品アイテム生成
        productItem = CostcoProductItem()

        # urlからカテゴリー、子カテゴリー取得
        url = response.url
        urlAfter = url[len('https://www.costco.co.jp')+1:]
        urlCategory = urlAfter[:urlAfter.find('/')]
        urlSubCategory = urlAfter[len(urlCategory)+1:urlAfter.find('/', len(urlCategory)+1)]

        # カテゴリ分別
        categoryNm = urlAfter[:urlAfter.find('/')]
        sub_categoryNm = urlSubCategory if urlSubCategory != 'c' else ""
        categoryId = ""
        sub_categoryId = ""
        # EnumからId取得
        for category in Categories:
            if (categoryNm == category.value.name):
                categoryId = category.value.id
        # EnumからId取得
        for sub_category in Sub_Categories:
            if (sub_categoryNm == sub_category.value.name):
                sub_categoryId = sub_category.value.id

        productItem['category'] = categoryId
        productItem['sub_category'] = sub_categoryId

        # 商品一覧取得
        productsList = response.xpath('//a[@class="thumb"]/@href')

        for product in productsList:
            next_page = product.get()
            yield scrapy.Request(url=next_page, callback=self.parse_product, meta = {'productItem': productItem})
            
    def parse_product(self, response):
        """商品個別ページ解析処理

        商品個別ページを解析

        Args:
            response (Response): Responseオブジェクト

        Yields:
            CostcoProductItem: 商品データ
        """

        # 価格変換
        price = response.xpath('//span[@class="notranslate ng-star-inserted"]/text()').get()
        if (price) :
            price = price.replace('¥','').replace(',','')

        # 商品データ設定
        productItem = CostcoProductItem()
        productItem = response.meta['productItem']
        productItem['Item_Number'] = response.xpath('//span[@class="notranslate"]/text()').get()
        productItem['title'] = response.xpath('//h1/text()').get()
        productItem['price'] = price
        productItem['description'] = response.xpath('//div[@class="pdp-tab-content-body product-details-content-wrapper"]/p/text()').get()
        productItem['url'] = response.url
        productItem['img'] = 'https://www.costco.co.jp' + response.xpath('//div[@class="primary-image-wrapper"]//img/@src').get()
        
        yield productItem
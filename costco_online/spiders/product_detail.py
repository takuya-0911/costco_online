import scrapy
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
                # タイヤ検索ページは除去
                if 'Online-Tires' not in next_page:
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
        yield {'url': url, 'urlAfter':urlAfter,'urlCategory':urlCategory,'urlSubCategory':urlSubCategory}
        productItem['category'] = urlAfter[:urlAfter.find('/')]
        productItem['sub_category'] = urlSubCategory if urlSubCategory != 'c' else ""

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
        productItem = CostcoProductItem()
        productItem = response.meta['productItem']
        productItem['Item_Number'] = response.xpath('//span[@class="notranslate"]/text()').get()
        productItem['title'] = response.xpath('//h1/text()').get()
        productItem['price'] = response.xpath('//span[@class="notranslate ng-star-inserted"]/text()').get()
        productItem['description'] = response.xpath('//div[@class="pdp-tab-content-body product-details-content-wrapper"]/p/text()').get()
        productItem['url'] = response.url
        productItem['img'] = 'https://www.costco.co.jp' + response.xpath('//div[@class="primary-image-wrapper"]//img/@src').get()
        
        yield productItem
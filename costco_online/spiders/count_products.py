import scrapy
from costco_online.items import CostcoOnlineItem

class CountProductsSpider(scrapy.Spider):
    name = 'count_products'
    allowed_domains = ['www.costco.co.jp']
    start_urls = ['https://www.costco.co.jp']

    def parse(self, response):
        """トップの解析処理

        トップのカテゴリー一覧を解析する

        Args:
            response (Response): responseオブジェクト

        Yields:
            Response: カテゴリー別ページ解析処理
        """
        # カテゴリー一覧取得
        categoryList = response.xpath('//div[@class="contMain"]//div[@class="col-xs-4 col-md-2"]')

        for category in categoryList:
            # 次ページ取得し、存在する場合カテゴリー別or商品一覧ページ解析
            next_page = CountProductsSpider.start_urls[0] + category.xpath('.//a/@href').get()
            if next_page:
                # Dropship-Frozen-Chilled-ItemsとFloralは子カテゴリー無しの為、除外
                if '/c/cos_13.16' not in next_page and '/c/cos_10.8' not in next_page and '/c/cos' in next_page:
                    # 子カテゴリーが存在する場合
                    yield scrapy.Request(url=next_page, callback=self.parse_child)
                else:
                    # 子カテゴリーが存在しない場合
                    yield scrapy.Request(url=next_page, callback=self.parse_productsList)

    def parse_child(self, response):
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
            CostcoOnlineItem: コストコオンラインデータ
        """
        # 商品アイテム生成
        resultItem = CostcoOnlineItem()
        # urlからカテゴリー、子カテゴリー取得
        url = response.url
        urlAfter = url[len(CountProductsSpider.start_urls[0])+1:]
        urlCategory = urlAfter[:urlAfter.find('/')]
        urlChildCategory = urlAfter[len(urlCategory)+1:urlAfter.find('/', len(urlCategory)+1)]
        resultItem['category'] = urlAfter[:urlAfter.find('/')]
        resultItem['child_category'] = urlChildCategory if urlChildCategory != 'c' else ""

        # ** - ** of ** から総数取得
        resultStr = response.xpath('//div[@class="search-pagination-container"]/span/text()').get()
        resultItem['count'] = resultStr[resultStr.find('of') + 3:]
        yield resultItem


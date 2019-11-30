import scrapy

from TaobaoInsurance.items import ProductInfoItem

class productListSpider(scrapy.Spider):

    name = 'productList'
    
    start_urls = ['https://baoxian.taobao.com/nv/itemSearch.html']
    
    def parse(self, response):
        
        product_data = response.css('div.insurance-listblock')
        
        product_item = ProductInfoItem()
        
        for each_product in product_data:

            product_item['is_product'] = 1
            product_item['product_name'] = each_product.css('span.li-title-t::text').get()
            product_item['product_url'] = 'https://baoxian.taobao.com' + each_product.css('div.li-title a::attr(href)').get()
            product_item['_id'] = each_product.css('div.li-title a::attr(href)').get()[each_product.css('div.li-title a::attr(href)').get().rfind('=') + 1 :]
            product_item['seller_id'] = each_product.css('span.li-title-ww a::attr(href)').get()[each_product.css('span.li-title-ww a::attr(href)').get().rfind('=') + 1 :]

            yield product_item
        
        next_page = response.css('a.next::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)
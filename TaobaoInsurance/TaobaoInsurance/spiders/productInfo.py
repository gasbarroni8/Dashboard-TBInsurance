import scrapy, pymongo, json

from TaobaoInsurance.items import ProductItem

class productInfoSpider(scrapy.Spider):

    name = 'productInfo'
    
    
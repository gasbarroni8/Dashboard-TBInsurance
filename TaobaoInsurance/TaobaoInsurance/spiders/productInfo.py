import scrapy, pymongo, json

from TaobaoInsurance.items import ProductInfoItem
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

'''服务器信息'''

zd_host = settings['MONGODB_HOST']
zd_port = settings['MONGODB_PORT']
zd_client = pymongo.MongoClient(host=zd_host, port=zd_port)
zd_db= zd_client['TaobaoInsurance']

class productInfoSpider(scrapy.Spider):

    name = 'productInfo'
    
    start_urls = []
    
    doc_product = zd_db['product_info']
    doc_data = doc_product.find()
    
    for each_product in doc_data:

        json_url = 'https://baoxian.taobao.com/json/item/info.do?item_id=' + each_product['_id']       
        start_urls.append(json_url)
    
    def parse(self, response):
        
        
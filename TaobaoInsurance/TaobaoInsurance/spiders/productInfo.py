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

    '''正式用例'''
    
    # start_urls = []
    
    # doc_product = zd_db['product_info']
    # doc_data = doc_product.find()
    
    # for each_product in doc_data:

    #     json_url = 'https://baoxian.taobao.com/json/item/info.do?item_id=' + each_product['_id']       
    #     start_urls.append(json_url)
    
    '''调试用例'''

    start_urls=['https://baoxian.taobao.com/json/item/info.do?item_id=540732488665']
    
    def parse(self, response):

        product_item = ProductInfoItem()
        response_data = json.loads(response.text)

        product_item['is_product'] = 1

        product_item['_id'] = response_data['itemId']
        product_item['product_tags'] = response_data['itemTags']
        product_item['product_collected'] = response_data['collectorCount']

        product_priceRange = response_data['price']
        product_item['product_maxprice'] = product_priceRange[product_priceRange.rfind('~') + 1 :]
        product_item['product_minprice'] = product_priceRange[: product_priceRange.rfind('~') - 1]
        

        product_item['seller_comp'] = response_data['sellerComp']
        
        yield product_item
        
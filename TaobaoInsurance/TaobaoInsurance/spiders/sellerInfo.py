import scrapy,pymongo,json

from TaobaoInsurance.items import SellerInfoItem
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

'''服务器信息'''

zd_host = settings['MONGODB_HOST']
zd_port = settings['MONGODB_PORT']
zd_client = pymongo.MongoClient(host=zd_host, port=zd_port)
zd_db = zd_client['TaobaoInsurance']

class sellerInfoSpider(scrapy.Spider):

    name = 'sellerInfo'
    
    '''正式'''

    doc_productInfo = zd_db['product_info']
    doc_sellerInfo = zd_db['seller_info']
    
    start_urls = []

    data_productInfo = doc_productInfo.find()
    data_sellerInfo = doc_sellerInfo.find()
    
    for each_product in data_productInfo:

        json_url = 'https://baoxian.taobao.com/json/item/info.do?item_id=' + str(each_product['product_id'])
        start_urls.append(json_url)
    
    '''测试'''

    # start_urls = ['https://baoxian.taobao.com/json/item/info.do?item_id=540732488665']

    def parse(self, response):
        
        seller_item = SellerInfoItem()
        response_data = json.loads(response.text)
        
        seller_item['is_sellerInfo'] = 1
        seller_item['seller_id'] = str(response_data['sellerId'])
        seller_item['seller_comp'] = str(response_data['sellerComp'])
        seller_item['seller_name'] = str(response_data['sellerNick'])
        seller_item['shop_id'] = str(response_data['shopId'])
        seller_item['shop_name'] = str(response_data['shopName'])
        seller_item['product_count'] = response_data['productCount']
        
        yield seller_item
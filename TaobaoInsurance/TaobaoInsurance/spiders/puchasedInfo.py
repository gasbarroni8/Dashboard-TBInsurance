import scrapy,pymongo,json

from TaobaoInsurance.items import PurchasedInfoItem
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

'''服务器信息'''

zd_host = settings['MONGODB_HOST']
zd_port = settings['MONGODB_PORT']
zd_client = pymongo.MongoClient(host=zd_host, port=zd_port)
zd_db = zd_client['TaobaoInsurance']

class puchasedInfoSpider(scrapy.Spider):

    name = 'puchasedInfo'
    
    '''正式'''

    doc_sellerInfo = zd_db['seller_info']

    # 根据每个文档中的seller_id和product_list中的product_id拼接链接而成

    base_url = 'http://baoxian.taobao.com/json/item/purchaseList.do?'
    
    data_sellerInfo = doc_sellerInfo.find()

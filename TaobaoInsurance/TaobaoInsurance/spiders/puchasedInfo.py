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

    name = 'purchasedInfo'
    
    '''正式'''

    # doc_sellerInfo = zd_db['seller_info']
    # start_urls = []

    # # 根据每个文档中的seller_id和product_list中的product_id拼接链接而成

    # base_url = 'http://baoxian.taobao.com/json/item/purchaseList.do?'
    
    # data_sellerInfo = doc_sellerInfo.find()

    # for each_seller in data_sellerInfo:

    #     each_sellerId = each_seller['seller_id']

    #     for each_productId in each_seller['product_list'] :

    #         target_url = base_url + 'seller_id=' + each_sellerId + '&item_id=' + each_productId + '&pageNo=1'

    #         start_urls.append(target_url)
    
    '''调试'''

    start_urls= ['http://baoxian.taobao.com/json/item/purchaseList.do?item_id=540732488665&seller_id=2967530750']
    
    def parse(self,response):

        response_data= json.loads(response.text)
        
        '''处理思路'''

        # 读取totalPage字段，如果超过13333，则循环次数为13333，否则为totalPage

        purchase_data = {}
        
        for each_data in response_data['data']:

            key_price = each_data['price']

            # 判断purchase_data中是否存在该价格键值对，如果没有则创建，创建时的value为对应each_data下的num

            if purchase_data.__contains__(key_price):

                purchase_data.update({key_price: purchase_data[key_price] + each_data['num']})
            
            else:

                purchase_data.update({key_price: each_data['num']})
        
        yield purchase_data
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

    start_urls= ['http://baoxian.taobao.com/json/item/purchaseList.do?item_id=540732488665&seller_id=2967530750&pageNo=1']
    
    def parse(self,response):

        response_data= json.loads(response.text)
        
        '''处理思路'''

        # 读取totalPage字段，如果超过13333，则循环次数为13333，否则为totalPage

        purchased_item = PurchasedInfoItem()
        purchased_item['is_purchased'] = 1
        purchased_item['product_id'] = response.url[response.url.find('=') + 1 : response.url.find('&')]
        purchased_item['data'] = {}

        for each_data in response_data['data']:

            key_date = each_data['time'][:10]
            key_price = each_data['price'][: each_data['price'].find('.')]

            if purchased_item['data'].__contains__(key_date):


                if purchased_item['data'][key_date].__contains__(key_price):

                    purchased_item['data'][key_date].update({key_price: purchased_item['data'][key_date][key_price] + each_data['num']})
                
                else:

                    purchased_item['data'][key_date].update({key_price: each_data['num']})
            
            else:

                purchased_item['data'].update({key_date: {key_price: each_data['num']}})
        
        yield purchased_item
        
        if response_data['totalPage'] <= 13333:

            last_page = response_data['totalPage']

        else:
            
            last_page = 13333

        next_page = int(response.url[response.url.rfind('=') + 1 :]) + 1

        if next_page < last_page:

            new_url = response.url[: response.url.rfind('=') + 1] + str(next_page)
            yield response.follow(new_url,callback=self.parse)
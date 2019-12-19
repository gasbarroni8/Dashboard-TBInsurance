import scrapy, pymongo, json, datetime, time

from TaobaoInsurance.items import PurchasedInfoItem
from scrapy.utils.project import get_project_settings

settings = get_project_settings()

'''服务器信息'''

zd_host = settings['MONGODB_HOST']
zd_port = settings['MONGODB_PORT']
zd_client = pymongo.MongoClient(host=zd_host, port=zd_port)
zd_db = zd_client['TaobaoInsurance']

class purchasedInfoSpider(scrapy.Spider):

    name = 'purchasedInfo'
    
    '''正式'''

    doc_sellerInfo = zd_db['seller_info']
    start_urls = []

    # 根据每个文档中的seller_id和product_list中的product_id拼接链接而成

    # base_url = 'http://baoxian.taobao.com/json/item/purchaseList.do?'
    
    # data_sellerInfo = doc_sellerInfo.find()

    # for each_seller in data_sellerInfo:

    #     each_sellerId = each_seller['seller_id']

    #     for each_productId in each_seller['product_list'] :

    #         target_url = base_url + 'item_id=' + each_productId + '&seller_id=' + each_sellerId + '&pageNo=1'

    #         start_urls.append(target_url)
    
    '''调试'''

    start_urls= ['http://baoxian.taobao.com/json/item/purchaseList.do?item_id=43467881347&seller_id=407675891&pageNo=1']
    
    def parse(self,response):

        response_data= json.loads(response.text)
        date_begin = datetime.date.today() - datetime.timedelta(days=1)
        # print(date_begin)
        date_lastindex = datetime.date(int(response_data['data'][-1]['time'][0:4]), int(response_data['data'][-1]['time'][5:7]), int(response_data['data'][-1]['time'][8:10]))
        # print(date_lastindex)

        if response_data['totalPage'] <= 13333:

            last_page = response_data['totalPage']
        else:

            last_page = 13333

        next_page = int(response.url[response.url.rfind('=') + 1 :]) + 1

        if date_lastindex.__gt__(date_begin):   #   date_lastindex>date_begin
            
            pass

        else:

            purchased_item = PurchasedInfoItem()
            purchased_item['is_purchased'] = 1
            purchased_item['product_id'] = response.url[response.url.find('=') + 1 : response.url.find('&')]
            purchased_item['data'] = {}

            for each_data in response_data['data']:

                key_date = each_data['time'][:10]
                key_price = each_data['price'][: each_data['price'].find('.')]

                data_eachdate = datetime.date(int(each_data['time'][0:4]), int(each_data['time'][5:7]), int(each_data['time'][8:10]))

                if data_eachdate.__eq__(date_begin):

                    if purchased_item['data'].__contains__(key_date):

                        if purchased_item['data'][key_date].__contains__(key_price):

                            purchased_item['data'][key_date].update({key_price: purchased_item['data'][key_date][key_price] + each_data['num']})
                        
                        else:

                            purchased_item['data'][key_date].update({key_price: each_data['num']})
                    
                    else:

                        purchased_item['data'].update({key_date: {key_price: each_data['num']}})
            
            yield purchased_item
        
        if date_lastindex.__ge__(date_begin) and next_page<last_page :

            new_url = response.url[: response.url.rfind('=') + 1] + str(next_page)
            yield response.follow(new_url,callback=self.parse)
        
        '''处理思路'''

        # 读取页面中的日期，如果读到date_begin则开始记录，如果督导date_end则终止记录
        # 读取totalPage字段，如果超过13333，则循环次数为13333，否则为totalPage

        # purchased_item = PurchasedInfoItem()
        # purchased_item['is_purchased'] = 1
        # purchased_item['product_id'] = response.url[response.url.find('=') + 1 : response.url.find('&')]
        # purchased_item['data'] = {}

        # for each_data in response_data['data']:

        #     key_date = each_data['time'][:10]
        #     key_price = each_data['price'][: each_data['price'].find('.')]

        #     data_eachdate = time.mktime(time.strptime(each_data['time'], "%Y-%m-%d %H:%M:%S"))
            
        #     if data_eachdate > date_begin:
                
        #         pass

        #     elif data_eachdate == date_begin:
                
        #         if purchased_item['data'].__contains__(key_date):


        #             if purchased_item['data'][key_date].__contains__(key_price):

        #                 purchased_item['data'][key_date].update({key_price: purchased_item['data'][key_date][key_price] + each_data['num']})
                    
        #             else:

        #                 purchased_item['data'][key_date].update({key_price: each_data['num']})
                
        #         else:

        #             purchased_item['data'].update({key_date: {key_price: each_data['num']}})
        
        # yield purchased_item
        
        # if response_data['totalPage'] <= 13333:

        #     last_page = response_data['totalPage']

        # else:
            
        #     last_page = 13333

        # next_page = int(response.url[response.url.rfind('=') + 1 :]) + 1

        # if next_page < last_page:

        #     new_url = response.url[: response.url.rfind('=') + 1] + str(next_page)
        #     yield response.follow(new_url,callback=self.parse)
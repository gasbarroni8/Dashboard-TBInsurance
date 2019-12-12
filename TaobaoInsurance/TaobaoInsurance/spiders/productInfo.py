import scrapy, pymongo, json

from scrapy.utils.project import get_project_settings
from TaobaoInsurance.items import ProductInfoItem, SellerInfoItem


settings = get_project_settings()

'''服务器信息'''

zd_host = settings['MONGODB_HOST']
zd_port = settings['MONGODB_PORT']
zd_client = pymongo.MongoClient(host=zd_host, port=zd_port)
zd_db = zd_client['TaobaoInsurance']

'''version1'''

# class productInfoSpider(scrapy.Spider):

#     name = 'productInfo'

#     '''正式用例'''
    
#     start_urls = []
    
#     doc_product = zd_db['product_info']
#     doc_data = doc_product.find()
    
#     for each_product in doc_data:

#         json_url = 'https://baoxian.taobao.com/json/item/info.do?item_id=' + str(each_product['_id'])       
#         start_urls.append(json_url)
    
#     '''调试用例'''

#     # start_urls=['https://baoxian.taobao.com/json/item/info.do?item_id=540732488665']
    
#     def parse(self, response):

#         product_item = ProductInfoItem()
#         response_data = json.loads(response.text)

#         product_item['is_productInfo'] = 1

#         product_item['_id'] = str(response_data['itemId'])
#         product_item['product_tags'] = response_data['itemTags']
#         product_item['product_collected'] = response_data['collectorCount']

#         '''产品价格'''

#         product_priceRange = response_data['price']

#         if product_priceRange.find('~') != -1:
#             product_item['product_maxprice'] = product_priceRange[product_priceRange.rfind('~') + 1 :]
#             product_item['product_minprice'] = product_priceRange[: product_priceRange.rfind('~') - 1]

#         else:
#             product_item['product_maxprice'] = product_priceRange
#             product_item['product_minprice'] = product_priceRange
            
#         '''产品详情'''

#         product_data = response_data['skuItem']
#         product_item['product_detail']= {}
        
#         for each_data in product_data:

#             temp_keys = each_data['skuTitle']
#             temp_values = []

#             for values in each_data['skuMapId'].values():
#                 temp_values.append(values)
            
#             product_item['product_detail'].update({temp_keys: temp_values})
            


#         '''地址'''

#         product_item['product_purchasedurl'] = 'https://baoxian.taobao.com' + response_data['purchaseUrl']
#         product_item['product_insuredurl'] = 'https://baoxian.taobao.com' + response_data['insuredProjectUrl']
        

#         product_item['seller_comp'] = response_data['sellerComp']
        
#         yield product_item

'''version2'''

class productInfoSpider(scrapy.Spider):

    name = 'productInfo'

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
        
        product_item = ProductInfoItem()
        seller_item = SellerInfoItem()
        response_data = json.loads(response.text)
        
        '''产品相关'''

        product_item['is_productInfo'] = 1

        product_item['product_id'] = str(response_data['itemId'])
        product_item['product_tags'] = response_data['itemTags']
        product_item['product_tags'].sort()
        product_item['product_collected'] = response_data['collectorCount']
        
        product_priceRange = str(response_data['price'])

        if product_priceRange.find('~') != -1:
            product_item['product_maxprice'] = product_priceRange[product_priceRange.rfind('~') + 1 :]
            product_item['product_minprice'] = product_priceRange[: product_priceRange.rfind('~') - 1]

        else:
            product_item['product_maxprice'] = product_priceRange
            product_item['product_minprice'] = product_priceRange
        
        product_data = response_data['skuItem']

        product_item['product_detail']= {}
        
        for each_data in product_data:

            temp_keys = each_data['skuTitle']
            temp_values = []

            for values in each_data['skuMapId'].values():
                temp_values.append(values)
            
            temp_values.sort()
            
            product_item['product_detail'].update({temp_keys: temp_values})
        
        product_item['seller_id'] = str(response_data['shopId'])
        
        yield product_item

        seller_item['is_sellerInfo'] = 1
        seller_item['seller_id'] = str(response_data['shopId'])
        seller_item['seller_comp'] = response_data['sellerComp']
        seller_item['seller_name'] = response_data['sellerNick']
        
        
        yield seller_item
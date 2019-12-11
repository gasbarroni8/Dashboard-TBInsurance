# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo,time

from scrapy.utils.project import get_project_settings

settings = get_project_settings()

'''服务器信息'''

zd_host = settings['MONGODB_HOST']
zd_port = settings['MONGODB_PORT']
zd_client = pymongo.MongoClient(host=zd_host, port=zd_port)
zd_db= zd_client['TaobaoInsurance']

class TaobaoinsurancePipeline(object):
    def process_item(self, item, spider):
        return item

'''version1'''

# class ProductListPipeline(object):

#     def __init__(self):
#        self.doc_product= zd_db['product_info']

#     def process_item(self,item,spider):

#         '''item转dict'''

#         process_data= dict(item)

#         if process_data.__contains__('is_productList'): #管道判断
#             product_found = self.doc_product.find_one({'_id': process_data['_id']})

#             if product_found is None:
#                 process_data.update({'create_time':time.strftime('%Y-%m-%d' , time.localtime())})
#                 self.doc_product.insert(process_data)
#                 return item

#             else:
#                 if product_found==process_data:
#                     return item

#                 else:
#                     process_data.update({'update_time': time.strftime('%Y-%m-%d', time.localtime())})
#                     process_data.update({'create_time': product_found['create_time']})

#                     self.doc_history = zd_db['product_history']
#                     history_found = self.doc_history.find_one({'_id': process_data['_id']})
                    
#                     if history_found is None:
#                         history_data = ProductHistoryItem()
#                         history_data['_id'] = process_data['_id']
#                         history_data['data'] = {}
#                         history_data['data'].update({
#                             time.strftime('%Y-%m-%d', time.localtime()):product_found
#                         })
#                         zd_db['product_history'].insert(history_data)
                    
#                     else:
#                         history_found['data'].insert({
#                             time.strftime('%Y-%m-%d', time.localtime()): product_found
#                         })
#                         new_data = history_found['data']
#                         self.doc_history.update_one({'_id':process_data['_id']},{'$set':new_data})
                    
#                     self.doc_product.update_one({'_id': process_data['_id']}, {'$set': process_data})
#                     return item
        
#         else:
#             return item


# class ProductInfoPipeline(object):

#     def __init__(self):
#         self.doc_product = zd_db['product_info']
    
#     def process_item(self, item, spider):
        
#         '''item转dict'''

#         process_data = dict(item)
        
#         if process_data.__contains__('is_productInfo'):
#             product_found = self.doc_product.find_one({'_id': process_data['_id']})

#             if product_found is None:
#                 return item
            
#             else:

#                 for product_key in process_data.keys():

#                     if product_found.__contains__(product_key):
#                         if product_found[product_key] == process_data[product_key]:
#                             pass
#                         else:
#                             self.doc_product.update_one({'_id': process_data['_id']}, {'$set': {product_key: process_data[product_key]}})
#                     else:
#                         self.doc_product.update_one({'_id': process_data['_id']}, {'$set': {product_key: process_data[product_key]}})
                
#                 return item
        
#         else:
#             return item

'''version2'''

class ProductListPipeline(object):

    '''productList管道处理内容'''

    # 该管道处理由productList.py中提交的product_item和seller_item
    
    # product_item包含如下字段：
    # is_productList--->管道识别用
    # product_name--->产品名称
    # product_url--->产品链接
    # product_id--->产品识别号

    # seller_item包含如下字段：
    # is_seller--->管道识别用
    # seller_id--->商户识别号
    # seller_name--->商户名称

    # 处理思路：
    # 判断表中有无存储，如果没有则插入，有的话在该管道不做处理

    def __init__(self):

        self.doc_productInfo = zd_db['product_info']
        self.doc_sellerInfo = zd_db['seller_info']
        
    def process_item(self, item, spider):
        
        process_data = dict(item)

        if process_data.__contains__('is_productList'):

            product_found = self.doc_productInfo.find_one({'product_id': process_data['product_id']})
            
            if product_found is None:

                del process_data['is_productList']
                self.doc_productInfo.insert(process_data)
                return item

            else:

                return item

        elif process_data.__contains__('is_seller'):

            seller_found = self.doc_sellerInfo.find_one({'seller_id': process_data['seller_id']})
            
            if seller_found is None:

                del process_data['is_seller']
                self.doc_sellerInfo.insert(process_data)
                return item

            else:

                return item
        
        else:
    
            return item
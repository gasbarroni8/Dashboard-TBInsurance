# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo,time

from scrapy.utils.project import get_project_settings
from TaobaoInsurance.items import ProductHistoryItem

settings = get_project_settings()

'''服务器信息'''

zd_host = settings['MONGODB_HOST']
zd_port = settings['MONGODB_PORT']
zd_client = pymongo.MongoClient(host=zd_host, port=zd_port)
zd_db= zd_client['TaobaoInsurance']

# class TaobaoinsurancePipeline(object):
#     def process_item(self, item, spider):
#         return item

class ProductListPipeline(object):

    def __init__(self):
       self.doc_product= zd_db['product_info']

    def process_item(self,item,spider):

        '''item转dict'''

        process_data= dict(item)

        if process_data.__contains__('is_product'): #管道判断
            product_found= self.doc_product.find_one({'_id':process_data['_id']})

            if product_found is None:
                process_data.update({'create_time':time.strftime('%Y-%m-%d' , time.localtime())})
                self.doc_product.insert(process_data)
                return item

            else:
                if product_found==process_data:
                    return item

                else:
                    process_data.update({'update_time': time.strftime('%Y-%m-%d', time.localtime())})
                    process_data.update({'create_time': product_found['create_time']})

                    self.doc_history = zd_db['product_history']
                    history_found = self.doc_history.find_one({'_id': process_data['_id']})
                    
                    if history_found is None:
                        history_data = ProductHistoryItem()
                        history_data['_id'] = process_data['_id']
                        history_data['data'] = {}
                        history_data['data'].update({
                            time.strftime('%Y-%m-%d', time.localtime()):product_found
                        })
                        zd_db['product_history'].insert(history_data)
                    
                    else:
                        history_found['data'].insert({
                            time.strftime('%Y-%m-%d', time.localtime()): product_found
                        })
                        new_data = history_found['data']
                        self.doc_history.update_one({'_id':process_data['_id']},{'$set':new_data})
                    
                    self.doc_product.update_one({'_id': process_data['_id']}, {'$set': process_data})
                    return item
        
        else:
            return item



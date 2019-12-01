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
zd_client= pymongo.MongoClient(host=zd_host,port=zd_port)

# class TaobaoinsurancePipeline(object):
#     def process_item(self, item, spider):
#         return item

class ProductListPipeline(object):

    def __init__(self):

       self.doc_product= zd_client['product_info']

    def process_item(self,item,spider):

        '''item转dict'''

        process_data= dict(item)

        if process_data.__contains__('is_product'):

            product_found= self.doc_product.find_one({'_id':process_data['_id']})

            if product_found is None:

                process_data.update({'create_time':time.strftime('%Y-%m-%d' , time.localtime())})

                self.doc_product.insert(process_data)

                return item

            else:

                if product_found==process_data:

                    return item

                else:

                    process_data.update({'update_time'})

                    self.doc_product.update_one()
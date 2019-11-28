# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TaobaoinsuranceItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

'''店铺信息'''

class SellerInfoItem(scrapy.Item):

    is_seller = scrapy.Field()  #管道识别，Number
    
    _id = scrapy.Field()    #店铺编号，String
    seller_nick = scrapy.Field()    #店铺名称，String
    seller_comp = scrapy.Field()    #店铺公司，String
    seller_group = scrapy.Field()   #店铺所属集团，String
    seller_class = scrapy.Field()  #店铺分类，Number（1自营2经纪）

    product_data = scrapy.Field()  #店铺售卖产品，Object


'''商品信息'''

class ProductInfoItem(scrapy.Item):

    is_product = scrapy.Field()  #管道识别，Number
    
    _id = scrapy.Field()  #商品编号，String
    product_name = scrapy.Field()  #商品名称，String
    product_url = scrapy.Field()  #商品地址，String
    product_minprice = scrapy.Field()  #商品最低价格，String
    product_maxprice = scrapy.Field()  #商品最高价格，String
    product_detail = scrapy.Field()  #商品详情，String
    product_collected = scrapy.Field()  #商品收藏，Number
    product_tags = scrapy.Field()  #商品标签，String
    
    seller_id = scrapy.Field()  #店铺编号，String

'''购买记录'''

class PurchasedInfoItem(scrapy.Item):

    is_purchased = scrapy.Field()  #管道识别，Number
    
    _id = scrapy.Field()  #商品编号，String
    product_name = scrapy.Field()  #商品名称，String
    seller_id = scrapy.Field()  #店铺编号，String
    seller_name = scrapy.Field()  #店铺名称，String
    
    
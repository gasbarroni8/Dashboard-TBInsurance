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
    is_seller = scrapy.Field()  # 管道识别，Number

    _id = scrapy.Field()  # 店铺编号，String
    seller_nick = scrapy.Field()  # 店铺名称，String
    seller_comp = scrapy.Field()  # 店铺公司，String
    seller_group = scrapy.Field()  # 店铺所属集团，String
    seller_class = scrapy.Field()  # 店铺分类，Number（1自营2经纪）

    product_data = scrapy.Field()  # 店铺售卖产品，Object


'''商品信息'''


class ProductInfoItem(scrapy.Item):
    is_productList = scrapy.Field()  # 管道识别，Number
    is_productInfo = scrapy.Field()  #管道识别，Number
    
    _id = scrapy.Field()  # 商品编号，String
    product_name = scrapy.Field()  # 商品名称，String
    product_url = scrapy.Field()  # 商品地址，String
    product_minprice = scrapy.Field()  # 商品最低价格，String
    product_maxprice = scrapy.Field()  # 商品最高价格，String
    product_detail = scrapy.Field()  # 商品详情，String
    product_collected = scrapy.Field()  # 商品收藏，Number
    product_tags = scrapy.Field()  # 商品标签，String
    product_buylimit = scrapy.Field()  #购买限制，Number

    product_purchasedurl = scrapy.Field()  #产品购买详情地址，String
    product_insuredurl = scrapy.Field()  #产品爆涨详情地址，String

    seller_id = scrapy.Field()  # 店铺编号，String
    seller_nick = scrapy.Field()  #店铺名称，String
    seller_comp = scrapy.Field()  #公司名称，String

'''商品历史信息'''

class ProductHistoryItem(scrapy.Item):

    is_producthis = scrapy.Field()  #管道识别，Number
    
    _id = scrapy.Field()    #商品编号，String
    data= scrapy.Field()    #历史数据，Object


'''购买记录'''


class PurchasedInfoItem(scrapy.Item):
    is_purchased = scrapy.Field()  # 管道识别，Number

    _id = scrapy.Field()  # 商品编号，String
    product_name = scrapy.Field()  # 商品名称，String
    seller_id = scrapy.Field()  # 店铺编号，String
    seller_name = scrapy.Field()  # 店铺名称，String

    purchased_total = scrapy.Field()  # 销量总计，Object


'''购买记录（详细）'''


class PurchasedDetailItem(scrapy.Item):
    is_detail = scrapy.Field()  # 管道识别，Number

    _id = scrapy.Field()  # 商品编号，String
    product_name = scrapy.Field()  # 商品名称，String
    seller_id = scrapy.Field()  # 店铺编号，String
    seller_name = scrapy.Field()  # 店铺名称, String

    purchased_daily = scrapy.Field()  # 日销量数据，Object


'''产品保障方案'''


class InsuredInfoItem(scrapy.Item):
    is_insured = scrapy.Field()  # 管道使用，Number

    _id = scrapy.Field()  # 商品编号，String
    product_name = scrapy.Field()  # 商品名称，String
    seller_id = scrapy.Field()  # 店铺编号，String
    seller_name = scrapy.Field()  # 店铺名称，String

    insured_data = scrapy.Field()  # 保障内容，Object
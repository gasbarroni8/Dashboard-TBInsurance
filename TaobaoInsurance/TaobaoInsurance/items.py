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

# eg(店铺基本信息+商品基本信息)
# https://baoxian.taobao.com/json/item/info.do?item_id=540732488665

# eg(商品购买信息)
# http://baoxian.taobao.com/json/item/purchaseList.do?item_id=540732488665&seller_id=2967530750

# eg(商品文案告知内容)
# http://baoxian.taobao.com/json/item/insuredProject.do?item_id=540732488665

'''店铺信息'''

class SellerInfoItem(scrapy.Item):

    '''version1'''

    # is_seller = scrapy.Field()  # 管道识别，number

    # _id = scrapy.Field()  # 店铺编号，string
    # seller_nick = scrapy.Field()  # 店铺名称，string
    # seller_comp = scrapy.Field()  # 店铺公司，string
    # seller_group = scrapy.Field()  # 店铺所属集团，string
    # seller_class = scrapy.Field()  # 店铺分类，number（1自营2经纪）

    # product_data = scrapy.Field()  # 店铺售卖产品，Object

    '''version2'''

    is_sellerInfo = scrapy.Field()  #管道识别，number

    seller_id = scrapy.Field()  #店铺编号，string
    seller_name = scrapy.Field()  #店铺昵称，string
    seller_comp = scrapy.Field()  #公司名称，string
    seller_group = scrapy.Field()  #集团名称，string
    seller_class = scrapy.Field()  #公司分类，string
    shop_id = scrapy.Field()  #商铺编号，String
    shop_name = scrapy.Field()  #商铺名称，String
    product_count = scrapy.Field()  #产品数量，Number
    
    product_list = scrapy.Field()  #产品列表，array
    histroy_list = scrapy.Field()  #产品历史，array


'''商品信息&商品历史信息'''

class ProductInfoItem(scrapy.Item):

    '''version1'''

    # is_productList = scrapy.Field()  # 管道识别，number
    # is_productInfo = scrapy.Field()  #管道识别，number
    
    # _id = scrapy.Field()  # 商品编号，string
    # product_name = scrapy.Field()  # 商品名称，string
    # product_url = scrapy.Field()  # 商品地址，string
    # product_minprice = scrapy.Field()  # 商品最低价格，string
    # product_maxprice = scrapy.Field()  # 商品最高价格，string
    # product_detail = scrapy.Field()  # 商品详情，string
    # product_collected = scrapy.Field()  # 商品收藏，number
    # product_tags = scrapy.Field()  # 商品标签，string
    # product_buylimit = scrapy.Field()  #购买限制，number

    # product_purchasedurl = scrapy.Field()  #产品购买详情地址，string
    # product_insuredurl = scrapy.Field()  #产品爆涨详情地址，string

    # seller_id = scrapy.Field()  # 店铺编号，string
    # seller_nick = scrapy.Field()  #店铺名称，string
    # seller_comp = scrapy.Field()  #公司名称，string

    '''version2'''

    is_productList = scrapy.Field()  #管道识别，number
    is_productInfo = scrapy.Field()  #管道识别，number
    is_productHis = scrapy.Field()  #管道识别，number

    product_id = scrapy.Field()  #商品编号，string
    product_name = scrapy.Field()  #商品名称，string
    product_url = scrapy.Field()  #商品地址，string
    product_maxprice = scrapy.Field()  #商品最高价，number
    product_minprice = scrapy.Field()  #商品最低价，number
    product_sellcount = scrapy.Field()  #商品销量，number
    product_collected = scrapy.Field()  #商品收藏数量，number
    product_tags = scrapy.Field()  #商品标签，array
    product_buylimit = scrapy.Field()  #商品购买限制，number
    product_detail = scrapy.Field()  #商品详情，json
    product_purchase = scrapy.Field()  #购买数据，bson
    product_insured = scrapy.Field()  #保障信息，bson
    time_online = scrapy.Field()  #上线时间，string
    time_offline = scrapy.Field()  #下线时间，string

    seller_id = scrapy.Field()  #店铺编号，number
   

# '''商品历史信息'''

# class ProductHistoryItem(scrapy.Item):

#     is_productHis = scrapy.Field()  #管道识别，number
    
#     _id = scrapy.Field()    #商品编号，string
#     data= scrapy.Field()    #历史数据，Object


'''购买记录'''


class PurchasedInfoItem(scrapy.Item):

    '''version1'''
    
    # is_purchased = scrapy.Field()  # 管道识别，number

    # _id = scrapy.Field()  # 商品编号，string
    # product_name = scrapy.Field()  # 商品名称，string
    # seller_id = scrapy.Field()  # 店铺编号，string
    # seller_name = scrapy.Field()  # 店铺名称，string

    # purchased_total = scrapy.Field()  # 销量总计，Object

    '''version2'''

    is_purchased = scrapy.Field()  #管道识别，number

    product_id = scrapy.Field()  #商品编号，string
    data = scrapy.Field()  #数据容器，json
    

# '''购买记录（详细）'''

# class PurchasedDetailItem(scrapy.Item):
#     is_detail = scrapy.Field()  # 管道识别，number

#     _id = scrapy.Field()  # 商品编号，string
#     product_name = scrapy.Field()  # 商品名称，string
#     seller_id = scrapy.Field()  # 店铺编号，string
#     seller_name = scrapy.Field()  # 店铺名称, string

#     purchased_daily = scrapy.Field()  # 日销量数据，Object

'''产品保障方案'''


class InsuredInfoItem(scrapy.Item):

    '''version1'''

    # is_insured = scrapy.Field()  # 管道使用，number

    # _id = scrapy.Field()  # 商品编号，string
    # product_name = scrapy.Field()  # 商品名称，string
    # seller_id = scrapy.Field()  # 店铺编号，string
    # seller_name = scrapy.Field()  # 店铺名称，string

    # insured_data = scrapy.Field()  # 保障内容，Object
    
    '''version2'''

    is_insured = scrapy.Field()  #管道识别，number
    
    product_id = scrapy.Field()  #商品编号，string
    history_id = scrapy.Field()  #历史信息编号，bson
    time_online = scrapy.Field()  #上线时间，string
    time_offline = scrapy.Field()  #下线时间，string
    data = scrapy.Field()  #数据容器，json
##	淘宝保险数据可视化项目



####	1.	项目背景

淘宝网的[保险频道](https://baoxian.taobao.com)下店铺以及产品数据的可视化展示。



####	2.	数据模型

数据库存储采用的MongoDB进行存储。



#####	2.1	店铺信息（seller_info)

| 属性名称     | 值类型 | 备注                                        |
| ------------ | ------ | ------------------------------------------- |
| _id          | bson   | 自动生成的ObjectId。                        |
| seller_id    | string | 淘宝店铺唯一编号。                          |
| seller_name  | string | 淘宝店铺名称。                              |
| seller_comp  | string | 公司名称。                                  |
| seller_class | number | 店铺分类。1--自营，2--经纪。                |
| seller_url   | string | 淘宝店铺地址。                              |
| product_list | array  | 产品列表，数组形式，存放2.2中的product_id。 |
| history_list | array  | 历史产品列表，数组形势。                    |

#####	范例

```json
{
    "_id":,
    "seller_id":"",
    "seller_name":"",
    "seller_comp":"",
    "seller_url":"",
    "product_list":[],
    "history_list":[],
}
```



#####	2.2	产品信息（product_info）&产品历史信息（product_history）

| 属性名称          | 值类型 | 备注                                 |
| ----------------- | ------ | ------------------------------------ |
| _id               | bson   | 自动生成ObjectId。                   |
| product_id        | string | 产品唯一编号。                       |
| product_url       | string | 产品链接地址。                       |
| product_maxprice  | number | 产品最高价格。                       |
| product_minprice  | number | 产品最低价格。                       |
| product_sellcount | number | 产品售出份数。                       |
| product_tags      | array  | 产品标签列表，单个标签为String格式。 |
| product_buylimit  | number | 产品购买限制。                       |
| product_detail    | json   | 产品方案详情。                       |
| product_purchase  | bson   |                                      |
| product_insured   | bson   |                                      |
| time_online       | string | 产品上线时间，格式为“yyyy-mm-dd”。   |
| time_offline      | string | 产品下线时间，格式为“yyyy-mm-dd”。   |

#####	范例

```json
{
    "_id":"",
    "product_id":"",
    "product_url":"",
    "product_maxprice":,
    "product_minprice":,
    "product_sellcount":,
    "product_tags":"",
    "product_buylimit":,
    "product_detail":,
    "product_purchase":,
    "product_insured":,
    "time_online":,
    "time_offline":,
}
```



#####	2.3	产品购买信息（product_purchase）

| 属性名称   | 值类型 | 备注                                     |
| ---------- | ------ | ---------------------------------------- |
| _id        | bson   | 自动生成的ObjectId。                     |
| product_id | string | 产品唯一编号。                           |
| *date*     | json   | 日销售数据，价格为key，对应销量为value。 |

#####	范例

```json
{
    "_id":,
    "product_id":"",
    "20191210":{},
    "20191211":{},
}
```



#####	2.4	产品相关文档（product_insured）

| 属性名称     | 值类型 | 备注                                           |
| ------------ | ------ | ---------------------------------------------- |
| _id          | bson   | 自动生成的ObjectId。                           |
| product_id   | string | 产品唯一编号。                                 |
| histroy_id   | string | 历史信息编号，对应2.2中product_info的“_id”值。 |
| time_online  | string | 产品上线时间，格式为“yyyy-mm-dd”。             |
| time_offline | string | 产品下线时间，格式为“yyyy-mm-dd”。             |
| *title*      | json   | 文档内容，标题为key，内容对value。             |

#####	范例

```json
{
    "_id":,
    "product_id":"",
    "history_id":"",
    "time_online":"",
    "time_offline":"",
    "保障内容":{},
    "投保须知":{},
}
```


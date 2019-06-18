# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #pm_item = scrapy.Field()

    #简介
    pm_dexId = scrapy.Field()
    pm_name_cn = scrapy.Field()
    pm_name_en = scrapy.Field()
    pm_name_jp = scrapy.Field()
    pm_url = scrapy.Field()

    #种族值
    pm_HP = scrapy.Field()   #生命值
    pm_Atk = scrapy.Field()  #物攻
    pm_Def = scrapy.Field()  #物防
    pm_SAtk = scrapy.Field() #特攻
    pm_SDef = scrapy.Field() #特防
    pm_Spd = scrapy.Field()  #速度

    #属性
    pm_Type = scrapy.Field()    

    #特性
    pm_Abi = scrapy.Field()
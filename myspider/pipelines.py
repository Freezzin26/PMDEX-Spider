# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import pymongo

class MyspiderPipeline(object):
    def process_item(self, item, spider):
        pmitem = item
        client = pymongo.MongoClient('localhost', 27017)
        db = client['pmtest']
        collection = db['pmtest']
        collection.insert({
            "pm_dexId" : pmitem["pm_dexId"],
            "pm_name_cn" : pmitem["pm_name_cn"],
            "pm_name_en" : pmitem["pm_name_en"],
            "pm_name_jp" : pmitem["pm_name_jp"],
            "pm_Type" : pmitem["pm_Type"],
            "pm_Abi" : pmitem["pm_Abi"],
            "pm_HP" : pmitem["pm_HP"],
            "pm_Atk" : pmitem["pm_Atk"],
            "pm_Def" : pmitem["pm_Def"],
            "pm_SAtk" : pmitem["pm_SAtk"],
            "pm_SDef" : pmitem["pm_SDef"],
            "pm_Spd" : pmitem["pm_Spd"]
        })
        return item

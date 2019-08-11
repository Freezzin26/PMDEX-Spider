# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import logging
import sqlite3

class MyspiderPipeline(object):
    def process_item(self, item, spider):
        pmitem = item
        if len(pmitem["pm_Type"]) > 1:
            pmitem["pm_Type"] = ",".join(pmitem["pm_Type"])
        else:
            pmitem["pm_Type"] = pmitem["pm_Type"][0]
        if len(pmitem["pm_Abi"]) > 1:
            pmitem["pm_Abi"] = ",".join(pmitem["pm_Abi"])
        else:
            pmitem["pm_Abi"] = pmitem["pm_Abi"][0]
        dbpath = os.path.join(os.getcwd(), "PMdatabase.db")
        try:
            conn = sqlite3.connect(dbpath)
            cur = conn.cursor()
            sqlstr = "insert into pmdex(pm_Id,pm_name_cn,pm_name_en,pm_name_jp,pm_Type,pm_Abi,pm_HP,pm_Atk,pm_Def,pm_SAtk,pm_SDef,pm_Spd) values(?,?,?,?,?,?,?,?,?,?,?,?)"
            cur.execute(sqlstr, (pmitem["pm_dexId"],pmitem["pm_name_cn"],pmitem["pm_name_en"],pmitem["pm_name_jp"],pmitem["pm_Type"],pmitem["pm_Abi"],pmitem["pm_HP"],pmitem["pm_Atk"],pmitem["pm_Def"],pmitem["pm_SAtk"],pmitem["pm_SDef"],pmitem["pm_Spd"]))
            conn.commit()
            cur.close()
        except Exception:
            logging.log("Error!!!")
        return item

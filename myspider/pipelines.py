# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging

class MyspiderPipeline(object):
    def process_item(self, item, spider):
        with open('PMDEX.txt', 'a', encoding='utf-8') as f:
            nlist = []
            for i in item['pm_item']:
                nlist.append(i[0])
            f.write(' '.join(nlist) + '\n')
            print(" ".join(nlist))
        return item

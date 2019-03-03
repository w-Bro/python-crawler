# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json


# class QsbkPipeline(object):
#     def __init__(self):
#         self.fp = open('duanzi.json', 'w', encoding='utf-8')
#
#     def open_spider(self, spider):
#         print('爬虫开始了')
#
#     def process_item(self, item, spider):
#         item_json = json.dumps(dict(item), ensure_ascii=False)
#         self.fp.write(item_json + '\n')
#         return item
#
#     def close_spider(self, spider):
#         self.fp.close()
#         print('爬虫结束了')

# 将数据全部放入列表，finish时再统一写入，耗内存
# 好处是存储的数据是一个满足json规则的数据，坏处是数据量比较大，比较耗内存
# from scrapy.exporters import JsonItemExporter
#
# class QsbkPipeline(object):
#     def __init__(self):
#         self.fp = open('duanzi.json', 'wb')
#         self.exporter = JsonItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')
#         self.exporter.start_exporting()
#
#     def open_spider(self, spider):
#         print('爬虫开始了')
#
#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item
#
#     def close_spider(self, spider):
#         self.exporter.finish_exporting()
#         self.fp.close()
#         print('爬虫结束了')


# 好处是每次处理数据的时候就直接存储到了磁盘中，这样就不会耗内存，坏处是一个字典一行，整个文件不是一个满足json格式的文件
from scrapy.exporters import JsonLinesItemExporter


class QsbkPipeline(object):
    def __init__(self):
        self.fp = open('duanzi.json', 'wb')
        self.exporter = JsonLinesItemExporter(self.fp, ensure_ascii=False, encoding='utf-8')

    def open_spider(self, spider):
        print('爬虫开始了')

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.fp.close()
        print('爬虫结束了')
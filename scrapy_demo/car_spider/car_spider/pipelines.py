# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from urllib import request
from scrapy.pipelines.images import ImagesPipeline
from car_spider import settings

# 为什么要选择使用scrapy内置的下载文件的方法：
# 1. 避免重新下载最近已经下载过的数据
# 2. 可以方便的指定文件存储的路径
# 3. 可以将下载的图片转换成通用的格式，比如png和jpg
# 4. 可以方便的生成缩略图
# 5. 可以方便的检测图片的宽和高，确保他们满足最小限制
# 6. 异步下载，效率非常高


class CarSpiderPipeline(object):
    def __init__(self):
        # 设置绝对路径
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'images')
        if not os.path.exists(self.path):
            os.mkdir(self.path)

    def process_item(self, item, spider):
        category = item['category']
        urls = item['urls']
        category_path = os.path.join(self.path, category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)
        for url in urls:
            image_name = url.split('_')[-1]
            request.urlretrieve(url, os.path.join(category_path, image_name))

        return item


class CarImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # 早发送下载请求之前调用
        request_objs = super(CarImagePipeline, self).get_media_requests(item, info)
        for request_obj in request_objs:
            request_obj.item = item
        return request_objs

    def file_path(self, request, response=None, info=None):
        # 图片将要被存储时被调用来获取图片存储的路径
        path = super(CarImagePipeline, self).file_path(request, response, info)
        category = request.item.get('category')
        image_store = settings.IMAGES_STORE
        category_path = os.path.join(image_store, category)
        if not category_path:
            os.mkdir(category_path)
        image_name = path.replace("full/", "")
        image_path = os.path.join(category_path, image_name)
        return image_path

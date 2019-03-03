# -*- coding: utf-8 -*-
import scrapy
from car_spider.items import CarSpiderItem


class CarSpider(scrapy.Spider):
    name = "car"
    allowed_domains = ["car.autohome.com.cn"]
    start_urls = ['https://car.autohome.com.cn/pic/series/703.html#pvareaid=2042214']

    def parse(self, response):
        uiboxes = response.xpath("//div[@class='uibox']")[1:]
        for uibox in uiboxes:
            category = uibox.xpath(".//div[@class='uibox-title']/a/text()").get()
            urls = uibox.xpath(".//ul//li//a/img/@src").getall()
            # 给url加上https:
            urls = list(map(lambda url: response.urljoin(url), urls))
            item = CarSpiderItem(category=category, image_urls=urls)
            yield item

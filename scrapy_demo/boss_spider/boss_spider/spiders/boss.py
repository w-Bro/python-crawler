# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from boss_spider.items import BossSpiderItem


class BossSpider(CrawlSpider):
    name = 'boss'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c100010000/?query=python&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'https://www.zhipin.com/c100010000/\?query=python&page=\d'), follow=True),
        Rule(LinkExtractor(allow=r'https://www.zhipin.com/job_detail/.+\.html'), callback="parse_job", follow=False),
    )

    def parse_job(self, response):
        name = response.xpath("//div[@class='name']/h1/text()").get().strip()
        salary = response.xpath("//span[@class='salary']/text()").get().strip()
        job_info = response.xpath("//div[@class='job-primary detail-box']/div[@class='info-primary']/p//text()").getall()
        city = job_info[0]
        work_years = job_info[1]
        education = job_info[2]
        company = response.xpath("//div[@class='company-info']/a/@title").get()
        item = BossSpiderItem(name=name, salary=salary, city=city, work_years=work_years, education=education,
                              company=company)
        yield item
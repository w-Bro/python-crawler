# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wxapp_spider.items import WxappSpiderItem

# scrapy genspider -t crawl wxapp "http://www.wxapp-union.com/"


class WxappSpider(CrawlSpider):
    name = 'wxapp'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']

    rules = (
        # 如果这个url对应的页面只是为了获取更多的url，并不需要里面的数据，可以不指定callback
        # follow表示继续跟进，爬取符合规则的url
        Rule(LinkExtractor(allow=r'.+mod=list&catid=2&page=\d'), follow=True),
        # 爬取详情页规则
        Rule(LinkExtractor(allow=r'.+article-.+\.html'), callback="parse_detail", follow=False),
    )

    def parse_detail(self, response):
        title = response.xpath("//h1[@class='ph']/text()").get()
        author_p = response.xpath("//p[@class='authors']")
        author = author_p.xpath(".//a/text()").get()
        pub_time = author_p.xpath(".//span/text()").get()
        article_content = response.xpath("//td[@id='article_content']//text()").getall()
        content = "".join(article_content).strip()
        item = WxappSpiderItem(title=title, author=author, pub_time=pub_time, content=content)
        yield item

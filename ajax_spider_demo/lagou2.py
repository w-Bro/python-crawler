from selenium import webdriver
from lxml import etree
import time


class LagouSpider(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = 'https://www.lagou.com/jobs/list_python?city=%E5%B9%BF%E5%B7%9E&cl=false&fromSearch=true&labelWords=&suginput='

    def run(self):
        self.driver.get(self.url)
        # 这里跟在控制台看到的html代码一直，可以使用xpath
        source = self.driver.page_source
        self.parse_list_page(source)

    def parse_list_page(self, source):
        html = etree.HTML(source)
        links = html.xpath("//a[@class='position_link']/@href")
        for link in links:
            self.request_detail_page(link)
            break

    def request_detail_page(self, url):
        self.driver.get(url)
        source = self.driver.page_source
        self.parse_detail_page(source)

    def parse_detail_page(self, source):
        html = etree.HTML(source)
        job_name = html.xpath("//span[@class='name']/text()")[0]
        job_detail = html.xpath("//div[@class='job-detail']/p/text()")
        print(job_detail)


if __name__ == '__main__':
    spider = LagouSpider()
    spider.run()
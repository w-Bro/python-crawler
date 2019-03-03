from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common .by import By
from lxml import etree
import time
import pymongo


class BossSpider(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.first_url = 'https://www.zhipin.com/job_detail/?query=python&scity=100010000&industry=&position='
        self.base_domain = 'https://www.zhipin.com'
        self.jobs = []
        client = pymongo.MongoClient('localhost', port=27017)
        db = client.Boss_spider
        self.collection = db.jobs

    def run(self):
        self.driver.get(self.first_url)
        while True:
            # self.parse_page(self.driver.page_source)
            time.sleep(2)
            next_page_btn = self.driver.find_element_by_xpath("//a[contains(@class, 'next')]")
            if "disabled" in next_page_btn.get_attribute('class'):
                break
            else:
                print(next_page_btn.get_attribute('class'))
                next_page_btn.click()

    def parse_page(self, source):
        html = etree.HTML(source)
        detail_urls = html.xpath("//div[@class='info-primary']//a/@href")
        detail_urls = map(lambda url: self.base_domain + url, detail_urls)
        for detail_url in detail_urls:
            self.request_detail_page(detail_url)
            time.sleep(2)

    def request_detail_page(self, url):
        # 打开新窗口
        self.driver.execute_script("window.open('%s')" % url)
        # 切换到新窗口
        self.driver.switch_to.window(self.driver.window_handles[1])
        # 显式等待：找到就不会再等待
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.ID, "//div[@id='main']"))
        # )
        self.parse_detail_page(self.driver.page_source)
        # 关闭详情页面
        self.driver.close()
        # 切换到列表页
        self.driver.switch_to.window(self.driver.window_handles[0])

    def parse_detail_page(self, source):
        html = etree.HTML(source)
        job_name = html.xpath("//h1/text()")[0]
        salary = html.xpath("//span[@class='salary']/text()")[0].strip()
        city = html.xpath("//div[@class='info-primary']/p/text()")[0].strip()
        company = html.xpath("//a[@ka='job-detail-company']/@title")[0]
        job_desc_list = html.xpath("//div[@class='text']/text()")
        # 列表合并成一个字符串
        job_desc = "".join(job_desc_list).replace('\n', '').strip()
        job = {
            'job_name': job_name,
            'salary': salary,
            'city': city,
            'company': company,
            'job_desc': job_desc
        }
        self.jobs.append(job)
        self.to_mongodb(job)

    def to_mongodb(self, data):
        # 存储数据
        try:
            self.collection.insert(data)
            print('mongodb成功写入第%d条数据' % len(self.jobs))
        except:
            print('Insert Data Failed')


if __name__ == '__main__':
    spider = BossSpider()
    spider.run()
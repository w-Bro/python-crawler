# -*- coding: utf-8 -*-
import scrapy
import re
from soufangwang_spider.items import NewHouseItem, ESFHouseItem


class SoufangwangSpider(scrapy.Spider):
    name = "soufangwang"
    allowed_domains = ["fang.com"]
    start_urls = ['https://www.fang.com/SoufunFamily.htm']

    def parse(self, response):
        trs = response.xpath("//div[@class='outCont']//tr")
        province = None
        for tr in trs:
            # 没有class的td标签
            tds = tr.xpath(".//td[not(@class)]")
            province_td = tds[0]
            province_text = province_td.xpath(".//text()").get().strip()
            if province_text:
                province = province_text
            if province == '其它':
                continue

            city_td = tds[1]
            city_links = city_td.xpath(".//a")

            for city_link in city_links:
                city = city_link.xpath(".//text()").get()
                city_url = city_link.xpath(".//@href").get()
                # 构建新房的url
                url_module = city_url.split("//")
                scheme = url_module[0]
                domain = url_module[1]
                if 'bj.' in domain:
                    newhouse_url = 'http://newhouse.fang.com/house/s'
                    esf_url = 'https://esf.fang.com/house/i31/'
                else:
                    newhouse_url = scheme + "//" + "newhouse." + domain + "/house/s"
                    # 构建二手房
                    esf_url = scheme + "//" + "esf." + domain

                # meta传递参数给下一个函数用
                yield scrapy.Request(url=newhouse_url, callback=self.parse_newhouse, meta={"info": (province, city)})
                yield scrapy.Request(url=esf_url, callback=self.parse_esf, meta={"info": (province, city)})

    def parse_newhouse(self, response):
        # 取出参数
        province, city = response.meta.get('info')
        print(province, city)
        lis = response.xpath("//div[@class='nl_con clearfix']/ul//li")
        for li in lis:
            # 有一行广告，其不包含class=nlc_details的div标签
            if li.xpath(".//div[contains(@class, 'nlc_details')]"):
                name = li.xpath(".//div[@class='nlcd_name']/a/text()").get().strip()
                house_type_list = li.xpath(".//div[@class='house_type clearfix']/a/text()").getall()
                rooms = "/".join(list(map(lambda x: re.sub("\s", "", x), house_type_list)))
                area = li.xpath(".//div[@class='house_type clearfix']/text()").getall()
                area = "".join(list(map(lambda x: re.sub(r"/|－|\s", "", x), area)))
                address = li.xpath(".//div[@class='address']/a/@title").get()
                district_text = "".join(li.xpath(".//div[@class='address']/a//text()").getall())
                district = re.search(r".*\[(.+)\].*", district_text)
                if district is None:
                    district = ""
                else:
                    district = district.group(1)
                sale = li.xpath(".//div[@class='fangyuan']/span/text()").get()
                price = "".join(li.xpath(".//div[@class='nhouse_price']//text()").getall())
                price = re.sub(r"\s|广告", "", price)
                origin_url = 'http:' + li.xpath(".//div[@class='nlcd_name']/a/@href").get()

                item = NewHouseItem(name=name, rooms=rooms, area=area, address=address, district=district,
                                    sale=sale, price=price, origin_url=origin_url, province=province, city=city)
                yield item

        # 链接不包含/b9数字/，说明是第一页
        if "尾页" in response.xpath("//li[@class='fr']//text()").getall():
            if re.search(r'/b9(\d+)/', response.url):
                next_page = int(re.search(r'/b9(\d+)/', response.url).group(1)) + 1
                next_url = response.url.split("/b9")[0] + "/b9" + str(next_page) + "/"
            else:
                next_url = response.url + "/b92/"
            yield scrapy.Request(url=next_url, callback=self.parse_newhouse, meta={"info": (province, city)})

    def parse_esf(self, response):
        province, city = response.meta.get('info')
        dls = response.xpath("//div[@class='shop_list shop_list_4']/dl")
        for dl in dls:
            if dl.xpath(".//p[contains(@class, 'add_shop')]"):
                name = dl.xpath(".//p[@class='add_shop']/a/@title").get()
                address = dl.xpath(".//p[@class='add_shop']//span/text()").get()
                item = ESFHouseItem(province=province, city=city, name=name, address=address)
                infos = dl.xpath(".//p[@class='tel_shop']//text()").getall()
                infos = list(map(lambda x: re.sub(r"\s", "", x), infos))
                for info in infos:
                    if "厅" in info:
                        item['rooms'] = info
                    elif '层' in info:
                        item['floor'] = info
                    elif '向' in info:
                        item['toward'] = info
                    elif "年建" in info:
                        item['year'] = info.replace("年建", "")
                    elif "㎡" in info:
                        item['area'] = info
                item['price'] = dl.xpath(".//dd[@class='price_right']/span[1]/b/text()").get() + '万'
                item['unit'] = dl.xpath(".//dd[@class='price_right']/span[2]/text()").get()
                item['origin_url'] = response.urljoin(dl.xpath(".//h4[@class='clearfix']/a/@href").get())
                yield item

        if "下一页" == response.xpath("//div[@class='page_al']/p[last()-2]//text()").get():
            next_url = response.urljoin(response.xpath("//div[@class='page_al']/p[last()-2]/a/@href").get())
            yield scrapy.Request(url=next_url, callback=self.parse_esf, meta={"info": (province, city)})



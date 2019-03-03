import requests
from lxml import etree

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/71.0.3578.98 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Referer': 'https://hr.tencent.com/position.php?keywords=python^&lid=2218^&tid=0^&start=350',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9'
}
BASE_DOMAIN = 'https://hr.tencent.com/'


# 获取职位详情超链接
def get_detail_urls(url):
    response = requests.get(base_url.format(0), headers=headers)
    html = etree.HTML(response.text)
    detail_urls = html.xpath("//table[@class='tablelist']//tr[@class!='f']//a//@href")
    detail_urls = map(lambda url: BASE_DOMAIN+url, detail_urls)
    return detail_urls


def parse_detail_page(url):
    job_info = {}
    response = requests.get(url, headers=headers)
    html = etree.HTML(response.text)
    job_info['name'] = html.xpath("//td[@id='sharetitle']/text()")[0]
    job_info['loc'] = html.xpath("//tr[@class='c bottomline']//td/text()")[0]
    job_info['type'] = html.xpath("//tr[@class='c bottomline']//td/text()")[1]
    job_info['num'] = html.xpath("//tr[@class='c bottomline']//td/text()")[2]
    textElems = html.xpath("//tr[@class='c']//ul[@class='squareli']")
    # list合并成字符串
    job_info['duty'] = "".join(textElems[0].xpath(".//li/text()"))
    job_info['claim'] = "".join(textElems[1].xpath(".//li/text()"))
    return job_info


if __name__ == '__main__':
    base_url = 'https://hr.tencent.com/position.php?keywords=python&tid=0&start={}'
    # 步长为10
    job_infos = []
    for i in range(0, 550, 10):
        print("*"*30 + "\n正在爬取第{}页\n".format(int((i+10)/10)) + "*"*30)
        detail_urls = get_detail_urls(base_url.format(i))
        for detail_url in detail_urls:
            job_info = parse_detail_page(detail_url)
            job_infos.append(job_info)
            print("获得第{}条数据".format(len(job_infos)))

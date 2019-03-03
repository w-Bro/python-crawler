import requests
from lxml import etree
from urllib import request
import os
import re


def parse_page(url):
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'http://www.doutula.com/photo/list/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    response = requests.get(url, headers=headers)
    text = response.text
    html = etree.HTML(text)
    imgs = html.xpath("//div[@class='page-content text-center']//img[@class!='gif']")
    for img in imgs:
        img_url = img.get('data-original')
        alt = img.get('alt')
        alt = re.sub(r'[\?？\.，。！!]', '', alt)
        suffix = os.path.splitext(img_url)
        filename = alt + suffix[1].split('!')[0]
        request.urlretrieve(img_url, 'images/' + filename)


def main():
    for x in range(1, 11):
        url = 'http://www.doutula.com/photo/list/?page=%d' % x
        parse_page(url)


if __name__ == '__main__':
    main()


import requests
import re

poems = []


def parse_page(url):
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    response = requests.get(url, headers=headers)
    text = response.text
    # DOTALL：点可以匹配换行符
    titles = re.findall(r'<div class="cont">.*?<b>(.*?)</b>', text, re.DOTALL)
    dynasties = re.findall(r'<p class="source">.*?<a.*?>(.*?)</a>', text, re.DOTALL)
    authors = re.findall(r'<p class="source">.*?<a.*?>.*?<a.*?>(.*?)</a>', text, re.DOTALL)
    content_tags = re.findall(r'<div class="contson".*?>(.*?)</div>', text, re.DOTALL)
    contents = []
    for content in content_tags:
        # 替换空行标签
        content = re.sub(r'<.*?>', "", content).strip()
        contents.append(content)

    # a = [1, 2]
    # b = [3, 4]
    # c = zip(a, b)
    # c = [
    #     (1, 3),
    #     (2, 4)
    # ]
    for value in zip(titles, dynasties, authors, contents):
        title, dynasty, author, content = value
        poem = {
            'title': title,
            'dynasty': dynasty,
            'author': author,
            'content': content
        }
        poems.append(poem)


def main():
    for index in range(1, 11):
        url = 'https://www.gushiwen.org/default_{}.aspx'.format(index)
        parse_page(url)

    for poem in poems:
        print(poem)
        print('='*50)


if __name__ == '__main__':
    main()


import requests
from bs4 import BeautifulSoup
from pyecharts import Bar

ALL_DATA = []


def parse_page(url):
    headers = {
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'http://www.weather.com.cn/textFC/hz.shtml',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    response = requests.get(url, headers=headers)
    text = response.content.decode('utf-8')
    soup = BeautifulSoup(text, 'html5lib')
    # 找到第一个div
    conMidtab = soup.find('div', class_='conMidtab')
    tables = conMidtab.find_all('table')
    for table in tables:
        trs = table.find_all('tr')[2:]
        for index, tr in enumerate(trs):
            tds = tr.find_all('td')
            city_td = tds[0]
            if index == 0:
                city_td = tds[1]
            city = list(city_td.stripped_strings)[0]
            temp_td = tds[-2]
            min_temp = list(temp_td.stripped_strings)[0]
            ALL_DATA.append({'city': city, 'min_temp': int(min_temp)})


def main():
    areas = ['hb', 'db', 'hd', 'hz', 'hn', 'xb', 'xn', 'gat']
    base_url = 'http://www.weather.com.cn/textFC/{}.shtml'
    for area in areas:
        parse_page(base_url.format(area))

    # 排序
    ALL_DATA.sort(key=lambda data: data['min_temp'])

    # 可视化
    datas = ALL_DATA[:10]
    cities = list(map(lambda data: data['city'], datas))
    temps = list(map(lambda data: data['min_temp'], datas))
    chart = Bar("中国最低气温天气排行榜")
    chart.add('', cities, temps)
    chart.render("temperature.html")


if __name__ == '__main__':
    main()

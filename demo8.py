# urllib模块的API使用起来人人感觉不友好
# Requests更方便

import requests

# response = requests.get('https://www.baidu.com')
# # response.content与text的区别是没有解码
# print(response.text)
# print(response.content.decode('utf-8'))
# print(response.url)
# print(response.encoding)
# print(response.status_code)

parmas = {
    'wd': '中国'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/71.0.3578.98 Safari/537.36'
}
url = 'https://www.baidu.com/s'
response = requests.get(url, params=parmas, headers=headers)

with open('baidu.html', 'w', encoding='utf-8') as fp:
    fp.write(response.content.decode('utf-8'))
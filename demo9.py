
import requests

# POST请求
data = {
    'first': 'true',
    'pn': '1',
    'kd': 'python'
}
headers = {
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/71.0.3578.98 Safari/537.36'
}
response = requests.post('https://www.lagou.com/jobs/positionAjax.json?'
                         'city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false', data=data, headers=headers)
print(type(response.json()))


# 代理
# proxy = {
#     'http': '120.234.138.102:53779'
# }
# response = requests.get('http://httpbin.org/ip', proxies=proxy)
# print(response.text)

# Cookie
response = requests.get('http://www.baidu.com')
print(response.cookies.get_dict())

# session
data = {
        'email': '970138074@qq.com',
        'password': 'pythonspider'
    }
login_url = 'http://www.renren.com/PLogin.do'
url = 'http://renren.com/880151247/profile'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/71.0.3578.98 Safari/537.36'
}

# 如果想要在多次请求中多次共享cookie，应该使用session
session = requests.session()
session.post(login_url, data=data, headers=headers)
response = session.get(url)
with open('renren3.html', 'w', encoding='utf-8') as fp:
    fp.write(response.text)

# 处理不信任的SLL证书，加参数verify=false
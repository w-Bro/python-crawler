
from urllib import request
from http.cookiejar import CookieJar
from urllib import parse

headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit'
                                '/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    }

def get_opener():
    # 1. 登录
    # 1.1 创建一个cookiejar对象
    cookiejar = CookieJar()
    # 1.2 使用cookiejar创建一个HTTPCookieProcess对象
    handler = request.HTTPCookieProcessor(cookiejar)
    # 1.3 使用上一步创建的handler创建一个opener
    opener = request.build_opener(handler)
    # 1.4使用opener发送登录请求
    return opener


def login_renren(opener):
    data = {
        'email': '970138074@qq.com',
        'password': 'pythonspider'
    }

    login_url = 'http://www.renren.com/PLogin.do'
    req = request.Request(login_url, data=parse.urlencode(data).encode('utf-8'), headers=headers)
    opener.open(req)


def visit_profile(opener):
    # 2. 访问个人主页
    # 使用之前的opener，它已经包含登录所需的cookie信息，不要新建opener
    url = 'http://renren.com/880151247/profile'
    resp = opener.open(url)
    with open('renren2.html', 'w', encoding='utf-8') as fp:
        fp.write(resp.read().decode('utf-8'))


if __name__ == '__main__':
    opener = get_opener()
    login_renren(opener)
    visit_profile(opener)
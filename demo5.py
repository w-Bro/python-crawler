from urllib import request

url = 'http://renren.com/880151247/profile'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit'
                  '/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Cookie': 'Cookie: anonymid=jr94j31w-uyspjj; depovince=GW; _r01_=1; ick_login=6ef3fbde-832b-4a12-9d59-dd361ab7c839; t=c9440f261090e9ba8472c26b8ad861112; societyguester=c9440f261090e9ba8472c26b8ad861112; id=969532062; xnsid=857641ad; jebecookies=70182e9a-9e8c-4180-b1c7-796e33d2da39|||||; ver=7.0; loginfrom=null; wp_fold=0'
}

req = request.Request(url, headers=headers)
resp = request.urlopen(req)
with open('renren.html', 'w', encoding='utf-8') as fp:
    # write必须写入一个str的数据类型
    # resp.read()读出来是一个byte类型
    fp.write(resp.read().decode('utf-8'))
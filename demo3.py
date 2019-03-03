from urllib import request
from urllib import parse

# 不加请求头，使用urlopen
url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
#
# resp = request.urlopen(url)
# print(resp.read())

# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.'
#                          '3578.98 Safari/537.36'}
# req = request.Request(url, headers=headers)
# resp = request.urlopen(req)
# print(resp.read())

url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false'
data = {
    'first': 'true',
    'pn': 1,
    'kd': 'python'
}
# data 也需要进行编码
# TypeError: POST data should be bytes, an iterable of bytes, or a file object. It cannot be of type str.
# ('utf-8')
headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Length': '25',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': '_ga=GA1.2.1083537074.1547639998; user_trace_token=20190116195957-3e85e579-1986-11e9-b67a-5254005c3644; LGUID=20190116195957-3e85ea48-1986-11e9-b67a-5254005c3644; hasDeliver=0; index_location_city=%E5%B9%BF%E5%B7%9E; JSESSIONID=ABAAABAAAFCAAEGDA72C6299D4F3F0774D6A45756E752BB; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1547639999,1548216894; _gat=1; _gid=GA1.2.1717419192.1548216895; LGSID=20190123121451-6e25eb90-1ec5-11e9-930e-525400f775ce; PRE_UTM=; PRE_HOST=www.google.com.hk; PRE_SITE=https%3A%2F%2Fwww.google.com.hk%2F; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; _putrc=B2E7887F595BC8A0123F89F2B170EADC; login=true; unick=%E6%8B%89%E5%8B%BE%E7%94%A8%E6%88%B72429; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; gate_login_token=31feb16eae6128e0e624364b3e4367929aad2de42f3b61c9f7fc5920e6b3ed46; TG-TRACK-CODE=index_search; LGRID=20190123121456-7147d575-1ec5-11e9-930e-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1548216900; SEARCH_ID=32a008113e4d4ca99852901e39ffb745',
    'Host': 'www.lagou.com',
    'Origin': 'https://www.lagou.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'X-Anit-Forge-Code': '0',
    'X-Anit-Forge-Token': 'None',
    'X-Requested-With': 'XMLHttpRequest'
}
req = request.Request(url, headers=headers, data=parse.urlencode(data).encode('utf-8'), method='POST')
resp = request.urlopen(req)
print(resp.read().decode('utf-8'))
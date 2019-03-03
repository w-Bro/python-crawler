
from urllib import request
from urllib import parse
# resp = request.urlopen('http://www.baidu.com')
# print(resp.read())
# request.urlretrieve('http://www.baidu.com', 'baidu.html')

parmas = {'name': '张三', 'age': 18, "greet": "hello world"}
result = parse.urlencode(parmas)
print(result)
# 这样运行会报错，编码问题
# url = 'http://www.baidu.com/s?wd=刘德华'
# resp = request.urlopen(url)
# print(resp.read())

# url = 'http://www.baidu.com/s'
# parmas = {'wd': '刘德华'}
# qs = parse.urlencode(parmas)
# print(qs)
# url = url + '?' + qs;
# resp = request.urlopen(url)
# print(resp.read())

# 与parse.urlencode相反，解码
print(parse.parse_qs(result))
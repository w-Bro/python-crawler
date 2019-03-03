from urllib import parse

# 锚点#1
url = 'http://www.baidu.com/s?wd=python&username=abc#1'

# 对url的各个组成部分进行分割
# urlparse和urlsplit的区别只在于没有params
result1 = parse.urlparse(url)
result2 = parse.urlsplit(url)
print(result1)
print(result2)
# print('scheme:', result.scheme)
# print('netloc:', result.netloc)
# print('params:', result.params)
# print('query:', result.query)
# print('path:', result.path)
# print('fragment:', result.fragment)


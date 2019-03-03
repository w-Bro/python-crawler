from urllib import request

# 代理，参数格式是字典
# handler = request.ProxyHandler({"http": '218.66.161.88:31769'})
#
# opener = request.build_opener(handler)
# req = request.Request("http://httpbin.org/ip")
# resp = opener.open(req)
# print(resp.read())

# 常用的代理
# 西利免费代理ip:http://www.cilidaili.com
# 快代理:http://www.kuaidaili.com/
# 代理云：http://www.dailiyun.com

# 未使用代理
url = 'http://httpbin.org/ip'
# resp = request.urlopen(url)
# print(resp.read())

# 使用代理(urlopen执行的步骤也是如下3步)
handler = request.ProxyHandler({"http": '110.52.235.62:9999'})
opener = request.build_opener(handler)
resp = opener.open(url)
print(resp.read())
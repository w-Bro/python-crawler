
from urllib import request
from http.cookiejar import MozillaCookieJar

# 保存cookie到本地
cookiejar = MozillaCookieJar('cookie.txt')
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)

resp = opener.open('http://httpbin.org/cookies/set?course=spider')

# 把即将过期的cookie信息保存下来
cookiejar.save(ignore_discard=True)

# 加载本地cookie信息
cookiejar.load(ignore_discard=True)
for cookie in cookiejar:
    print(cookie)
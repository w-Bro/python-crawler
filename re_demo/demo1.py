import re

# # 1. 匹配某个字符串
# text = "hello"
# ret = re.match('he', text)
# print(ret.group())
# text = "ahello"
# ret = re.search('he', text)
# print(ret.group())
#
# # 2. 点：匹配任意字符,不能匹配换行符
# text = "hello"
# ret = re.match('.', text)
# print(ret.group())
#
# # 3. \d：匹配任意数字
# text = "45"
# ret = re.match('\d', text)
# print(ret.group())
#
# # 4. \D：匹配任意的非数字
# text = "+"
# ret = re.match('\D', text)
# print(ret.group())
#
# # 5. \s：匹配空白字符(\n, \t, \r, 空格)
# text = "\n"
# ret = re.match('\s', text)
# print(ret.group())
#
# # 6. \w：匹配a-z, A-Z, 下划线， 数字
# text = "a15"
# ret = re.match('\w', text)
# print(ret.group())
#
# # 7. \W：与\w相反
# text = "+"
# ret = re.match('\W', text)
# print(ret.group())

# 8. []组合的方式，只要满足中括号中的字符，就可以匹配
# text = "0731-88888888"
# ret = re.match('[\d-]+', text)
# print(ret.group())
# 8.1 []的形式代替\d:[0-9]
# 8.2 []的形式代替\D:[^0-9]
# 8.2 []的形式代替\w:[a-zA-Z0-9_]
# 8.3 []的形式代替\W:[^a-zA-Z0-9_]

# 9. *：匹配0或任意多个字符
# text = "0731"
# ret = re.match('\d*', text)
# print(ret.group())

# 10. +：匹配1个或多个字符
# text = "abcd"
# ret = re.match('\w+', text)
# print(ret.group())

# 11. ?：匹配一个或0个（要么没有，要么一个）
# text = "abcd"
# ret = re.match('\w?', text)
# print(ret.group())

# 12.{m}：匹配m个字符
# text = "abcd"
# ret = re.match('\w{2}', text)
# print(ret.group())

# 13.{m,n}：匹配m-n个字符
# text = "abcd"
# ret = re.match('\w{1,2}', text)
# print(ret.group())

# 14. 验证手机号码
# text = "18578788123"
# ret = re.match('1[34578]\d{9}', text)
# print(ret.group())

# 15. 验证邮箱:
# text = "fsdfsdf15_ds@qq.com"
# ret = re.match('\w+@[0-9a-z]+\.[a-z]+', text)
# print(ret.group())

# 16. 验证URL：
# text = "https://baidu.com/s/ssss/ss"
# ret = re.match('(http|https|ftp)://[^\s]+', text)
# print(ret.group())

# 17. 验证身份证:
# text = "12345678123456789X"
# ret = re.match('\d{17}[\dxX]', text)
# print(ret.group())

# 18. ^(脱字号): 表示以...开始，在中括号中表示取反操作
# match函数是从第一个字符开始匹配，用不用无所谓，用search函数
# text = "hello"
# ret = re.search('^h', text)
# print(ret.group())

# 19. $：表示以...结尾
# text = "xxx@163.com"
# ret = re.match('\w+@163.com$', text)
# print(ret.group())

# 20. |：匹配多个字符串或者表达式
# text = "http"
# ret = re.search('http|https|ftp', text)
# print(ret.group())

# 21. 贪婪模式与非贪婪模式：
# text = "<h1>标题</h1>"
# ret = re.search('<.+>', text)
# print('贪婪模式：' + ret.group())
#
# ret = re.search('<.+?>', text)
# print('非贪婪模式： ' + ret.group())

# 22. 匹配0-100之间的数字
# 可以出现的：1 2 3 10 100
# 不可以出现的：09 101
# text = "10"
# ret = re.match('0$|[1-9]\d?$|100$', text)
# print(ret.group())

# 23. 转义字符\
# text = "apple price is $299"
# ret = re.search('\$\d+', text)
# print(ret.group())

# 24. 原生字符串：r = raw = 原生的
# text = "\\n"
# text = r'\n'
# print(text)

text = "\c"
# ret = re.match('\\\\c', text)
ret = re.match(r'\\c', text)
print(ret.group())
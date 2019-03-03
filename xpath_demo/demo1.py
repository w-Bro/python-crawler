
from lxml import etree

# 构造解析器
parser = etree.HTMLParser(encoding='utf-8')
html = etree.parse("tencent.html", parser=parser)

# 1. 获取所有tr标签
# //tr
# xpath函数返回的是列表
# trs = html.xpath("//tr")
# for tr in trs:
#     print(etree.tostring(tr, encoding='utf-8').decode('utf-8'))

# 2. 获取第二个tr标签
# tr = html.xpath("//tr[2]")[0]
# print(etree.tostring(tr, encoding='utf-8').decode('utf-8'))

# 3. 获取所有class等于even的标签
# trs = html.xpath("//tr[@class='even']")
# for tr in trs:
#     print(etree.tostring(tr, encoding='utf-8').decode('utf-8'))

# 4. 获取所有a标签的href属性
# //a[@href]是获取所有拥有href属性的a标签
# //a/@href是a标签的href值
# aList = html.xpath("//a/@href")
# for a in aList:
#     print(a)

# 5. 获取所有职位信息纯文本
trs = html.xpath("//tr")
for tr in trs:
    # 只在当前标签下查找
    href = tr.xpath(".//a/@href")[0]
    full_url = 'hr.tencent.com/' + href
    title = tr.xpath(".//td//text()")
    print(title)
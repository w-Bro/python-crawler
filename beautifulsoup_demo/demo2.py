
from bs4 import BeautifulSoup

html = """
<table class="tablelist" cellpadding="0" cellspacing="0">
		    	<tbody><tr class="h">
		    		<td class="l" width="374">职位名称</td>
		    		<td>职位类别</td>
		    		<td>人数</td>
		    		<td>地点</td>
		    		<td>发布时间</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47423&amp;keywords=&amp;tid=0&amp;lid=0">TEG02-网络运维工程师</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-02-01</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47424&amp;keywords=&amp;tid=0&amp;lid=0">29310-智慧零售高级产品策划经理（深圳）</a></td>
					<td>产品/项目类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-02-01</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47426&amp;keywords=&amp;tid=0&amp;lid=0">30622-腾讯广告Q系流量商业化产品经理（深圳）</a></td>
					<td>产品/项目类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-02-01</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47417&amp;keywords=&amp;tid=0&amp;lid=0">26563-平台内容运营</a></td>
					<td>产品/项目类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-02-01</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47418&amp;keywords=&amp;tid=0&amp;lid=0">26563-游戏平台（WeGame）产品策划</a></td>
					<td>产品/项目类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-02-01</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47419&amp;keywords=&amp;tid=0&amp;lid=0">27092-用户增长后台开发工程师（深圳）</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-02-01</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47420&amp;keywords=&amp;tid=0&amp;lid=0">TME-全民K歌Android开发工程师</a></td>
					<td>技术类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-02-01</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47421&amp;keywords=&amp;tid=0&amp;lid=0">23671-企鹅号Howto品类产品运营（深圳）</a></td>
					<td>产品/项目类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-02-01</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47422&amp;keywords=&amp;tid=0&amp;lid=0">30616-投资者关系</a></td>
					<td>职能类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2019-02-01</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47411&amp;keywords=&amp;tid=0&amp;lid=0">22989-腾讯云资深运营开发工程师（深圳）</a></td>
					<td>技术类</td>
					<td>2</td>
					<td>深圳</td>
					<td>2019-02-01</td>
		    	</tr>
		    </tbody></table>
"""


# lxml为解析器，其他的解析器有："html.parser"、{"lxml", "xml"}、html5lib(最好的容错性,pip install html5lib)
soup = BeautifulSoup(html, "lxml")
# print(soup.prettify())

# css选择器


# 1. 获取所有tr标签
# trs = soup.select('tr')
# for tr in trs:
#     print(tr)

# 2. 获取第2个tr标签
# tr = soup.select('tr')[1]
# print(tr)

# 3. 获取所有class等于even的tr标签
# trs = soup.select("tr.even")
# for tr in trs:
#     print(tr)

# 4. 将所有id等于test,class也等于test的a标签提取出来
# css选择器实现不了

# 5. 获取所有a标签的href属性
# aList = soup.select('a')
# for a in aList:
#     # 1. 通过下标的方式
#     href = a['href']
#     # 2. 通过attrs属性的方式
#     # href = a.attrs['href']
#     print(href)
# 6. 获取所有职位信息（纯文本）
trs = soup.select('tr')[1:]
for tr in trs:
    infos = list(tr.stripped_strings)
    print(infos)

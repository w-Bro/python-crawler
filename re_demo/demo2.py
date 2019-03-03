import re

# 分组
text = "apple's price is $29, orange's price is $10"
ret = re.search('.*(\$\d+).*(\$\d+)', text)
print(ret.group())
print(ret.group(1))
print(ret.group(2))
print(ret.group(1, 2))
print(ret.groups())

# 返回所有满足条件的列表
ret = re.findall('\$\d+', text)
print(ret)

# 替换
ret = re.sub('\$\d+', "0", text)
print(ret)

html = """
<dd class="job_bt">
        <h3 class="description">职位描述：</h3>
        <div class="job-detail">
        <p>1、负责管理后台的开发，参与项目的编程、调试和模块测试工作；</p>
<p>2、根据项目需求，能够独立按时完成网站开发任务；</p>
<p>3、对相关部门提交的BUG进行分析测试，并作出修改；</p>
<p>4、构建与开发公司内部平台系统。</p>
<p><br></p>
<p><br></p>
<p>岗位要求：</p>
<p>1、大专及以上学历，计算机相关专业；</p>
<p>2、两年以上工作经验，熟悉django flask web.py等相关web框架；</p>
<p>3、熟悉jquery等前端框架；</p>
<p>4、熟悉css html等相关知识；</p>
<p>5、有游戏管理后台开发经验优先。</p>
        </div>
    </dd>
"""
ret = re.sub('<.+?>', '', html)
print(ret)

text = "hello world 你 好"
ret = re.split(' ', text)
print(ret)

# compile效率比较高,可以加注释
text = "the number is 20.50"
# r = re.compile('\d+\.?\d*')
r = re.compile(r"""
            \d+ # 小数点前面的数字
            \.? # 小数点本身
            \d* # 小数点后面的数字
""", re.VERBOSE)
ret = re.search(r, text)
print(ret.group())
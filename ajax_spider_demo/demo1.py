from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()



# 关闭当前页面
# driver.close()
#
# # 退出整个浏览器
# driver.quit()

# inputTag = driver.find_element_by_id('kw')
# inputTag = driver.find_element_by_name('wd')
# inputTag = driver.find_element_by_xpath("//input[@id='kw']")
# inputTag = driver.find_element_by_css_selector(".quickdelete-wrap > input")
# inputTag = driver.find_elements(By.CSS_SELECTOR, ".quickdelete-wrap > input")[0]
# inputTag.send_keys('python')

# 常见的表单元素：input type='text/password/email/number'
# button、input type='submit'
# checkbox: input='checkbox'
# select: 下拉列表

# driver.get('https://www.baidu.com/')
# inputTag = driver.find_element_by_id('kw')
# inputTag.send_keys('python')
# time.sleep(3)
# inputTag.clear()

# driver.get('https://www.douban.com/')
# rememberBtn = driver.find_element_by_name('remember')
# rememberBtn.click()

driver.get('https://www.baidu.com/')
inputTag = driver.find_element_by_id('kw')
inputTag.send_keys('python')
submitTag = driver.find_element_by_id('su')
submitTag.click()
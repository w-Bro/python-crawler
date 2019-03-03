# 鼠标行为链

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.get('https://www.baidu.com')

inputTag = driver.find_element_by_id('kw')
submitBtn = driver.find_element_by_id('su')

actions = ActionChains(driver)
actions.move_to_element(inputTag)
actions.send_keys_to_element(inputTag, 'python')
actions.move_to_element(submitBtn)
actions.click(submitBtn)
actions.perform()

# click_and_hold(element): 点击但不松开鼠标
# context_click(element): 右键点击
# double_click(element): 双击

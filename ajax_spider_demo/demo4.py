# 页面等待
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common .by import By

driver = webdriver.Chrome()

driver.get('https://www.douban.com')

# 隐式等待：等待10秒，不管找没找到都是等待10秒
# driver.implicitly_wait(10)
# driver.find_element_by_id('fsedfsdfsfsdfs')


# 显式等待：10秒内找到就不会再等待
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'DFASDASDAS'))
)

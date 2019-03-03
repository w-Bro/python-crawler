# 代理IP
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://114.235.22.156:9000")
driver = webdriver.Chrome(chrome_options=options)

driver.get('http://www.httpbin.org/ip')
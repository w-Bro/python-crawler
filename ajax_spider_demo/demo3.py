from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.baidu.com')

for cookie in driver.get_cookies():
    print(cookie)

print('=' * 30)

driver.delete_cookie("PSTM")
print('=' * 30)

print(driver.get_cookie("PSTM"))
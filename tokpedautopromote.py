from selenium import webdriver
# from selenium.webdriver.common.by import By
import urllib

email = ""
pwd = ""

option = webdriver.ChromeOptions()

# driver = webdriver.Chrome(chrome_options=option)
driver = webdriver.Chrome("/Users/harjiwigaasmoko/Projects/selenium/chromedriver")
# executor_url = driver.command_executor._url
# session_id = driver.session_id
driver.implicitly_wait(20)
# driver.get("https://tokopedia.com/")
driver.get("https://www.tokopedia.com/login?theme=iframe&p=https%3A%2F%2Fwww.tokopedia.com%2F&t=1542558862754")
# driver.find_element_by_id('login-ddl-link').click()
# driver.find_element_by_id('iframe-login')
username = driver.find_element_by_id("inputEmail")
password = driver.find_element_by_id("inputPassword")
username.send_keys("harjiark@gmail.com")
password.send_keys("HAR7a55sppwjiwi")

driver.find_element_by_id('global_login_btn').click()
driver.get("https://www.tokopedia.com/oleholeholih/getuk-goreng")
driver.find_element_by_id('dink-it').click()
text = driver.find_element_by_css_selector(".p-4.pb-10.pt-0").text

print(text)
# print(executor_url)
# print(session_id)
driver.implicitly_wait(20)
driver.close()
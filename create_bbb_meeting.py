from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://bbb.tu-dresden.de/b/")
time.sleep(10)
driver.find_element_by_xpath('//a[@href="/b/signin"]').click()
time.sleep(10)
element = driver.find_element_by_xpath('//input[@id="session_username"]').send_keys("rish338a")
driver.find_element_by_id("session_password").send_keys("rI/4srivast")
driver.find_element_by_xpath('//input[@value="Sign in"]').click()
time.sleep(10)
driver.find_element_by_xpath('//input[@value="Start"]').click()
time.sleep(10)
driver.find_element_by_xpath("//button[@aria-label='Listen only']").click()


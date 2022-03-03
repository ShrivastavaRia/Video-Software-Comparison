from operator import ge
from selenium import webdriver
import time
import pathlib
import platform


def get_chromedriver_location():
    return str(pathlib.Path(__file__).parent.resolve() / "chromedriver-") + str(
        platform.system()
    )

def create_meeting(timeout):
    driver = webdriver.Chrome(executable_path=get_chromedriver_location())
    # driver.get("https://bbb.tu-dresden.de/b/")
    driver.get("https://demo.bigbluebutton.org/gl")
    time.sleep(10)
    driver.find_element_by_xpath('//a[@href="/gl/signin"]').click()
    # driver.find_element_by_xpath('//a[@href="/b/signin"]').click()
    time.sleep(10)
    element = driver.find_element_by_xpath('//input[@id="session_email"]').send_keys(
        "riashrivastava4996@gmail.com"
    )
    driver.find_element_by_id("session_password").send_keys("7u*ezxY&W%BGfNj")
    # element = driver.find_element_by_xpath('//input[@id="session_username"]').send_keys("rish338a")
    # driver.find_element_by_id("session_password").send_keys("rI/4srivast")
    driver.find_element_by_xpath('//input[@value="Sign in"]').click()
    time.sleep(10)
    driver.find_element_by_xpath('//input[@value="Start"]').click()
    time.sleep(10)
    driver.find_element_by_xpath("//button[@aria-label='Listen only']").click()
    time.sleep(timeout)
    driver.quit()

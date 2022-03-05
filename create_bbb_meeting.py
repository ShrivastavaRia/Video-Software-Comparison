from operator import ge
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pathlib
import platform


def get_chromedriver_location():
    return str(pathlib.Path(__file__).parent.resolve() / "chromedriver-") + str(
        platform.system()
    )

def create_meeting(timeout):
    opt = Options()
    opt.add_argument("--disable-infobars")
    opt.add_argument("start-maximized")
    opt.add_argument("--disable-extensions")
    # Pass the argument 1 to allow and 2 to block
    opt.add_experimental_option(
        "prefs",
        {
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 1,
            "profile.default_content_setting_values.geolocation": 1,
            "profile.default_content_setting_values.notifications": 1,
        },
    )
    driver = webdriver.Chrome(chrome_options=opt, executable_path=get_chromedriver_location())
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
    i = 0
    retry_total = 5
    while i < retry_total:
        i = i + 1
        time.sleep(5)
        try:
            driver.find_element_by_xpath('//input[@value="Sign in"]').click()
            break
        except Exception as e:
            pass
    time.sleep(10)
    driver.find_element_by_xpath('//input[@value="Start"]').click()
    time.sleep(10)
    driver.find_element_by_xpath("//button[@aria-label='Listen only']").click()
    time.sleep(5)

    made_user_presenter = False
    while True or not made_user_presenter:
        try:
            driver.find_element_by_xpath('//span[text()="test123"]').click()
            time.sleep(5)
            driver.find_element_by_xpath('//div[text()="Make presenter"]').click()
            made_user_presenter = True
            time.sleep(5)
        except Exception as e:
            print(e)
            pass

    time.sleep(timeout)
    driver.quit()

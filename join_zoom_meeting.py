from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

from measure_rapl_counters import make_measurements
from get_zoom_link_from_db import get_link
import pyautogui
from get_chromedriver import get_chromedriver_location


def measure_join_meeting(measurement_file_prefix):
    opt = Options()
    opt.add_argument("--disable-infobars")
    opt.add_argument("----disable-default-apps")
    opt.add_argument("start-maximized")
    opt.add_argument("--disable-dev-shm-usage")
    # Pass the argument 1 to allow and 2 to block
    opt.add_experimental_option(
        "prefs",
        {
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 1,
            "profile.default_content_setting_values.geolocation": 1,
            "profile.default_content_setting_values.notifications": 0,
        },
    )

    driver = webdriver.Chrome(
        chrome_options=opt, executable_path=get_chromedriver_location()
    )
    driver.get(get_link())    

    # Maximize the window and let code stall
    # for 10s to properly maximise the window.
    time.sleep(10)
    pyautogui.press('enter')
    time.sleep(5)
    driver.find_element_by_xpath('//div[text()="Launch Meeting"]').click()
    time.sleep(10)
    pyautogui.press('enter')
    time.sleep(5)
    driver.find_element_by_xpath('//a[text()="Join from Your Browser"]').click()
    time.sleep(10)
    driver.find_element_by_id("inputname").send_keys("TestUser1")
    driver.find_element_by_id("joinBtn").click()
    time.sleep(10)
    driver.find_element_by_id('wc_agree1').click()
    time.sleep(10)
    make_measurements(filename=measurement_file_prefix)
    driver.quit()

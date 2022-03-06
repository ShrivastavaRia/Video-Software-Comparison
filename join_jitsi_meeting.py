from ast import expr_context
from selenium import webdriver
import pyautogui
import time
from room_name import ROOM_NAME
from get_chromedriver import get_chromedriver_location
from measure_rapl_counters import make_measurements
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def measure_join_meeting(measurement_file_prefix, is_share=False):
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option(
        "prefs",
        {
            "profile.default_content_setting_values.media_stream_mic": 1,
            "profile.default_content_setting_values.media_stream_camera": 1,
            "profile.default_content_setting_values.geolocation": 1,
            "profile.default_content_setting_values.notifications": 0,
        },
    )
    opt.add_argument("--use-fake-device-for-media-stream")
    opt.add_argument('--auto-select-desktop-capture-source="Entire screen"')
    opt.add_argument("--start-maximized")
    driver = webdriver.Chrome(
        options=opt, executable_path=get_chromedriver_location()
    )
    driver.get("https://jitsi.tu-dresden.de/{}".format(ROOM_NAME))
    time.sleep(10)
    driver.find_element_by_xpath('//div[@class="prejoin-input-area"]//input').send_keys(
        "TestUser"
    )
    driver.find_element_by_xpath('//div[@data-testid="prejoin.joinMeeting"]').click()
    time.sleep(10)

    if is_share:
        for _ in range(0,10):
            pyautogui.press('tab')
        time.sleep(2)
        element = driver.find_element_by_xpath('//div[@aria-label="Toggle screenshare"]')
        element.click()
        time.sleep(10)
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("enter")
    make_measurements(filename=measurement_file_prefix)
    driver.quit()
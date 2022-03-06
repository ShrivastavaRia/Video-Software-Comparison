from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

from measure_rapl_counters import make_measurements
from get_zoom_link_from_db import get_link
import pyautogui
from get_chromedriver import get_chromedriver_location


def measure_join_meeting(measurement_file_prefix, is_share=False, launch_in_app=False):
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
    if not launch_in_app:
        opt.add_argument("--disable-default-apps")
    opt.add_argument("--use-fake-device-for-media-stream")
    opt.add_argument('--auto-select-desktop-capture-source="Entire screen"')
    opt.add_argument("--start-maximized")

    
    driver = webdriver.Chrome(
        options=opt, executable_path=get_chromedriver_location()
    )
    join_link = get_link()
    if not launch_in_app:
        # Transform link to a web browser based link
        join_link = join_link.split("j/")
        join_link = join_link[0] + "wc/" + "join/" + join_link[1]
    # logic to launch in app
    driver.get(join_link)
    time.sleep(10)
    if launch_in_app:
        pass
    else:
        try:
            driver.find_element_by_xpath('//button[text()="Accept Cookies"]').click()
        except Exception as e:
            print("cookie window for zoom not found, continuing")
        driver.find_element_by_id("inputname").send_keys("TestUser1")
        time.sleep(10)
        driver.find_element_by_id("joinBtn").click()
        time.sleep(10)
        driver.find_element_by_id('wc_agree1').click()
        time.sleep(10)
        if is_share:
            driver.find_element_by_xpath("//*[contains(@class, 'sharing-entry-button-container--green')]").click()
            time.sleep(10)
            pyautogui.press("tab")
            pyautogui.press("tab")
            pyautogui.press("tab")
            pyautogui.press("tab")
            pyautogui.press("enter")
            time.sleep(10)
    make_measurements(filename=measurement_file_prefix)
    driver.quit()
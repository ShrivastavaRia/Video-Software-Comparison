from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui
import time

from measure_rapl_counters import make_measurements

from get_chromedriver import get_chromedriver_location


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
    driver.get("https://demo.bigbluebutton.org/gl/ria-whs-kwa-vw6")
    time.sleep(10)

    # Obtain button by link text and click.
    driver.find_element_by_id("_gl_ria-whs-kwa-vw6_join_name").send_keys("test123")
    driver.find_element_by_id("room-join").click()
    time.sleep(15)
    driver.find_element_by_xpath("//button[@aria-label='Microphone']").click()
    time.sleep(15)
    try:
        driver.find_element_by_xpath('//i[contains(@class,"icon-bbb-thumbs_up")]').click()
    
    except Exception as e:
        pass
    time.sleep(10)
    driver.find_element_by_xpath('//button[@aria-label="Share webcam"]').click()
    # for i in range(25):
    #     pyautogui.press('tab')
    # time.sleep(1)
    # pyautogui.press('enter')
    # time.sleep(5)
    time.sleep(10)
    driver.find_element_by_xpath('//button[@aria-label="Start sharing"]').click()
    time.sleep(10)
    if is_share:
        driver.find_element_by_xpath('//button[@aria-label="Share your screen"]').click()
        time.sleep(10)
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("enter")
    make_measurements(filename=measurement_file_prefix)
    driver.quit()
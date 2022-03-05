from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pathlib
import platform
import time
from room_name import ROOM_NAME


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
    chromedriver_location = get_chromedriver_location()
    print(chromedriver_location)
    driver = webdriver.Chrome(
        chrome_options=opt, executable_path=get_chromedriver_location()
    )
    driver.get("https://jitsi.tu-dresden.de/")
    time.sleep(10)
    driver.find_element_by_id("enter_room_field").send_keys(ROOM_NAME)
    driver.find_element_by_id("enter_room_button").click()
    time.sleep(10)
    driver.find_element_by_xpath('//div[@class="prejoin-input-area"]//input').send_keys(
        "Ria"
    )
    driver.find_element_by_xpath('//div[@data-testid="prejoin.joinMeeting"]').click()
    time.sleep(10)
    driver.find_element_by_xpath('//span[text()="I am the host"]').click()
    driver.find_element_by_xpath('//input[@name="username"]').send_keys("rish338a")
    driver.find_element_by_xpath('//input[@name="password"]').send_keys("rI/4srivast")
    driver.find_element_by_id("modal-dialog-ok-button").click()
    time.sleep(timeout)
    driver.quit()

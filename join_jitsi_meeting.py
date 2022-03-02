import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from room_name import ROOM_NAME
from get_chromedriver import get_chromedriver_location
from measure_rapl_counters import make_measurements



def measure_join_meeting(measurement_file_prefix):
  opt = Options()
  opt.add_argument("--disable-infobars")
  opt.add_argument("start-maximized")
  opt.add_argument('--disable-dev-shm-usage')
  # Pass the argument 1 to allow and 2 to block
  opt.add_experimental_option("prefs", { \
      "profile.default_content_setting_values.media_stream_mic": 1, 
      "profile.default_content_setting_values.media_stream_camera": 1,
      "profile.default_content_setting_values.geolocation": 1, 
      "profile.default_content_setting_values.notifications": 1 
    })

  driver = webdriver.Chrome(chrome_options= opt, executable_path=get_chromedriver_location())
  driver.get("https://jitsi.tu-dresden.de/{}".format(ROOM_NAME))
  time.sleep(10)
  driver.find_element_by_xpath('//div[@class="prejoin-input-area"]//input').send_keys("TestUser")
  driver.find_element_by_xpath('//div[@data-testid="prejoin.joinMeeting"]').click()
  time.sleep(10)
  did_measurement_succeed = make_measurements(filename=measurement_file_prefix)
  # Make measurements for specified seconds[csv values for powerstat, total energy consumed, average wattage] over n iterations[100 iterations of one minute each]
  driver.quit()
  return did_measurement_succeed

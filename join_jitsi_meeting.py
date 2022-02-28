import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyRAPL
pyRAPL.setup()
import time
from room_name import ROOM_NAME
from get_chromedriver import get_chromedriver_location




def join_meeting(duration_of_measurement):
  report = pyRAPL.outputs.CSVOutput("jitsi-output" + str(datetime.datetime.now()), append=False)
  opt = Options()
  opt.add_argument("--disable-infobars")
  opt.add_argument("start-maximized")
  opt.add_argument("--disable-extensions")
  # Pass the argument 1 to allow and 2 to block
  opt.add_experimental_option("prefs", { \
      "profile.default_content_setting_values.media_stream_mic": 1, 
      "profile.default_content_setting_values.media_stream_camera": 1,
      "profile.default_content_setting_values.geolocation": 1, 
      "profile.default_content_setting_values.notifications": 1 
    })

  driver = webdriver.Chrome(chrome_options= opt, executable_path=get_chromedriver_location())

  with pyRAPL.Measurement("JitsiPerformance", output=report):
    driver.get("https://jitsi.tu-dresden.de/{}".format(ROOM_NAME))
    time.sleep(10)
    driver.find_element_by_xpath('//div[@class="prejoin-input-area"]//input').send_keys("TestUser")
    driver.find_element_by_xpath('//div[@data-testid="prejoin.joinMeeting"]').click()
    time.sleep(duration_of_measurement)
    driver.quit()
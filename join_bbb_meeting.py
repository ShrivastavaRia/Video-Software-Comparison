# import module
from selenium import webdriver

import pyRAPL
import time

desired_cap = {
  'browser_version': '75.0',
  'os': 'Windows',
  'os_version': '10',

  #Configure ChromeOptions to pass fake media stream
  'chromeOptions': {
    'args': ["--use-fake-device-for-media-stream", "--use-fake-ui-for-media-stream"]
  }
}
  
# Create the webdriver object. Here the 
# chromedriver is present in the driver 
# folder of the root directory.
driver = webdriver.Chrome(executable_path='chromedriver.exe', desired_capabilities=desired_cap)
#pyRAPL.setup()
#meter = pyRAPL.Measurement('bar')
# get https://www.geeksforgeeks.org/
driver.get("https://bbb.tu-dresden.de/b/ria-aaf-apw-p1p/")
  
# Maximize the window and let code stall 
# for 10s to properly maximise the window.
time.sleep(10)
  
# Obtain button by link text and click.
driver.find_element_by_id('_b_ria-aaf-apw-p1p_join_name').send_keys("User1")
driver.find_element_by_id('room-join').click()
time.sleep(20)
driver.find_element_by_xpath("//button[@aria-label='Listen only']").click()

#meter.begin()
time.sleep(100)
#meter.end()
driver.quit()

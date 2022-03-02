from selenium import webdriver
import time

from measure_rapl_counters import make_measurements

from get_chromedriver import get_chromedriver_location


def measure_join_meeting(measurement_file_prefix):
    desired_cap = {
        "browser_version": "75.0",
        "os": "Windows",
        "os_version": "10",
        "chromeOptions": {
            "args": [
                "--use-fake-device-for-media-stream",
                "--use-fake-ui-for-media-stream",
            ]
        },
    }
    driver = webdriver.Chrome(
        executable_path=get_chromedriver_location(), desired_capabilities=desired_cap
    )
    # pyRAPL.setup()
    # meter = pyRAPL.Measurement('bar')
    # get https://www.geeksforgeeks.org/
    driver.get("https://demo.bigbluebutton.org/gl/ria-whs-kwa-vw6")

    # Maximize the window and let code stall
    # for 10s to properly maximise the window.
    time.sleep(10)

    # Obtain button by link text and click.
    driver.find_element_by_id("_gl_ria-whs-kwa-vw6_join_name").send_keys("User1")
    driver.find_element_by_id("room-join").click()
    time.sleep(10)
    driver.find_element_by_xpath("//button[@aria-label='Listen only']").click()
    make_measurements(filename=measurement_file_prefix)
    driver.quit()

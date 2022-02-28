import pathlib
import platform

def get_chromedriver_location():
  return str(pathlib.Path(__file__).parent.resolve() /  "chromedriver-") + str(platform.system())
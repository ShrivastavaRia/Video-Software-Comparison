import pathlib
import platform


def get_chromedriver_location():
    path = str(pathlib.Path(__file__).parent.resolve() / "chromedriver-") + str(
        platform.system()
    )
    
    return path

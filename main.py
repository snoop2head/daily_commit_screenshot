# This one gets all table data text
import re
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from PIL import Image
from io import BytesIO
from datetime import date


def get_github_screenshot(github_user_id: str):
    """
    get screenshot for github daily commit progress
    """

    # chrome driver options: headless, mobile responsive emulation
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    mobile_emulation = {"deviceName": "iPhone X"}
    options.add_experimental_option("mobileEmulation", mobile_emulation)

    # set chromedriver path with options
    driver = webdriver.Chrome("./chromedriver", options=options)

    # open url link with driver
    url = f"https://github.com/{github_user_id}"
    driver.get(url)
    time.sleep(2)

    # set today's date as variable
    today = date.today()
    today_date = str(today)

    # select elements on github page for the screenshot
    github_panel_wrapper = driver.find_element_by_class_name("js-yearly-contributions")
    comitted_day = driver.find_element_by_css_selector(f'[data-date="{today_date}"]')

    # scroll for selected element for screenshot
    driver.execute_script("arguments[0].scrollIntoView();", github_panel_wrapper)
    driver.execute_script("window.scrollBy(0, -50)")

    # select today's github commit tile icon
    comitted_day.click()
    time.sleep(2)

    driver.save_screenshot(f"./img/{today_date}_github.png")
    driver.quit()

    # crop images to highlight commit information
    im = Image.open(
        f"./img/{today_date}_github.png"
    )  # uses PIL library to open image in memory

    w, h = im.size
    reducing_pix_top = 130
    reducing_pix_bottom = 220
    im.crop((0, reducing_pix_top, w, h - reducing_pix_bottom)).save(
        f"./img/{today_date}_github.png"
    )  # saves new cropped image


def main():
    """
    designate functions for main
    """
    get_github_screenshot("snoop2head")


if __name__ == "__main__":
    main()

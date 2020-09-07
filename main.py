# This one gets all table data text
import re
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
from PIL import Image
from datetime import date


def get_github_screenshot(github_user_id: str):
    """
    get screenshot for github daily commit progress
    """

    # chrome driver options
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    options.add_argument("window-size=1920,1080")
    driver = webdriver.Chrome("./chromedriver", options=options)
    driver.maximize_window()

    url = f"https://github.com/{github_user_id}"

    # open url link with driver
    driver.get(url)

    today = date.today()
    today_date = str(today)

    # select elements on github page for the screenshot
    github_panel_wrapper = driver.find_element_by_class_name("js-yearly-contributions")
    github_panel = driver.find_element_by_class_name("graph-before-activity-overview")
    comitted_day = driver.find_element_by_css_selector(f'[data-date="{today_date}"]')

    # scroll down for screenshot
    # driver.execute_script("arguments[0].scrollIntoView();", github_panel)
    driver.execute_script("window.scrollTo(0, 600)")

    # select today's github commit tile icon
    time.sleep(2)

    # click today's github commit tile icon
    comitted_day.click()

    # take screen shot
    github_panel.screenshot(f"./img/{today_date}_github.png")

    # quit driver
    driver.quit()


def main():
    """
    designate functions for main
    """
    get_github_screenshot("snoop2head")


if __name__ == "__main__":
    main()

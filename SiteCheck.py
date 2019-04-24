import os
from selenium import webdriver

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")
browser = webdriver.Chrome(DRIVER_BIN)


def open_browser_and_select_item(title):
    browser.get('http://www.hurriyet.com.tr/')
    element = browser.find_element_by_xpath('//*[@id="sticky-header-control"]/header/div/div/div/div[3]/a')
    element.click()
    menu_container = browser.find_element_by_xpath('//*[@id="sticky-header-control"]/header/nav/div[2]/div')
    menu_elements = menu_container.find_elements_by_tag_name('a')
    item_exist = False
    for item in menu_elements:
        if item.text == title:
            item_exist = True
    if item_exist:
        print(title + " is exist in menu")
    else:
        print(title + " is not exist in menu")


open_browser_and_select_item('Bigpara')
browser.close()
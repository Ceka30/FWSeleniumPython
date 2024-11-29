import os
from config.browser_handler import browser_handler
from pages.clickToCall_page import clickToCall_page

def init_config(context,scenario):
    driver = browser_handler["chrome"]()
    context.driver = driver
    context.clickToCall_page = clickToCall_page(driver)
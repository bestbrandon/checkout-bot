from selenium import webdriver
import time
browser = webdriver.Chrome()

browser.get('http://www.supremenewyork.com/shop/accessories/w8alkjscb/ykw9go8i2')
add_button = browser.find_element_by_css_selector('#add-remove-buttons > input')
add_button.click()

time.sleep(.1)
checkout_now = browser.find_element_by_css_selector('#cart > a.button.checkout')
checkout_now.click()


from selenium import webdriver
import time
browser = webdriver.Chrome()

browser.get('http://www.supremenewyork.com/shop/accessories/wlbn2v5ix/v3s6d1rm2')
add_button = browser.find_element_by_css_selector('#add-remove-buttons > input')
add_button.click()

time.sleep(.1)
checkout_now = browser.find_element_by_css_selector('#cart > a.button.checkout')
checkout_now.click()

name = browser.find_element_by_css_selector('#order_billing_name')
name.send_keys("test first name")

email = browser.find_element_by_css_selector('#order_email')
email.send_keys("testemail@test.com")

phone = browser.find_element_by_css_selector('#order_tel')
phone.send_keys("555-555-5555")

address = browser.find_element_by_css_selector('#bo')
address.send_keys("123 sesame street")

zip_code = browser.find_element_by_css_selector('#order_billing_zip')
zip_code.send_keys("01234")

city = browser.find_element_by_css_selector('#order_billing_city')
city.send_keys("New York City")

state = browser.find_element_by_css_selector('#order_billing_state')
state.send_keys('NY')

credit_card = browser.find_element_by_css_selector('#cnb')
credit_card.send_keys('1234 4567 7890 1234')

cvv = browser.find_element_by_css_selector('#vval')
cvv.send_keys(111)

agree = browser.find_element_by_css_selector('#cart-cc > fieldset > p:nth-child(5) > label > div > ins')
agree.click()
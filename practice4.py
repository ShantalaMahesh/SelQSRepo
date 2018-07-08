from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
driver = Chrome('D:\chromedriver.exe')
driver.maximize_window()
driver.get('https://www.google.com/')
element =  driver.find_element_by_link_text('Images')
element.click()
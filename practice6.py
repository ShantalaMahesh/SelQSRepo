from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
driver = Chrome('D:\chromedriver.exe')
driver.maximize_window()

driver.get('https://www.facebook.com/')
element1 = driver.find_element_by_id('email')
element2 = driver.find_element_by_id('pass')
element1.send_keys('nnjnkbbjmku@gmail.com',Keys.CONTROL,'a')
element1.send_keys(Keys.CONTROL,'c')
element2.send_keys(Keys.CONTROL,'v')
element2.send_keys(Keys.ENTER)

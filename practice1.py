from selenium.webdriver import  Chrome
from  selenium.webdriver.common.keys import Keys
driver=Chrome('D:\chromedriver.exe')
driver.maximize_window()
driver.get('https://www.google.com/')
element_search_txt_bx=driver.find_element_by_id('lst-ib')
element_search_txt_bx.send_keys('Java',Keys.CONTROL,'a')
element_search_txt_bx.send_keys('python',Keys.ENTER)

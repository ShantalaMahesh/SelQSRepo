from selenium.webdriver import Chrome
driver=Chrome('D:\chromedriver.exe')
driver.maximize_window()
driver.get('https://www.google.com/')
element = driver.find_element_by_link_text('Gmail')
element.click()
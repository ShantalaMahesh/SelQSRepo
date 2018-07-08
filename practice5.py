from selenium.webdriver import Chrome

driver=Chrome('D:\chromedriver.exe')
driver.maximize_window()
driver.get("https://www.yatra.com/")
element1=driver.find_element_by_id('BE_flight_origin_city')
element2 = driver.find_element_by_id('BE_flight_arrival_city')
element3 =driver.find_element_by_id('BE_flight_flsearch_btn')
element1.send_keys('Mumbai')
element2.send_keys('Banglore')
element3.click()

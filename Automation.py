from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time 
driver = webdriver.Chrome("C:/Users/HP/Downloads/Chrome driver/chromedriver")
driver.get("https://web.whatsapp.com/")
wait=WebDriverWait(driver, 600)
target='"Jaspreet"'
string = "I am Using Python with Whatsapp"
x_arg='//span[contains(@title, '+ target + ')]'
target = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
target.click()
input_box=driver.find_element_by_class_name('_1Plpp')
for i in range(300):
    input_box.send_keys(string + Keys.ENTER)

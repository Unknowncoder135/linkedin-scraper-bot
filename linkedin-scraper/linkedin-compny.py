from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
import pandas as pd
import wget

# logic of login..
PATH ="C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get('https://www.linkedin.com')
time.sleep(2)

username = driver.find_element_by_name('session_key')
password = driver.find_element_by_name('session_password')
username.send_keys('your usename')
password.send_keys('your password')

time.sleep(3)
submit = driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(3)
# for a bug   
# submit1 = driver.find_element_by_xpath("//button[@type='button']").click()
lists  = []

#  data fatch...
for x in range(0,50,25):
    driver.get('https://www.linkedin.com/jobs/search/?keywords=your url  &start='+str(x))
    time.sleep(2)

    main_item  = driver.find_elements_by_xpath("//div[starts-with(@class,'job-card-container')]")
    # print(len(main_item))
    # print(main)
    for z in main_item:
        a = z.text
        print(a)
        lists.append(a)


# df = pd.DataFrame(lists)
# df.to_csv('data1.csv',index = False)

driver.quit()

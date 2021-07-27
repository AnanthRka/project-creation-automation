# Batch file location: C:\Windows\System32\create.bat

import sys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from time import sleep

project_name = sys.argv[1]

# initializing the browser
option = webdriver.ChromeOptions()
option.add_argument('--headless')
option.add_argument("--log-level=3")
option.add_experimental_option('excludeSwitches', ['enable-logging'])

CDM = ChromeDriverManager(log_level='0')
browser = webdriver.Chrome(CDM.install(), options=option)
browser.get(r'https://github.com/login')
username = "Enter your Github username"
password = "Enter your Github password"
sleep(1)

browser.find_element_by_xpath('//*[@id="login_field"]').send_keys(username)

browser.find_element_by_xpath('//*[@id="password"]').send_keys(password)
sleep(2)
browser.find_element_by_xpath('//*[@id="login"]/div[4]/form/div/input[12]').click()
url = browser.current_url
if url != r'https://github.com/':
    sys.exit()
sleep(1)
browser.get(r'https://github.com/new')
browser.find_element_by_xpath('//*[@id="repository_name"]').send_keys(project_name)
sleep(2)
browser.find_element_by_xpath('//*[@id="repository_name"]').send_keys(Keys.ENTER)

browser.quit()
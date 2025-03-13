import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import ElementClickInterceptedException
from selenium.common.exceptions import NoSuchElementException

load_dotenv()

tinder_URL = "https://tinder.com/"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(tinder_URL)

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]
time.sleep(3)

cookie = driver.find_element(By.XPATH, value='//*[@id="q2008297129"]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]/div')

login = driver.find_element(By.XPATH, value='//*[@id="q2008297129"]/div/div[1]/div/main/div[1]/div/div/div/'
                                            'div/div/header/div/div[2]/div[2]/a/div[2]/div[2]')

cookie.click()
time.sleep(1)
login.click()
time.sleep(2)

fb_log = driver.find_element(By.XPATH, value='//*[@id="q279916053"]/div/div/div/div[1]/div/div/div[2]/'
                                             'div[2]/span/div[2]/button/div[2]/div[2]')
fb_log.click()
time.sleep(2)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

email = driver.find_element(By.XPATH, value='//*[@id="email"]')
password = driver.find_element(By.XPATH, value='//*[@id="pass"]')

email.send_keys(EMAIL, Keys.TAB)
password.send_keys(PASSWORD, Keys.ENTER)
time.sleep(5)

driver.switch_to.window(base_window)
time.sleep(3)

try :
    location = driver.find_element(By.XPATH, value='//*[@id="q279916053"]/div/div/div/div/'
                                                   'div[3]/button[1]/div[2]/div[2]')
    location.click()
    time.sleep(2)

    notification = driver.find_element(By.XPATH, value='//*[@id="q279916053"]/div/div/div/'
                                                       'div/div[3]/button[1]/div[2]/div[2]')
    notification.click()
    time.sleep(4)

except NoSuchElementException as e:
    print(f"Error occurred: {e}")
    time.sleep(3)

gold = driver.find_element(By.XPATH, value='//*[@id="q279916053"]/div/div/div/div[3]/button[2]/div[2]/div[2]')
if gold:
    gold.click()
    time.sleep(3)
else:
    pass

while True:
    try:
        like = driver.find_elements(By.CSS_SELECTOR, 'span.gamepad-icon-wrapper[style="transform: scale(1);'
                                                     ' filter: none;"]')[1]
        if like:
            like.click()
            time.sleep(3)
    except (NoSuchElementException, ElementClickInterceptedException) as e:
        print(f"Error occurred: {e}")
        time.sleep(3)
        break

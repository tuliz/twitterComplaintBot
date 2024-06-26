from selenium import webdriver
from selenium.webdriver.common.by import By
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = ''
TWITTER_PASSWORD = ''
TWITTER_URL = 'https://x.com/home'


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://www.speedtest.net/')

# When opening speed test page there is an agreement, get the agree button an click
time.sleep(6)
accept_btn = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
accept_btn.click()

# After clicking accept button wait for a few seconds for it to close and then get start test button and click
time.sleep(6)
start_test = driver.find_element(By.CLASS_NAME, 'js-start-test')
start_test.click()

# Keep a while loop untill the test is ending
while True:

    try:
        #get the download and upload result only if there are number in both of them
        download = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        upload = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        if download != '—' and download != '' and upload != '—' and upload != '':
            break

    except:
        pass

# Close the speed test page after finishing test
driver.close()

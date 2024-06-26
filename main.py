from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = ''
TWITTER_PASSWORD = ''
TWITTER_URL = 'https://x.com/home'


def speedtest_check():

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
            # get the download and upload result only if there are number in both of them
            download = driver.find_element(By.XPATH,
                                           '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
            upload = driver.find_element(By.XPATH,
                                         '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
            if download != '—' and download != '' and upload != '—' and upload != '':
                break

        except:
            pass

    return {'download':download, 'upload':upload}


def connect_twitter(tweet):

    driver.get('https://x.com/home')

    # When connecting there is an agreement window, get the button and click
    time.sleep(2)
    agreement = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div[2]/div/div/div/button')
    agreement.click()

    # Get the login button and click it to move to the login page
    time.sleep(2)
    login_btn = driver.find_element(By.CSS_SELECTOR, 'a[data-testid="loginButton"]')
    login_btn.click()

    # Get the Email input and enter the email
    time.sleep(3)
    email_input = driver.find_element(By.NAME, 'text')
    email_input.send_keys(TWITTER_EMAIL, Keys.ENTER)

    # Get the position of the password input
    time.sleep(2)
    password_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'

    # There are times that twitter suspect the login and asks for a user name or phone
    try:
        password_input = driver.find_element(By.XPATH, password_xpath)
        password_input.send_keys(TWITTER_PASSWORD, Keys.ENTER)

    # If the password input is not found and means you need to enter username/phone
    except:
        user_input = driver.find_element(By.TAG_NAME, 'input')
        user_input.send_keys('', Keys.ENTER)
        time.sleep(3)
        password_input = driver.find_element(By.XPATH, password_xpath)
        password_input.send_keys(TWITTER_PASSWORD, Keys.ENTER)

    # Get the tweet input and send the tweet to the input
    time.sleep(5)
    tweet_input = driver.find_element(By.CSS_SELECTOR, 'br[data-text="true"]')
    tweet_input.send_keys(tweet)

    # Find the submit button and click it to send the tweet
    time.sleep(2)
    send_tweet = driver.find_element(By.XPATH,
                                     '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
    send_tweet.click()

# Selenium Setup
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=chrome_options)

download_upload = speedtest_check()

# If the download and upload lower then promised call function for connecting to twitter and tweet about it
if float(download_upload['download']) < PROMISED_DOWN and float(download_upload['upload']) < PROMISED_UP:
    tweet = (f'The promised Download is {PROMISED_DOWN} and the promised Upload is {PROMISED_UP} and instead'
             f'i got a download of {download_upload['download']} and upload of {download_upload['upload']}')
    connect_twitter(tweet)

#Close the speed test page after finishing test
driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time

class InternetSpeedTwitterBot:
    def __init__(self):
        # Selenium Setup
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def speedtest_check(self):

        self.driver.get('https://www.speedtest.net/')

        # When opening speed test page there is an agreement, get the agree button an click
        time.sleep(6)
        accept_btn = self.driver.find_element(By.ID, 'onetrust-accept-btn-handler')
        accept_btn.click()

        # After clicking accept button wait for a few seconds for it to close and then get start test button and click
        time.sleep(6)
        start_test = self.driver.find_element(By.CLASS_NAME, 'js-start-test')
        start_test.click()

        # Keep a while loop untill the test is ending
        while True:

            try:
                # get the download and upload result only if there are number in both of them
                download = self.driver.find_element(By.XPATH,
                                               '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
                upload = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
                if download != '—' and download != '' and upload != '—' and upload != '':
                    break

            except:
                pass

        return {'download': download, 'upload': upload}

    def connect_twitter(self,tweet,email, password):

        self.driver.get('https://x.com/home')

        # When connecting there is an agreement window, get the button and click
        time.sleep(2)
        agreement = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div[2]/div/div/div/button')
        agreement.click()

        # Get the login button and click it to move to the login page
        time.sleep(2)
        login_btn = self.driver.find_element(By.CSS_SELECTOR, 'a[data-testid="loginButton"]')
        login_btn.click()

        # Get the Email input and enter the email
        time.sleep(3)
        email_input = self.driver.find_element(By.NAME, 'text')
        email_input.send_keys(email, Keys.ENTER)

        # Get the position of the password input
        time.sleep(2)
        password_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input'

        # There are times that twitter suspect the login and asks for a user name or phone
        try:
            password_input = self.driver.find_element(By.XPATH, password_xpath)
            password_input.send_keys(password, Keys.ENTER)

        # If the password input is not found and means you need to enter username/phone
        except:
            user_input = self.driver.find_element(By.TAG_NAME, 'input')
            user_input.send_keys('', Keys.ENTER)
            time.sleep(3)
            password_input = self.driver.find_element(By.XPATH, password_xpath)
            password_input.send_keys(password, Keys.ENTER)

        # Get the tweet input and send the tweet to the input
        time.sleep(5)
        tweet_input = self.driver.find_element(By.CSS_SELECTOR, 'br[data-text="true"]')
        tweet_input.send_keys(tweet)

        # Find the submit button and click it to send the tweet
        time.sleep(2)
        send_tweet = self.driver.find_element(By.XPATH,
                                         '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button')
        send_tweet.click()

    def close_windows(self):
        self.driver.quit()
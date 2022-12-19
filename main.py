from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import random
import time

INTERNET_PROVIDER = # Type your provider here
PROMISED_DOWN = # Promised down speed
PROMISED_UP = # Promised up speed
TWITTER_EMAIL = # Email
TWITTER_PASSWORD = # Twitter password
TWITTER_USERNAME = # Twitter username



class InternetSpeedTwitterBot:

    def __init__(self):
        """Twitter Bot Class"""
        self.s = Service('C:\Development\chromedriver.exe')
        self.driver = webdriver.Chrome(service=self.s)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        """Testing the internet speed"""
        self.driver.get("https://www.speedtest.net/")
        time.sleep(2)
        # Accept all cookies
        try:
            self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()

        except NoSuchElementException:
            print("No cookies pop-up, skipped.")
            pass
        # Run Speed Test

        finally:
            self.driver.find_element(By.XPATH,
                                     '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a').click()
            time.sleep(50)
            self.up = float(self.driver.find_element(By.XPATH,
                                               '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]'
                                               '/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text)
            self.down = float(self.driver.find_element(By.XPATH,
                                                 '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]'
                                                 '/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text)
            return self.up, self.down

    def tweet_at_provider(self):
        """Tweeting to provider"""
        MESSAGE = f"Hey {INTERNET_PROVIDER}, why is my internet speed in Helsinki {self.down}down/{self.up}up when " \
                  f"i pay for {PROMISED_DOWN}/{PROMISED_UP}?"

        if self.down < PROMISED_DOWN:
            self.driver.get("https://twitter.com/?lang=fi")
            time.sleep(random.uniform(3.5, 4.5))

            # Accept all cookies
            self.driver.find_element(By.XPATH,
                                         '//*[@id="layers"]/div/div[2]/div/div/div/div[2]/div[1]').click()

             # Login
            self.driver.find_element(By.XPATH,
                                          '//*[@id="layers"]/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/a').click()
            time.sleep(5)
            self.driver.find_element(By.XPATH,
                                         '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]'
                                         '/div[2]/div/div/div[2]/div[2]'
                                         '/div/div/div/div[5]/label/div/div[2]/div/input').send_keys(TWITTER_EMAIL + Keys.ENTER)
            time.sleep(random.uniform(5.0, 6.5))

            try:

                # There was unusual login activity on your account
                time.sleep(random.uniform(5.5, 8.5))
                self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/'
                                                   'div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label'
                                                   '/div/div[2]/div/input').send_keys(TWITTER_USERNAME + Keys.ENTER)

            except NoSuchElementException:
                print("No warnings, then skip")
                pass

            finally:
                time.sleep(random.uniform(5.5, 8.5))
                self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div'
                                                   '/div[2]/div[2]/div/div/div[2]/div'
                                                   '[2]/div[1]/div/div/div[3]/div/'
                                                   'label/div/div[2]/div[1]/input').send_keys(TWITTER_PASSWORD + Keys.ENTER)
                time.sleep(random.uniform(5.5, 8.5))

                # Tweeting
                time.sleep(random.uniform(8.5, 11.5))
                tweet = self.driver.find_element(By.CSS_SELECTOR, 'br[data-text="true"]')
                tweet.send_keys(MESSAGE)

                # Time to send the tweet
                self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/'
                                                   'div[3]/div/div[2]/div[1]/div/div/div/div[2]/'
                                                   'div[3]/div/div/div[2]/div[3]').click()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
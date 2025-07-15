import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
PROMISED_DOWN=150
PROMISED_UP=10
TWITTER_EMAIL='Mikeydread28@gmail.com'
TWITTER_PASSWORD='CryptX29'

class InternetSpeedTwitterBot:
    def __init__(self,driver_path):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.up=0
        self.down=0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)

        try:
            wait = WebDriverWait(self.driver,10)
            button=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.start-button a')))
            button.click()
            print("Testing Starting...")
            #num1 = self.driver.find_element(By.XPATH,value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span[1]')
            #print(num1.text)
        except:
            print("Failed")
    def tweet_at_provider(self):
        print("Testing Please Allow 60 seconds")
        time.sleep(30)
        try:
            wait= WebDriverWait(self.driver,10)
            num1=wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span[1]')))
            print(f"This is your Download Speed {num1.text} Mbps")
        except:
            print("This one failed")

        time.sleep(15)
        num2=self.driver.find_element(By.XPATH,value='//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        print(f"This is your Upload Speed {num2.text} Mbps")

bot=InternetSpeedTwitterBot("https://www.speedtest.net/")
bot.get_internet_speed()
bot.tweet_at_provider()

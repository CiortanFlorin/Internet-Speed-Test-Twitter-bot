from selenium import webdriver
import time

class InternetSpeedTwitterBot:
    def __init__(self, path, down, up):
        self.driver = webdriver.Chrome(path)
        self.down = down
        self.up = up

    def getspeed(self,URL):
        self.driver.get(URL)
        self.driver.find_element_by_id('_evidon-banner-acceptbutton').click()
        self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]').click()
        time.sleep(50)
        self.down_speed = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up_speed = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        print(self.down_speed)
        print(self.up_speed)

    def twit(self, URL, username, password):
        self.driver.get(URL)
        time.sleep(1)
        self.driver.find_element_by_css_selector("a[href='/login']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div').click()
        time.sleep(2)
        msg=f'Hey internet provider, why is my interet speed {self.down_speed}down/{self.up_speed}up when I pay for {self.down}down/{self.up}up ?'
        print(msg)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div').send_keys(msg)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div').click()
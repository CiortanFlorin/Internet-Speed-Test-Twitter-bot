from InternetSpeedTwitterBot import InternetSpeedTwitterBot


chrome_driver_path = "E:\development\chromedriver.exe"
PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "YOUR EMAIL"
TWITTER_PASS = "YOUR TWITTER PASSWORD"
URL = "https://www.speedtest.net/"
URL2 = "https://twitter.com/?logout=1626378656019"
driver = InternetSpeedTwitterBot(chrome_driver_path, PROMISED_UP, PROMISED_DOWN)

driver.getspeed(URL)

driver.twit(URL2, TWITTER_EMAIL, TWITTER_PASS)
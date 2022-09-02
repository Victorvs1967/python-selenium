import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def test01():
  browser = webdriver.Firefox()
  browser.get('https://duckduckgo.com')
  browser.save_screenshot('duckduckgo.png')
  time.sleep(5)
  browser.get('https://google.com')
  browser.refresh()
  browser.quit()  
  
def test02(): 
  browser = webdriver.Firefox()
  browser.get('https://youtube.com')
  # time.sleep(2)
  # xpath = '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer/a/tp-yt-paper-button/yt-formatted-string'
  # browser.find_element(By.XPATH, xpath).click()
  # time.sleep(2)
  # login_xpath = '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input'
  # browser.find_element(By.XPATH, login_xpath).send_keys('victorsmirnov67@gmail.com')
  # next_xpath = '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button'
  # browser.find_element(By.XPATH, next_xpath).click()
  
  html = browser.find_element(By.TAG_NAME, 'html')
  for _ in range(10):
    html.send_keys(Keys.DOWN)
  
def main():
  # test01()  
  test02()
  

if __name__ == '__main__':
  main()
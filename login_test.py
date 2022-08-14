from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

def test_log_in():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    wait = WebDriverWait(driver, 10)
    driver.get('http://seleniumdemo.com/')
    driver.find_element(By.XPATH, '//*[@id="menu-item-22"]/a/span').click()
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys('jacekkowalski@gmail.com')
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('ZYWzJn8dP2Lgzvi')
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(Keys.ENTER)
    
        
    driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

def test_log_in_passed():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get('http://seleniumdemo.com/')
    driver.find_element(By.XPATH, '//*[@id="menu-item-22"]/a/span').click()
    driver.find_element(By.ID, 'username').send_keys('testeroprogramowania@gmial.com')
    driver.find_element(By.ID, 'password').send_keys('testeroprogramowania')
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(Keys.ENTER)
    
    assert driver.find_element(By.LINK_TEXT, 'Logout').is_displayed()   

def test_log_in_failed():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get('http://seleniumdemo.com/')
    driver.find_element(By.XPATH, '//*[@id="menu-item-22"]/a/span').click()
    driver.find_element(By.ID, 'username').send_keys('testeroprogramowania@gmial.com')
    driver.find_element(By.ID, 'password').send_keys('testeroprogramowania123')
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(Keys.ENTER)    
    
    # czy zawiera się w ...
    assert 'ERROR: Incorrect username or password.' in driver.find_element(By.XPATH, '//ul[@class="woocommerce-error"]//li').text 
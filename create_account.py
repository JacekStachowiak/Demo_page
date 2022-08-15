from webbrowser import Chrome
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_create_account_failed():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('http://seleniumdemo.com/?page_id=7/')
    driver.find_element(By.ID, 'reg_email').send_keys('testeroprogramowania@gmial.com')
    driver.find_element(By.ID, 'reg_password').send_keys('testeroprogramowania')
    driver.find_element(By.ID, 'reg_password').click(Keys.ENTER)
    
    
    
    
    
    
    
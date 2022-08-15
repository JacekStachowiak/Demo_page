from webbrowser import Chrome
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import random

def test_update_address():
    email = str(random.randint(0, 10000)) + 'testeroprogramowania@gmial.com'
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('http://seleniumdemo.com/?page_id=7/')
    driver.maximize_window()
    driver.find_element(By.ID, 'reg_email').send_keys(email)
    driver.find_element(By.ID, 'reg_password').send_keys('testeroprogramowania')
    driver.find_element(By.ID, 'reg_password').send_keys(Keys.ENTER)
    driver.find_element(By.LINK_TEXT, 'Addresses').click()
    driver.find_element(By.LINK_TEXT, 'Edit').click()
    driver.find_element(By.ID, 'billing_first_name').send_keys('Jack123')
    driver.find_element(By.ID, 'billing_last_name').send_keys('Stach123')
    driver.find_element(By.ID, 'billing_company').send_keys('Capital')
    Select(driver.find_element(By.ID, 'billing_country')).select_by_visible_text('Poland')
    driver.find_element(By.ID, 'billing_address_1').send_keys('Dworcowa 2')
    driver.find_element(By.ID, 'billing_postcode').send_keys('75-095')
    driver.find_element(By.ID, 'billing_city').send_keys('Kraków')
    driver.find_element(By.ID, 'billing_phone').send_keys('566 765 123')
    driver.find_element(By.XPATH, '//button[@value="Save address"]').click()
            
    address = 'Address changed successfully.' in driver.find_element(By.XPATH, '//div[@class="woocommerce-message"]').text
    assert address
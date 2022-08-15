from webbrowser import Chrome
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import random

class AddressLocators:
    
    reg_email_input = (By.ID, 'reg_email')
    reg_password_input = (By.ID, 'reg_password')
    addresses_link = (By.LINK_TEXT, 'Addresses')
    edit_link = (By.LINK_TEXT, 'Edit')
    first_name_input = (By.ID, 'billing_first_name')
    last_name_input = (By.ID, 'billing_last_name')
    company_ID = (By.ID, 'billing_company')     
    country_select = (By.ID, 'billing_country')
    street_input = (By.ID, 'billing_address_1')
    postcode_input = (By.ID, 'billing_postcode')
    city_input = (By.ID, 'billing_city')
    phone_input = (By.ID, 'billing_phone') 
    save_button = (By.XPATH, '//button[@value="Save address"]')
    mesage = (By.XPATH, '//div[@class="woocommerce-message"]')  

class MyAccountPage:
    
    username_input = (By.ID, 'username')
    password_input = (By.ID, 'password')
    reg_email_input = (By.ID, 'reg_email')
    reg_password_input = (By.ID, 'reg_password')
    # my_account_link = (By.XPATH, '//*[@id="menu-item-22"]/a/span')
    error_message = (By.XPATH, '//ul[@class="woocommerce-error"]//li')
    logout_link = (By.LINK_TEXT, 'Logout')
 
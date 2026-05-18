from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    # login fields
    textbox_email_login_xpath = "(//input[@placeholder='email'])[1]"
    textbox_password_xpath = "(//input[@placeholder='password'])[1]"
    textbox_ownerId_xpath = "(//input[@placeholder='shop_xxxxx'])[1]"
    # forgot password fields
    link_forgot_pass_xpath = "(//button[normalize-space()='Forgot Password?'])[1]"
    textbox_email_field_xpath = "(//input[@placeholder='Enter your email address'])[1]"
    button_send_link_xpath = "(//button[normalize-space()='Send Link'])[1]"
    button_cancel_link_xpath = "(//button[normalize-space()='Cancel'])[1]"
    # login button
    button_login_xpath = "(//button[normalize-space()='Login'])[1]"
    # logout button
    button_logout_xpath = "//aside[1]//div[3]//button[1]"
    button_confirm_logout_xpath = "(//button[contains(text(),'Logout')])[1]"
    button_cancel_logout_xpath = "(//button[normalize-space()='Cancel'])[1]"


    def __init__(self, driver):
        self.driver = driver

    def set_login_email(self, login_email):
        self.driver.find_element(By.XPATH, self.textbox_email_login_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_email_login_xpath).send_keys(login_email)

    def set_login_pass(self, login_pass):
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(login_pass)

    def set_owner_id(self, owner_id):
        self.driver.find_element(By.XPATH, self.textbox_ownerId_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_ownerId_xpath).send_keys(owner_id)

    def click_forgot_pass(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.link_forgot_pass_xpath))
        ).click()

    def set_email_field(self, email_field):
        self.driver.find_element(By.XPATH, self.textbox_email_field_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_email_field_xpath).send_keys(email_field)

    def click_send_link_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_send_link_xpath))
        ).click()

    def click_cancel_link_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_cancel_link_xpath))
        ).click()

    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_login_xpath))
        ).click()

    def click_logout_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_logout_xpath))
        ).click()

    def click_confirm_logout_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_confirm_logout_xpath))
        ).click()

    def click_cancel_logout_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_cancel_logout_xpath))
        ).click()



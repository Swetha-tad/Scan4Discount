from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegisterPage:
    button_register_xpath = "(//button[normalize-space()='Create Account as Shop Owner'])[1]"
    # registration form fields
    textbox_fullname_xpath = "(//input[@placeholder='John Doe'])[1]"
    textbox_phone_xpath = "(//input[@placeholder='9876543210'])[1]"
    textbox_email_name = "email"
    button_send_xpath = "(//button[normalize-space()='Send OTP'])[1]"
    textbox_otp_xpath = "(//input[@placeholder='Enter 6-digit OTP'])[1]"
    button_verify_xpath = "(//button[normalize-space()='Verify OTP'])[1]"
    button_cancel_xpath = "(//button[normalize-space()='Cancel'])[1]"
    textbox_business_name_xpath = "(//input[@placeholder='My Shop Pvt. Ltd.'])[1]"
    textbox_city_name = "city"
    textbox_state_name = "state"
    textbox_pincode_name = "pincode"
    textbox_address_name = "address"
    button_upload_xpath = "(//input[@type='file'])[1]"
    button_submit_xpath = "(//button[normalize-space()='Next: Choose Plan'])[1]"
    # plan details
    card_plan1_xpath = "(//div)[23]"
    card_plan2_xpath = "(//div)[26]"
    card_plan3_xpath = "(//div[@class='border rounded-xl p-5 cursor-pointer transition-all relative border-yellow-500 bg-yellow-500/10 shadow-lg shadow-yellow-500/10'])[1]"
    button_proceed_xpath = "(//button[normalize-space()='Proceed to Payment'])[1]"
    button_back_xpath = "(//button[contains(text(),'← Back')])[1]"


    def __init__(self, driver):
        self.driver = driver

    def click_register_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_register_xpath))
        ).click()

    def set_full_name(self, full_name):
        self.driver.find_element(By.XPATH, self.textbox_fullname_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_fullname_xpath).send_keys(full_name)

    def set_phone_number(self, phone_number):
        self.driver.find_element(By.XPATH, self.textbox_phone_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_phone_xpath).send_keys(phone_number)

    def set_email_id(self, email_id):
        self.driver.find_element(By.NAME, self.textbox_email_name).clear()
        self.driver.find_element(By.NAME, self.textbox_email_name).send_keys(email_id)

    def click_send_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_send_xpath))
        ).click()

    def set_otp(self, otp):
        self.driver.find_element(By.XPATH, self.textbox_otp_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_otp_xpath).send_keys(otp)

    def click_verify_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_verify_xpath))
        ).click()

    def click_cancel_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_cancel_xpath))
        ).click()

    def set_business_name(self, business_name):
        self.driver.find_element(By.NAME, self.textbox_business_name_xpath).clear()
        self.driver.find_element(By.NAME, self.textbox_business_name_xpath).send_keys(business_name)

    def set_city(self, city):
        self.driver.find_element(By.NAME, self.textbox_city_name).clear()
        self.driver.find_element(By.NAME, self.textbox_city_name).send_keys(city)

    def set_state(self, state):
        self.driver.find_element(By.NAME, self.textbox_state_name).clear()
        self.driver.find_element(By.NAME, self.textbox_state_name).send_keys(state)

    def set_pincode(self, pincode):
        self.driver.find_element(By.NAME, self.textbox_pincode_name).clear()
        self.driver.find_element(By.NAME, self.textbox_pincode_name).send_keys(pincode)

    def set_address(self, address):
        self.driver.find_element(By.NAME, self.textbox_address_name).clear()
        self.driver.find_element(By.NAME, self.textbox_address_name).send_keys(address)

    def click_upload_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_upload_xpath))
        ).click()

    def click_submit_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_submit_xpath))
        ).click()

    def click_plan1_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.card_plan1_xpath))
        ).click()

    def click_plan2_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.card_plan2_xpath))
        ).click()

    def click_plan3_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.card_plan3_xpath))
        ).click()

    def click_proceed_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_proceed_xpath))
        ).click()

    def click_back_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.button_back_xpath))
        ).click()






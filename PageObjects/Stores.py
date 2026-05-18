from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class StoresPage:
    url_stores_xpath = "(//span[normalize-space()='Stores'])[1]"
    btn_addstore_xpath = "(//button[normalize-space()='Add Store'])[1]"
    # add store fields
    text_store_name_xpath = "(//input[@placeholder='e.g. Downtown Fashion Hub'])[1]"
    text_store_code_xpath = "(//input[@placeholder='e.g. STR-042 or STORE_001'])[1]"
    drpdown_store_status_xpath = "(//select[@name='status'])[1]"
    text_store_address_xpath = "(//textarea[@placeholder='Street, area, landmark...'])[1]"
    text_store_city_xpath = "(//input[@placeholder='Hyderabad'])[1]"
    text_store_state_xpath = "(//input[@placeholder='Telangana'])[1]"
    text_store_zip_code_xpath = "(//input[@placeholder='500081'])[1]"
    text_owner_phone_xpath = "(//input[@placeholder='9XXXXXXXXX'])[1]"
    text_owner_email_xpath = "(//input[@placeholder='contact@store.com'])[1]"
    btn_create_store_xpath = "(//button[normalize-space()='Create Store'])[1]"
    btn_cancel_store_xpath = "(//button[normalize-space()='Cancel'])[1]"
    # search filter
    text_store_search_xpath = "(//input[@placeholder='Search stores by name, code, city...'])[1]"
    drpdown_store_filter_xpath = "(//select[@class='w-full sm:w-auto px-4 py-3 text-sm bg-gray-50 dark:bg-gray-800 border border-gray-300 dark:border-gray-700 rounded-lg focus:outline-none focus:ring-2 focus:ring-yellow-500 text-gray-900 dark:text-gray-100'])[1]"
    # store actions
    btn_store_actions_xpath = "(//*[name()='svg'][@class='lucide lucide-ellipsis-vertical'])[1]"
    btn_view_store_xpath = "(//button[@class='w-full text-left px-3 py-2 text-xs text-gray-700 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-800 flex items-center gap-2'])[1]"
    btn_edit_store_xpath = "(//button[normalize-space()='Edit'])[1]"
    btn_deactivate_store_xpath = "(//button[normalize-space()='Deactivate'])[1]"
    btn_delete_store_xpath = "(//button[@class='w-full text-left px-3 py-2 text-xs text-red-600 dark:text-red-400 hover:bg-gray-100 dark:hover:bg-gray-800 flex items-center gap-2.5'])[1]"
    btn_view_qrcode_xpath = "(//button[normalize-space()='View QR Code'])[1]"

    def __init__(self, driver):
        self.driver = driver

    def click_stores_page(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.url_stores_xpath))
        ).click()

    def click_add_store_btn(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_addstore_xpath))
        ).click()

    def set_store_name(self, store_name):
        self.driver.find_element(By.XPATH, self.text_store_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_store_name_xpath).send_keys(store_name)

    def set_store_code(self, store_code):
        self.driver.find_element(By.XPATH, self.text_store_code_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_store_code_xpath).send_keys(store_code)

    def select_store_status(self, store_status):
        status_dropdown = Select(self.driver.find_element(By.XPATH, self.drpdown_store_status_xpath))
        status_dropdown.select_by_visible_text(store_status)

    def set_store_address(self, store_address):
        self.driver.find_element(By.XPATH, self.text_store_address_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_store_address_xpath).send_keys(store_address)

    def set_store_city(self, store_city):
        self.driver.find_element(By.XPATH, self.text_store_city_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_store_city_xpath).send_keys(store_city)

    def set_store_state(self, store_state):
        self.driver.find_element(By.XPATH, self.text_store_state_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_store_state_xpath).send_keys(store_state)

    def set_store_zipcode(self, store_zipcode):
        self.driver.find_element(By.XPATH, self.text_store_zip_code_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_store_zip_code_xpath).send_keys(store_zipcode)

    def set_store_owner_phone(self, owner_phone):
        self.driver.find_element(By.XPATH, self.text_owner_phone_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_owner_phone_xpath).send_keys(owner_phone)

    def set_store_owner_email(self, owner_email):
        self.driver.find_element(By.XPATH, self.text_owner_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_owner_email_xpath).send_keys(owner_email)

    def click_create_store_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_create_store_xpath))
        ).click()

    def click_cancel_store_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_cancel_store_xpath))
        ).click()

    def set_store_search(self,valid_keyword):
        self.driver.find_element(By.XPATH, self.text_store_search_xpath).clear()
        self.driver.find_element(By.XPATH, self.text_store_search_xpath).send_keys(valid_keyword)

    def select_store_filter(self, store_filter):
        filter_dropdown = Select(self.driver.find_element(By.XPATH, self.drpdown_store_filter_xpath))
        filter_dropdown.select_by_visible_text(store_filter)


    def click_store_actions_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_store_actions_xpath))
        ).click()

    def click_store_view_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_view_store_xpath))
        ).click()

    def click_store_edit_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_edit_store_xpath))
        ).click()

    def click_store_deactivate_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_deactivate_store_xpath))
        ).click()

    def click_store_delete_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_delete_store_xpath))
        ).click()

    def click_view_Qr_code_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_view_qrcode_xpath))
        ).click()


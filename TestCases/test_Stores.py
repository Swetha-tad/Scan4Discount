import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageObjects.Login import LoginPage
from PageObjects.Stores import StoresPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
import time


class TestStores:
    loginURL = ReadConfig.get_loginURL()
    # login fields
    login_email = ReadConfig.get_login_email()
    login_pass = ReadConfig.get_login_pass()
    owner_id = ReadConfig.get_owner_id()
    # stores page
    storesURL = ReadConfig.get_stores_URL()
    add_store_btn = ReadConfig.get_add_store_btn()
    # store creation fields
    store_name = ReadConfig.get_store_name()
    store_code = ReadConfig.get_store_code()
    store_status = ReadConfig.get_store_status()
    store_address = ReadConfig.get_store_address()
    store_city = ReadConfig.get_store_city()
    store_state = ReadConfig.get_store_state()
    store_zipcode = ReadConfig.get_store_zipcode()
    owner_phone = ReadConfig.get_owner_phone()
    owner_email = ReadConfig.get_owner_email()
    create_store_btn = ReadConfig.get_create_store_btn()
    cancel_store_btn = ReadConfig.get_cancel_store_btn()
    # store search and filters
    store_search = ReadConfig.get_store_search()
    store_filter = ReadConfig.get_store_filter()
    # store actions
    store_actions = ReadConfig.get_store_actions()
    store_view_btn  = ReadConfig.get_store_view_btn()
    store_edit_btn = ReadConfig.get_store_edit_btn()
    store_deactivate_btn = ReadConfig.get_store_deactivate_btn()
    store_delete_btn = ReadConfig.get_store_delete_btn()
    view_qrcode_btn = ReadConfig.get_view_qrcode_btn()

    logger = LogGen.loggen()

    def test_stores_page_launch(self,setup):
        self.logger.info("*******  Verifying Stores Page Launch  *******")
        self.driver = setup
        wait = WebDriverWait(self.driver, 10)

        self.driver.get(self.loginURL)

        self.Login = LoginPage(self.driver)
        self.Stores = StoresPage(self.driver)

        self.Login.set_login_email(self.login_email)
        self.Login.set_login_pass(self.login_pass)
        self.Login.set_owner_id(self.owner_id)
        self.Login.click_login_button()

        self.Stores.click_stores_page()

        act_title = self.driver.title

        if act_title == "Scan4Discount":
            self.logger.info("******* Stores Page loaded successfully *******")
            self.driver.save_screenshot(".\\Screenshots\\test_stores_page_launch_Pass.png")
            self.driver.quit()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_stores_page_launch_Fail.png")
            self.driver.quit()
            self.logger.info("******* Stores Page Failed to Load *******")
            assert False


    def test_add_valid_store(self,setup):
        self.logger.info("*******  Verifying Valid Store Creation  *******")
        self.driver = setup
        self.driver.get(self.loginURL)
        self.Login = LoginPage(self.driver)
        self.Stores = StoresPage(self.driver)
        time.sleep(2)
        self.Login.set_login_email(self.login_email)
        self.Login.set_login_pass(self.login_pass)
        self.Login.set_owner_id(self.owner_id)
        self.Login.click_login_button()
        time.sleep(4)
        self.Stores.click_stores_page()
        time.sleep(4)
        self.Stores.click_add_store_btn()


        act_title = self.driver.title

        if act_title == "Scan4Discount":
            assert True
            self.logger.info("*******  Stores Page loaded successfully *******")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_stores_page_launch_Pass.png")
            self.driver.quit()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_stores_page_launch_Fail.png")
            self.driver.quit()
            self.logger.info("*******  Stores Page Failed to Load *******")
            assert False




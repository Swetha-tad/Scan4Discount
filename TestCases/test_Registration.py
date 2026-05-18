import unittest

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageObjects.Registration import RegisterPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
import time


class TestRegistration:
    loginURL = ReadConfig.get_loginURL()
    register_btn = ReadConfig.get_register_btn()
    full_name = ReadConfig.get_full_name()
    phone_number = ReadConfig.get_phone_number()
    email_id = ReadConfig.get_email_id()
    upload_btn = ReadConfig.get_upload_btn()
    submit_btn = ReadConfig.get_submit_btn()
    plan_card1 = ReadConfig.get_plan_card1()
    plan_card2 = ReadConfig.get_plan_card2()
    plan_card3 = ReadConfig.get_plan_card3()
    proceed_btn = ReadConfig.get_proceed_btn()
    back_btn = ReadConfig.get_back_btn()

    logger = LogGen.loggen()

    def test_Registration_PageTitle(self, setup):
        self.logger.info("*******  Verifying Registration Page Title  *******")
        self.driver = setup
        self.driver.get(self.loginURL)
        self.Registration = RegisterPage(self.driver)

        self.Registration.click_register_button()
        time.sleep(2)
        act_title = self.driver.title

        if act_title == "Scan4Discount":
            assert True
            self.logger.info("*******  Register Page loaded successfully *******")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Registration_PageTitle_Pass.png")
            self.driver.quit()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Registration_PageTitle_Fail.png")
            self.driver.quit()
            self.logger.info("*******  Registration Page Failed to Load *******")
            assert False

    @pytest.mark.parametrize(
        "full_name, phone_number, email_id",
        [
            ("John Doe", "9876543210", "john@test.com"), ("3654_+++", "23165", "john@.com"), ("", "", "")
        ]
    )

    def test_Mandatory_fields_verify(self, setup, full_name, phone_number, email_id):
        self.logger.info("*******  Verifying Valid Registration *******")
        self.driver = setup
        self.driver.get(self.loginURL)
        self.Registration = RegisterPage(self.driver)

        self.Registration.click_register_button()
        time.sleep(2)
        self.Registration.set_full_name(full_name)
        self.Registration.set_phone_number(phone_number)
        self.Registration.set_email_id(email_id)
        #self.Registration.set_business_name(business_name)
        #self.Registration.set_city(city)
        #self.Registration.set_state(state)
        #self.Registration.set_pincode(state)
        #self.Registration.set_address(address)

        act_title = self.driver.title

        if act_title == "Scan4Discount":
            assert True
            self.logger.info("******* Mandatory fields verification Successful with valid data *******")
            self.driver.save_screenshot(".\\Screenshots\\test_fields_verification_pass.png")
            self.driver.quit()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_fields_verification_Fail.png")
            self.driver.quit()
            self.logger.info("*******  Mandatory fields verification failed with valid data *******")
            assert False






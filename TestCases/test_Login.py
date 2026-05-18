import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageObjects.Login import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
import time


class TestLogin:
    loginURL = ReadConfig.get_loginURL()
    # login fields
    login_email = ReadConfig.get_login_email()
    login_pass = ReadConfig.get_login_pass()
    owner_id = ReadConfig.get_owner_id()
    # forgot password fields
    forgot_pass_link = ReadConfig.get_forgot_pass_link()
    email_id = ReadConfig.get_email_id()
    send_link = ReadConfig.get_send_link_button()
    cancel_link = ReadConfig.get_cancel_link_button()
    # login button
    login_btn = ReadConfig.get_login_button()
    # logout button
    logout_btn = ReadConfig.get_logout_button()
    confirm_logout_btn = ReadConfig.get_confirm_logout_button()
    cancel_logout_btn = ReadConfig.get_cancel_logout_button()

    logger = LogGen.loggen()


    def test_Valid_Login(self, setup):
        self.logger.info("*******  Verifying Valid User Login  *******")
        self.driver = setup
        self.driver.get(self.loginURL)
        self.Login = LoginPage(self.driver)
        time.sleep(2)
        self.Login.set_login_email(self.login_email)
        self.Login.set_login_pass(self.login_pass)
        self.Login.set_owner_id(self.owner_id)
        self.Login.click_login_button()
        time.sleep(3)
        act_title = self.driver.title

        if act_title == "Scan4Discount":
            assert True
            self.logger.info("*******  User Login successfully *******")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_valid_Login_Pass.png")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_valid_Login_Fail.png")
            self.driver.close()
            self.logger.info("*******  User Login failed *******")
            assert False

    @pytest.mark.parametrize(
        "login_email, login_pass, owner_id",
        [
            ("swetha.excel2025@gmail.com", "validpassword", "owner_1205"),
            ("invaliduser@test.com", "Swetha_tad@26", "owner_1205"),
            ("", "", ""),
        ]
    )

    def test_InValid_Login(self, setup, login_email, login_pass, owner_id):
        self.logger.info("*******  Verifying InValid User Login  *******")
        self.driver = setup
        self.driver.get(self.loginURL)
        self.Login = LoginPage(self.driver)
        time.sleep(2)
        self.Login.set_login_email(login_email)
        self.Login.set_login_pass(login_pass)
        self.Login.set_owner_id(owner_id)
        self.Login.click_login_button()
        time.sleep(3)
        act_title = self.driver.title

        if act_title == "Scan4Discount":
            assert True
            self.logger.info("*******  Invalid User Login Failed *******")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Invalid_Login_Pass.png")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Invalid_Login_Fail.png")
            self.driver.close()
            self.logger.info("*******  Invalid User Login failed *******")
            assert False

    @pytest.mark.parametrize(
        "email_field",
        [
            "swetha.excel2025@gmail.com",
            "invaliduser@test.com",
            "",
        ]
    )


    def test_forgot_password(self,setup,email_field):
        self.logger.info("*******  Verifying Forgot Password Functionality  *******")
        self.driver = setup
        self.driver.get(self.loginURL)
        self.Login = LoginPage(self.driver)

        self.Login.click_forgot_pass()
        self.Login.set_email_field(email_field)
        self.Login.click_send_link_button()

        time.sleep(3)
        act_title = self.driver.title

        if act_title == "Scan4Discount":
            assert True
            self.logger.info("*******  Forgot Password Functionality working successfully *******")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_forgot_password_Pass.png")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_forgot_password_Fail.png")
            self.driver.close()
            self.logger.info("*******  Forgot Password Functionality Failed *******")
            assert False


    def test_logout(self,setup):
        self.logger.info("*******  Verifying Logout Functionality  *******")
        self.driver = setup
        self.driver.get(self.loginURL)
        self.Login = LoginPage(self.driver)
        time.sleep(2)
        self.Login.set_login_email(self.login_email)
        self.Login.set_login_pass(self.login_pass)
        self.Login.set_owner_id(self.owner_id)
        self.Login.click_login_button()
        time.sleep(2)
        self.Login.click_logout_button()
        time.sleep(2)
        self.Login.click_confirm_logout_button()

        act_title = self.driver.title

        if act_title == "Scan4Discount":
            assert True
            self.logger.info("*******  User Logged out successfully *******")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Logout_Pass.png")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Logout__Fail.png")
            self.driver.close()
            self.logger.info("*******  User Logout failed *******")
            assert False


    def test_cancel_logout(self,setup):
        self.logger.info("*******  Verifying Cancel Logout Functionality *******")
        self.driver = setup
        self.driver.get(self.loginURL)
        self.Login = LoginPage(self.driver)
        time.sleep(2)
        self.Login.set_login_email(self.login_email)
        self.Login.set_login_pass(self.login_pass)
        self.Login.set_owner_id(self.owner_id)
        self.Login.click_login_button()
        time.sleep(2)
        self.Login.click_logout_button()
        time.sleep(2)
        self.Login.click_cancel_logout_button()

        act_title = self.driver.title

        if act_title == "Scan4Discount":
            assert True
            self.logger.info("*******  User remained logged In *******")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_cancel_logout_Pass.png")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_cancel_logout_Fail.png")
            self.driver.close()
            self.logger.info("*******  User Log out failed *******")
            assert False





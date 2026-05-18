import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageObjects.Dashboard import DashboardPage
from PageObjects.Login import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
import time


class TestDashboard:
    loginURL = ReadConfig.get_loginURL()
    # login fields
    login_email = ReadConfig.get_login_email()
    login_pass = ReadConfig.get_login_pass()
    owner_id = ReadConfig.get_owner_id()
    # dashboard fields
    dashboard_URL = ReadConfig.get_dashboard_url()
    mode_btn = ReadConfig.get_mode_btn()
    guide_btn = ReadConfig.get_guide_btn()
    overview_page = ReadConfig.get_overview_page()
    customers_page = ReadConfig.get_customers_page()
    stores_page = ReadConfig.get_stores_page()
    discounts_page = ReadConfig.get_discounts_page()
    rewards_page = ReadConfig.get_rewards_page()
    coupons_page = ReadConfig.get_coupons_page()
    activity_page = ReadConfig.get_activity_page()

    logger = LogGen.loggen()


    def test_Dashboard_page(self, setup):
        self.logger.info("*******  Verifying Shop Owner Dashboard Page  *******")
        self.driver = setup
        self.driver.get(self.loginURL)
        self.driver.get(self.dashboard_URL)
        self.Login = LoginPage(self.driver)
        self.Dashboard = DashboardPage(self.driver)
        time.sleep(2)
        self.Login.set_login_email(self.login_email)
        self.Login.set_login_pass(self.login_pass)
        self.Login.set_owner_id(self.owner_id)
        self.Login.click_login_button()
        time.sleep(3)
        act_title = self.driver.title

        if act_title == "Scan4Discount":
            assert True
            self.logger.info("*******  Dashboard page launched successfully *******")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Dashboard_page_Pass.png")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Dashboard_page_Fail.png")
            self.driver.close()
            self.logger.info("*******  Dashboard page failed to launch *******")
            assert False


    def test_customers_page(self, setup):
        self.logger.info("*******  Verifying Customers Dashboard Page  *******")
        self.driver = setup
        self.driver.get(self.loginURL)
        self.driver.get(self.dashboard_URL)
        self.Login = LoginPage(self.driver)
        self.Dashboard = DashboardPage(self.driver)
        time.sleep(2)
        self.Login.set_login_email(self.login_email)
        self.Login.set_login_pass(self.login_pass)
        self.Login.set_owner_id(self.owner_id)
        self.Login.click_login_button()
        time.sleep(3)
        self.Dashboard.click_customers_button()

        act_title = self.driver.title

        if act_title == "Scan4Discount":
            assert True
            self.logger.info("*******  Customers page launched successfully *******")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_customers_page_Pass.png")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_customers_page_Fail.png")
            self.driver.close()
            self.logger.info("*******  Customers page failed to launch *******")
            assert False


    def test_stores_page(self, setup):
        self.logger.info("*******  Verifying Stores Dashboard Page  *******")
        self.driver = setup
        self.driver.get(self.loginURL)
        self.driver.get(self.dashboard_URL)
        self.Login = LoginPage(self.driver)
        self.Dashboard = DashboardPage(self.driver)
        time.sleep(2)
        self.Login.set_login_email(self.login_email)
        self.Login.set_login_pass(self.login_pass)
        self.Login.set_owner_id(self.owner_id)
        self.Login.click_login_button()
        time.sleep(3)
        self.Dashboard.click_stores_button()

        act_title = self.driver.title

        if act_title == "Scan4Discount":
            assert True
            self.logger.info("*******  Stores page launched successfully *******")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_stores_page_Pass.png")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_stores_page_Fail.png")
            self.driver.close()
            self.logger.info("*******  Stores page failed to launch *******")
            assert False


    def test_discounts_page(self, setup):
        self.logger.info("*******  Verifying Discounts Dashboard Page  *******")
        self.driver = setup
        self.driver.get(self.loginURL)
        self.driver.get(self.dashboard_URL)
        self.Login = LoginPage(self.driver)
        self.Dashboard = DashboardPage(self.driver)
        time.sleep(2)
        self.Login.set_login_email(self.login_email)
        self.Login.set_login_pass(self.login_pass)
        self.Login.set_owner_id(self.owner_id)
        self.Login.click_login_button()
        time.sleep(3)
        self.Dashboard.click_discount_button()

        act_title = self.driver.title

        if act_title == "Scan4Discount":
            assert True
            self.logger.info("*******  Discounts page launched successfully *******")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_discounts_page_Pass.png")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_discounts_page_Fail.png")
            self.driver.close()
            self.logger.info("*******  Discounts page failed to launch *******")
            assert False


    def test_rewards_page(self, setup):
        self.logger.info("*******  Verifying Rewards Dashboard Page  *******")
        self.driver = setup
        self.driver.get(self.loginURL)
        self.driver.get(self.dashboard_URL)
        self.Login = LoginPage(self.driver)
        self.Dashboard = DashboardPage(self.driver)
        time.sleep(2)
        self.Login.set_login_email(self.login_email)
        self.Login.set_login_pass(self.login_pass)
        self.Login.set_owner_id(self.owner_id)
        self.Login.click_login_button()
        time.sleep(3)
        self.Dashboard.click_rewards_button()

        act_title = self.driver.title

        if act_title == "Scan4Discount":
            assert True
            self.logger.info("*******  Rewards page launched successfully *******")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_rewards_page_Pass.png")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_rewards_page_Fail.png")
            self.driver.close()
            self.logger.info("*******  Rewards page failed to launch *******")
            assert False


    def test_coupons_page(self, setup):
        self.logger.info("*******  Verifying Coupons Dashboard Page  *******")
        self.driver = setup
        self.driver.get(self.loginURL)
        self.driver.get(self.dashboard_URL)
        self.Login = LoginPage(self.driver)
        self.Dashboard = DashboardPage(self.driver)
        time.sleep(2)
        self.Login.set_login_email(self.login_email)
        self.Login.set_login_pass(self.login_pass)
        self.Login.set_owner_id(self.owner_id)
        self.Login.click_login_button()
        time.sleep(3)
        self.Dashboard.click_coupons_button()

        act_title = self.driver.title

        if act_title == "Scan4Discount":
            assert True
            self.logger.info("*******  Coupons page launched successfully *******")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_coupons_page_Pass.png")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_coupons_page_Fail.png")
            self.driver.close()
            self.logger.info("*******  Coupons page failed to launch *******")
            assert False


    def test_activity_page(self, setup):
        self.logger.info("*******  Verifying Activity Dashboard Page  *******")
        self.driver = setup
        self.driver.get(self.loginURL)
        self.driver.get(self.dashboard_URL)
        self.Login = LoginPage(self.driver)
        self.Dashboard = DashboardPage(self.driver)
        time.sleep(2)
        self.Login.set_login_email(self.login_email)
        self.Login.set_login_pass(self.login_pass)
        self.Login.set_owner_id(self.owner_id)
        self.Login.click_login_button()
        time.sleep(4)
        self.Dashboard.click_activity_button()

        act_title = self.driver.title

        if act_title == "Scan4Discount":
            assert True
            self.logger.info("*******  Activity page launched successfully *******")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_activity_page_Pass.png")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_activity_page_Fail.png")
            self.driver.close()
            self.logger.info("*******  Activity page failed to launch *******")
            assert False




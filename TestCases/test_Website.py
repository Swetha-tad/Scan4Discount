import unittest

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageObjects.Website import HomePage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
import time
from Utilities.csv_utils import read_csv_data
from Utilities.json_utils import read_json_data
from Utilities.excel_utils import read_signup_data


class Test_Website:
    baseURL = ReadConfig.get_ApplicationURL()
    valid_email = ReadConfig.get_valid_email()
    Invalid_email = ReadConfig.get_Invalid_email()
    features_url = ReadConfig.get_FeaturesURL()
    pricing_url = ReadConfig.get_PricingURL()
    button_pricing1 = ReadConfig.get_button_pricing1()
    button_pricing2 = ReadConfig.get_button_pricing2()
    blogs_url = ReadConfig.get_BlogsURL()
    docs_url = ReadConfig.get_DocsURL()
    faqs_url = ReadConfig.get_FAQsURL()
    contactus_url = ReadConfig.get_ContactUs_URL()

    logger = LogGen.loggen()

    def test_HomePageTitle(self,setup):
        self.logger.info("*******  Verifying Home Page Title  *******")
        self.driver = setup
        self.driver.get(self.baseURL)

        #time.sleep(2)
        act_title = self.driver.title

        if act_title == "Scan4Discount":
            assert True
            self.driver.close()
            self.logger.info("*******  Home Page Title test is successful *******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_HomePageTitle.png")
            self.driver.close()
            self.logger.info("*******  Home Page Title test is Failed *******")
            assert False


    def test_watch_demo_button(self,setup):
        self.logger.info("*******  Verifying Watch Demo button  *******")
        self.driver = setup
        self.driver.get(self.baseURL)

        time.sleep(2)
        self.Website = HomePage(self.driver)

        self.Website.click_watch_demo()
        self.driver.save_screenshot(".\\Screenshots\\" + "test_watch_demo_button.png")
        self.driver.close()
        self.logger.info("*******  Watch Demo button is working fine *******")


    def test_Get_Started_button(self,setup):
        self.logger.info("*******  Verifying Get_Started_button  *******")
        self.driver = setup
        self.driver.get(self.baseURL)

        time.sleep(2)
        self.Website = HomePage(self.driver)

        self.Website.click_get_started()
        act_title = self.driver.title

        if act_title == "Scan4Discount":
            assert True
            self.driver.close()
            self.logger.info("*******  Get Started button is working fine *******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Get_Started_button.png")
            self.driver.close()
            self.logger.info("*******  Get Started button is not working fine *******")
            assert False



    def test_Get_Started_Now_button(self,setup):
        self.logger.info("*******  Verifying Get_Started_Now_button  *******")
        self.driver = setup
        self.driver.get(self.baseURL)

        time.sleep(2)
        self.Website = HomePage(self.driver)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.Website.click_get_started_now()
        act_title = self.driver.title

        if act_title == "Scan4Discount":
            assert True
            self.driver.close()
            self.logger.info("*******  Get Started Now button is working fine *******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Get_Started_Now_button.png")
            self.driver.close()
            self.logger.info("*******  Get Started Now button is not working fine *******")
            assert False



    def test_Request_Demo_button(self,setup):
        self.logger.info("*******  Verifying Request_Demo_button  *******")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.Website = HomePage(self.driver)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.Website.click_request_demo()
        act_title = self.driver.title

        if act_title == "Scan4Discount":
            assert True
            self.driver.close()
            self.logger.info("*******  Request Demo button is working fine *******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_Request_Demo_button.png")
            self.driver.close()
            self.logger.info("*******  Request Demo button is not working fine *******")
            assert False


    def test_validate_email(self,setup):
        self.logger.info("*******  Verifying Email-validation  *******")
        self.driver = setup
        self.driver.get(self.baseURL)

        time.sleep(2)
        self.Website = HomePage(self.driver)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.Website.set_email(self.valid_email)
        self.Website.click_subscribe()
        time.sleep(2)
        self.driver.save_screenshot(".\\Screenshots\\" + "test_validate_email.png")
        self.driver.close()
        self.logger.info("*******  Valid Email verification test is successful *******")


    def test_invalid_email(self,setup):
        self.logger.info("*******  Verifying Email-validation  *******")
        self.driver = setup
        self.driver.get(self.baseURL)

        time.sleep(2)
        self.Website = HomePage(self.driver)

        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        self.Website.set_email(self.Invalid_email)
        self.Website.click_subscribe()
        time.sleep(2)
        self.driver.save_screenshot(".\\Screenshots\\" + "test_invalid_email.png")
        self.driver.close()
        self.logger.info("*******  InValid Email verification test is successful *******")


    def test_features_page(self,setup):
        self.logger.info("*******  Verifying Feature Page  *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.Website = HomePage(self.driver)

        self.Website.click_features()
        time.sleep(2)
        self.driver.save_screenshot(".\\Screenshots\\" + "test_features_page.png")
        self.driver.close()
        self.logger.info("*******  Features page loaded successfully *******")

    def test_pricing_page(self,setup):
        self.logger.info("*******  Verifying Pricing Page  *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.Website = HomePage(self.driver)

        self.Website.click_pricing()
        time.sleep(2)
        self.driver.save_screenshot(".\\Screenshots\\" + "test_monthly_pricing.png")

        self.Website.click_button_pricing1()
        time.sleep(2)
        self.driver.save_screenshot(".\\Screenshots\\" + "test_quarterly_pricing.png")

        self.Website.click_button_pricing2()
        time.sleep(2)
        self.driver.save_screenshot(".\\Screenshots\\" + "test_yearly_pricing.png")
        self.driver.close()
        self.logger.info("*******  All subscription plan details captured successfully  *******")


    def test_blogs_page(self,setup):
        self.logger.info("*******  Verifying Blogs Page  *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.Website = HomePage(self.driver)

        self.Website.click_blogs()
        time.sleep(2)
        self.driver.save_screenshot(".\\Screenshots\\" + "test_blogs_page.png")
        self.driver.close()
        self.logger.info("*******  Blogs page loaded successfully  *******")


    def test_docs_page(self,setup):
        self.logger.info("*******  Verifying Documents Page  *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.Website = HomePage(self.driver)

        self.Website.click_docs()
        time.sleep(2)
        self.driver.save_screenshot(".\\Screenshots\\" + "test_docs_page.png")
        self.driver.close()
        self.logger.info("*******  Documents page loaded successfully  *******")


    def test_FAQs_page(self,setup):
        self.logger.info("*******  Verifying FAQ Page  *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.Website = HomePage(self.driver)

        self.Website.click_faqs()
        time.sleep(2)
        self.driver.save_screenshot(".\\Screenshots\\" + "test_FAQs_page.png")
        self.driver.close()
        self.logger.info("*******  FAQs page loaded successfully  *******")

    def test_ContactUs_page(self,setup):
        self.logger.info("*******  Verifying Contact Us Page  *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.Website = HomePage(self.driver)

        self.Website.click_contact_us()
        time.sleep(2)
        self.driver.save_screenshot(".\\Screenshots\\" + "test_Contact Us_page.png")
        self.driver.close()
        self.logger.info("*******  Contact Us page loaded successfully  *******")

    # Load the data from the TestData folder
    test_data1 = read_csv_data('TestData/invalid_data.csv')

    @pytest.mark.parametrize("data", test_data1)
    def test_form_submission_Invalid_data(self,setup, data):
        self.logger.info("*******  Verifying Form Submission with InValid Data  *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.Website = HomePage(self.driver)

        self.Website.click_contact_us()
        time.sleep(2)

        self.driver.find_element(By.NAME, "name").send_keys(data['name'])
        self.driver.find_element(By.NAME, "email").send_keys(data['email'])
        self.driver.find_element(By.NAME, "shopName").send_keys(data['shop_name'])
        self.driver.find_element(By.NAME, "message").send_keys(data['message'])

        self.driver.find_element(By.XPATH, "(//button[normalize-space()='Send Message'])[1]").click()
        time.sleep(2)
        self.driver.save_screenshot(".\\Screenshots\\" + "test_form_submission_Invalid_data.png")
        self.driver.close()
        self.logger.info("*******  Form submission with In-Valid Data  *******")



    # Load the data from the TestData folder
    test_data2 = read_json_data('TestData/valid_data.json')

    @pytest.mark.parametrize("data", test_data2)
    def test_form_submission_Valid_data(self, setup, data):
        self.logger.info("*******  Verifying Form Submission with Valid Data  *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.Website = HomePage(self.driver)

        self.Website.click_contact_us()
        time.sleep(2)

        self.driver.find_element(By.NAME, "name").send_keys(data['name'])
        self.driver.find_element(By.NAME, "email").send_keys(data['email'])
        self.driver.find_element(By.NAME, "shopName").send_keys(data['shop_name'])
        self.driver.find_element(By.NAME, "message").send_keys(data['message'])

        self.driver.find_element(By.XPATH, "(//button[normalize-space()='Send Message'])[1]").click()
        time.sleep(2)
        self.driver.save_screenshot(".\\Screenshots\\" + "test_form_submission_Valid_data.png")
        self.driver.close()
        self.logger.info("*******  Form submission with Valid Data  *******")


    def test_signin_page(self,setup):
        self.logger.info("*******  Verifying Signin button redirects to Signin page *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.Website = HomePage(self.driver)

        self.Website.click_signin()
        time.sleep(2)

        all_tabs = self.driver.window_handles
        self.driver.switch_to.window(all_tabs[1])
        self.driver.save_screenshot(".\\Screenshots\\" + "test_signin_page.png")
        self.driver.switch_to.window(all_tabs[0])
        self.driver.close()
        self.logger.info("*******  Signin page loaded successfully  *******")


    def test_signup_page(self,setup):
        self.logger.info("*******  Verifying Signup button redirects to Registration page *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.Website = HomePage(self.driver)

        self.Website.click_signup()
        time.sleep(2)

        self.driver.save_screenshot(".\\Screenshots\\" + "test_signup_page.png")
        self.driver.close()
        self.logger.info("*******  SignUp page loaded successfully  *******")


    excel_data = read_signup_data('TestData/Enquiry_form_data.xlsx', 'Sheet1')

    @pytest.mark.parametrize("ShopName, OwnerName, EmailAddress, PhoneNumber, City, Message", excel_data)
    def test_register_shop_form(self,setup, ShopName, OwnerName, EmailAddress, PhoneNumber, City, Message):
        self.logger.info("*******  Verifying Registration page *******")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.Website = HomePage(self.driver)

        self.Website.click_signup()
        time.sleep(2)

        # Fill form
        self.driver.find_element(By.NAME, "shopName").send_keys(ShopName)
        self.driver.find_element(By.NAME, "ownerName").send_keys(OwnerName)
        self.driver.find_element(By.NAME, "email").send_keys(EmailAddress)
        self.driver.find_element(By.NAME, "phone").send_keys(PhoneNumber)
        self.driver.find_element(By.NAME, "city").send_keys(City)
        self.driver.find_element(By.NAME, "message").send_keys(Message)
        self.driver.find_element(By.XPATH, "(//button[normalize-space()='Submit Request'])[1]").click()

        self.driver.save_screenshot(".\\Screenshots\\" + "test_register_shop_form.png")
        self.driver.close()
        self.logger.info("*******  Registration form Test completed successfully  *******")
















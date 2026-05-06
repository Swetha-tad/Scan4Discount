from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    # Home page
    link_home_xpath = "(//a[@class='transition text-yellow-400 font-semibold'])[1]"
    button_get_started_xpath = "(//button[normalize-space()='Get Started'])[1]"
    button_get_started_now_xpath = "(//a[normalize-space()='Get Started Now'])[1]"
    button_request_demo_xpath = "//a[normalize-space()='Request Demo']"
    textbox_email_xpath = "//input[@placeholder='Enter your email']"
    button_subscribe_xpath = "//button[normalize-space()='Subscribe']"
    # Features page
    link_features_xpath = "//a[contains(text(), 'Features')]"
    # Pricing page
    link_pricing_xpath = "//a[contains(text(), 'Pricing')]"
    button_pricing1_xpath = "(//button[normalize-space()='Quarterly'])[1]"
    button_pricing2_xpath = "(//button[normalize-space()='Yearly'])[1]"
    # Blogs page
    link_blogs_xpath = "//a[contains(text(), 'Blogs')]"
    # Documents page
    link_docs_xpath = "//a[contains(text(), 'Documents')]"
    # FAQS page
    link_faqs_xpath = "//a[contains(text(), 'FAQs')]"
    # Contact Us page
    link_contact_us_xpath = "//a[contains(text(), 'Contact us')]"
    # Sign in Page
    button_signin_xpath = "//a[contains(text(), 'Sign In')]"
    # Sign Up Page
    button_signup_xpath = "//a[contains(text(), 'Sign Up')]"


    def __init__(self, driver):
        self.driver = driver

    def click_link_home(self):
        self.driver.find_element(By.XPATH,self.link_home_xpath).click()

    def click_get_started(self):
        self.driver.find_element(By.XPATH,self.button_get_started_xpath).click()

    def click_get_started_now(self):
        self.driver.find_element(By.XPATH,self.button_get_started_now_xpath).click()

    def click_request_demo(self):
        self.driver.find_element(By.XPATH,self.button_request_demo_xpath).click()

    def set_email(self,email):
        self.driver.find_element(By.XPATH,self.textbox_email_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_email_xpath).send_keys(email)

    def click_subscribe(self):
        self.driver.find_element(By.XPATH,self.button_subscribe_xpath).click()

    def click_features(self):
        features = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.link_features_xpath))
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", features)
        features.click()

    def click_pricing(self):
        pricing = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.link_pricing_xpath))
        )
        pricing.click()

    def click_button_pricing1(self):
        self.driver.find_element(By.XPATH,self.button_pricing1_xpath).click()

    def click_button_pricing2(self):
        self.driver.find_element(By.XPATH,self.button_pricing2_xpath).click()

    def click_blogs(self):
        self.driver.find_element(By.XPATH, self.link_blogs_xpath).click()

    def click_docs(self):
        self.driver.find_element(By.XPATH, self.link_docs_xpath).click()

    def click_faqs(self):
        self.driver.find_element(By.XPATH, self.link_faqs_xpath).click()

    def click_contact_us(self):
        self.driver.find_element(By.XPATH, self.link_contact_us_xpath).click()

    def click_signin(self):
        self.driver.find_element(By.XPATH, self.button_signin_xpath).click()

    def click_signup(self):
        self.driver.find_element(By.XPATH, self.button_signup_xpath).click()






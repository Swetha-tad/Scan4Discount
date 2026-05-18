from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DashboardPage:
    btn_mode_xpath = "(//*[name()='svg'][contains(@class,'lucide lucide-moon w-7 h-7 text-slate-700 bg-amber-100 dark:bg-slate-800 rounded-full p-1 shadow-sm')])[2]"
    btn_guide_xpath = "(//button[@class='flex items-center gap-2 px-3 md:px-4 py-2 bg-yellow-500 hover:bg-yellow-400 text-black rounded-lg font-semibold text-xs md:text-sm transition-all shadow-lg hover:shadow-xl'])[1]"
    btn_overview_xpath = "(//button[normalize-space()='Overview'])[1]"
    btn_customers_xpath = "(//button[normalize-space()='Customers'])[1]"
    btn_stores_xpath = "(//button[normalize-space()='Stores'])[1]"
    btn_discounts_xpath = "(//button[normalize-space()='Discounts'])[1]"
    btn_rewards_xpath = "(//button[normalize-space()='Rewards'])[1]"
    btn_coupons_xpath = "(//button[normalize-space()='Coupons'])[1]"
    btn_activity_xpath = "(//button[normalize-space()='Activity'])[1]"

    def __init__(self, driver):
        self.driver = driver

    def click_mode_btn(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_mode_xpath))
        ).click()

    def click_guide_button(self):
        WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, self.btn_guide_xpath))
            ).click()

    def click_overview_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_overview_xpath))
        ).click()

    def click_customers_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_customers_xpath))
        ).click()

    def click_stores_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_stores_xpath))
        ).click()

    def click_discount_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_discounts_xpath))
        ).click()

    def click_rewards_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_rewards_xpath))
        ).click()

    def click_coupons_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_coupons_xpath))
        ).click()

    def click_activity_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.btn_activity_xpath))
        ).click()


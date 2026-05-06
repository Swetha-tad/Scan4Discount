from selenium import webdriver
import allure


@allure.feature("Website Dashboard Test")
@allure.story("Open Website")
@allure.severity(allure.severity_level.CRITICAL)


def test_Home():
    driver = webdriver.Chrome()
    driver.get("https://scan4discount.com/in")
    with allure.step("Get the Page title"):

        title = driver.title
        print(title)

    driver.quit()
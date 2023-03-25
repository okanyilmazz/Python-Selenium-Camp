from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Test_Sauce_Work:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    sleep(2)


    def test_null_login(self):
        loginBtn = self.driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        errorMessage = self.driver.find_element(
            By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Username is required"
        print(f"Null Login Test: {testResult}")

    def test_null_password(self):
        usernameInput = self.driver.find_element(By.ID, "user-name")
        sleep(1)
        usernameInput.send_keys("1")
        loginBtn = self.driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        errorMessage = self.driver.find_element(
            By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Password is required"
        print(f"Null Password Test: {testResult}")

    def test_locked_user(self):
        usernameInput = self.driver.find_element(By.ID, "user-name")
        passwordInput = self.driver.find_element(By.ID, "password")
        sleep(5)
        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        errorMessage = self.driver.find_element(
            By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        testResult = errorMessage.text == "Epic sadface: Sorry, this user has been locked out."
        print(f"Locked User Test: {testResult}")

    def show_error_icon_test(self):
        loginBtn = self.driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        sleep(2)
        errorIcons = self.driver.find_elements(By.CLASS_NAME, "error_icon")
        if (errorIcons.__len__() > 1):
            print(f"Error Icon Test : {True}")
        else:
            print(f"Error Icon Test : {False}")
        closeButton = self.driver.find_element(By.CLASS_NAME, "error-button")
        sleep(1)
        closeButton.click()
        sleep(1)

        # 1. Yöntem
        errorIcons = self.driver.find_elements(By.CLASS_NAME, "error_icon")
        if (errorIcons.__len__() > 1):
            print(f"Error icon not appearing after clicking X Button: {False}")
        else:
            print(f"Error icon not appearing after clicking X Button: {True}")

        # 2. Yöntem
        # try: self.driver.find_element(By.CLASS_NAME,"error_icon")
        # except NoSuchElementException:
        #     return print(f"Error icon not appearing after clicking X Button: {True}")
        # return False

    def login_standard_user(self):
        usernameInput = self.driver.find_element(By.ID, "user-name")
        passwordInput = self.driver.find_element(By.ID, "password")
        sleep(1)
        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")
        loginBtn = self.driver.find_element(By.ID, "login-button")
        sleep(2)
        loginBtn.click()
        sleep(2)
        get_url = self.driver.current_url
        if (get_url == "https://www.saucedemo.com/inventory.html"):
            print(f"is the current url equal to /inventory.html : {True}")
        else:
            print(False)

    def show_product_count(self):
        self.login_standard_user()
        sleep(2)
        productList = self.driver.find_elements(
            By.CLASS_NAME, "inventory_item")
        if (productList.__len__() == 6):
            print(f"Product count equal to 6 : {True}")
        else:
            print(f"Product count equal to 6 : {False}")
 

testClass = Test_Sauce_Work()
# testClass.test_null_login()
# testClass.test_null_password()
# testClass.test_locked_user()
# testClass.show_error_icon_test()
# testClass.login_standard_user()
testClass.show_product_count()

while True:
    continue

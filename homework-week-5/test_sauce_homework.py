from datetime import date
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import pytest
from pathlib import Path


class Test_Sauce_Work:
    def setup_method(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.folderPath = str(date.today())
        Path("homework-week-4/"+self.folderPath).mkdir(exist_ok=True)

    def teardown_method(self):
        self.driver.quit()

    def getData():
        return [("1", "1"), ("okan", "yilmaz"), ("user", "test"), ("secure", "login")]

    def test_null_login(self):
        self.waitForElementVisible((By.ID, 'login-button'))
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(
            By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(
            "homework-week-4/"+self.folderPath+"/test-null-login.png")
        assert errorMessage.text == "Epic sadface: Username is required"

    def test_null_password(self):
        self.waitForElementVisible((By.ID, 'user-name'))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        usernameInput.send_keys("1")
        self.waitForElementVisible((By.ID, 'login-button'))
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(
            By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(
            "homework-week-4/"+self.folderPath+"/test-null-password.png")
        assert errorMessage.text == "Epic sadface: Password is required"

    def test_locked_user(self):
        self.waitForElementVisible((By.ID, 'user-name'))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, 'password'))
        passwordInput = self.driver.find_element(By.ID, "password")

        usernameInput.send_keys("locked_out_user")
        passwordInput.send_keys("secret_sauce")
        self.waitForElementVisible((By.ID, 'login-button'))
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(
            By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(
            "homework-week-4/"+self.folderPath+"/test-locked_user.png")
        assert errorMessage.text == "Epic sadface: Sorry, this user has been locked out."

    def test_show_error_icon_test(self):
        self.waitForElementVisible((By.ID, 'login-button'))
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        self.waitForElementVisible((By.CLASS_NAME, 'error_icon'))
        errorIcons = self.driver.find_elements(By.CLASS_NAME, "error_icon")

        if (errorIcons.__len__() > 1):
            self.driver.save_screenshot(
                "homework-week-4/"+self.folderPath+"/test_show_error_icon.png")
            assert True
        else:
            assert False

        self.waitForElementVisible((By.CLASS_NAME, 'error-button'))
        closeButton = self.driver.find_element(By.CLASS_NAME, "error-button")
        closeButton.click()

        # 1. Yöntem
        errorIcons = self.driver.find_elements(By.CLASS_NAME, "error_icon")
        if (errorIcons.__len__() > 1):

            assert False
        else:
            self.driver.save_screenshot(
                "homework-week-4/"+self.folderPath+"/test_close_error_icon.png")
            assert True

        # 2. Yöntem
        # try: self.driver.find_element(By.CLASS_NAME,"error_icon")
        # except NoSuchElementException:
        #     return print(f"Error icon not appearing after clicking X Button: {True}")
        # return False

    def test_login_standard_user(self):
        self.waitForElementVisible((By.ID, 'user-name'))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, 'password'))
        passwordInput = self.driver.find_element(By.ID, "password")

        usernameInput.send_keys("standard_user")
        passwordInput.send_keys("secret_sauce")

        self.waitForElementVisible((By.ID, 'login-button'))
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()

        get_url = self.driver.current_url
        if (get_url == "https://www.saucedemo.com/inventory.html"):
            self.driver.save_screenshot(
                "homework-week-4/"+self.folderPath+"/test_login_standard_user.png")
            assert True
        else:
            assert False

    def test_show_product_count(self):
        self.test_login_standard_user()
        self.waitForElementVisible((By.CLASS_NAME, 'inventory_item'))
        productList = self.driver.find_elements(
            By.CLASS_NAME, "inventory_item")
        if (productList.__len__() == 6):
            self.driver.save_screenshot(
                "homework-week-4/"+self.folderPath+"/test_show_product_count.png")
            assert True
        else:
            assert False

    @pytest.mark.parametrize("username,password", getData())
    def test_invalid_login(self, username, password):
        self.waitForElementVisible((By.ID, 'user-name'))
        usernameInput = self.driver.find_element(By.ID, "user-name")
        self.waitForElementVisible((By.ID, 'password'))
        passwordInput = self.driver.find_element(By.ID, "password")
        usernameInput.send_keys(username)
        passwordInput.send_keys(password)
        self.waitForElementVisible((By.ID, 'login-button'))
        loginBtn = self.driver.find_element(By.ID, "login-button")
        loginBtn.click()
        errorMessage = self.driver.find_element(
            By.XPATH, "//*[@id='login_button_container']/div/form/div[3]/h3")
        self.driver.save_screenshot(
            "homework-week-4/"+self.folderPath+"/test-invalid-login-{username}-{password}.png")
        assert errorMessage.text == "Epic sadface: Username and password do not match any user in this service"

    def test_add_all_items_to_cart(self):
        self.test_login_standard_user()
        self.waitForElementVisible((By.CLASS_NAME, 'btn_inventory'))
        inventoryBtnList = self.driver.find_elements(
            By.CLASS_NAME, "btn_inventory")
        for inventoryBtn in inventoryBtnList:
            inventoryBtn.click()

        self.waitForElementVisible((By.CLASS_NAME, 'shopping_cart_container'))
        cartBtn = self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_container")
        cartBtn.click()

        self.waitForElementVisible((By.CLASS_NAME, 'cart_item'))
        itemList = self.driver.find_elements(By.CLASS_NAME, "cart_item")

        if (itemList.__len__() == 6):
            self.driver.save_screenshot(
                "homework-week-4/"+self.folderPath+"/test_add_all_items_to_cart.png")
            assert True
        else:
            assert False

    def test_confirm_order(self):
        self.test_add_all_items_to_cart()
        self.waitForElementVisible((By.ID, 'checkout'))
        checkoutBtn = self.driver.find_element(By.ID, 'checkout')
        checkoutBtn.click()

        self.waitForElementVisible((By.ID, 'first-name'))
        firstNameInput = self.driver.find_element(By.ID, "first-name")
        self.waitForElementVisible((By.ID, 'last-name'))
        lastNameInput = self.driver.find_element(By.ID, "last-name")
        self.waitForElementVisible((By.ID, 'postal-code'))
        postalCodeInput = self.driver.find_element(By.ID, "postal-code")

        firstNameInput.send_keys("Okan")
        lastNameInput.send_keys("Yılmaz")
        postalCodeInput.send_keys("0000")
        self.waitForElementVisible((By.ID, 'continue'))
        continueBtn = self.driver.find_element(By.ID, "continue")
        continueBtn.click()
        finishBtn = self.driver.find_element(By.ID, "finish")
        finishBtn.click()

        self.waitForElementVisible((By.CLASS_NAME, 'complete-text'))
        successMessage = self.driver.find_element(
            By.CLASS_NAME, 'complete-text')
        self.driver.save_screenshot(
            "homework-week-4/"+self.folderPath+"/test_confirm_order.png")
        assert successMessage.text == "Your order has been dispatched, and will arrive just as fast as the pony can get there!"

    def waitForElementVisible(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(
            ec.visibility_of_element_located(locator))

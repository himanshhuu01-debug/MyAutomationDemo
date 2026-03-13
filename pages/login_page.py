from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    # ── Locators ── apni site inspect karke update karo (F12)
    USERNAME_FIELD  = (By.XPATH, "//input[@id='username' or @id='email']")
    PASSWORD_FIELD  = (By.ID, "password")
    LOGIN_BUTTON    = (By.XPATH, "//button[@type='submit']")
    LOGOUT_BUTTON   = (By.XPATH, "//*[contains(text(),'Logout') or contains(text(),'logout')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait   = WebDriverWait(driver, 10)

    # ── Core Actions ──────────────────────────────────────────

    def enter_username(self, username):
        field = self.wait.until(EC.presence_of_element_located(self.USERNAME_FIELD))
        field.clear()
        field.send_keys(username)

    def enter_password(self, password):
        field = self.wait.until(EC.presence_of_element_located(self.PASSWORD_FIELD))
        field.clear()
        field.send_keys(password)

    def login_button(self):
        btn = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        btn.click()

    def logout(self):
        try:
            btn = self.wait.until(EC.element_to_be_clickable(self.LOGOUT_BUTTON))
            btn.click()
        except:
            pass

    # ── Visibility Helpers ────────────────────────────────────

    def is_username_field_visible(self):
        try:
            return self.driver.find_element(*self.USERNAME_FIELD).is_displayed()
        except:
            return False

    def is_password_field_visible(self):
        try:
            return self.driver.find_element(*self.PASSWORD_FIELD).is_displayed()
        except:
            return False

    def is_login_button_visible(self):
        try:
            return self.driver.find_element(*self.LOGIN_BUTTON).is_displayed()
        except:
            return False

    def is_login_button_enabled(self):
        try:
            return self.driver.find_element(*self.LOGIN_BUTTON).is_enabled()
        except:
            return False

    def is_password_masked(self):
        try:
            return self.driver.find_element(*self.PASSWORD_FIELD).get_attribute("type") == "password"
        except:
            return False

    # ── Value Helpers ─────────────────────────────────────────

    def get_username_value(self):
        try:
            return self.driver.find_element(*self.USERNAME_FIELD).get_attribute("value")
        except:
            return ""

    def get_username_placeholder(self):
        try:
            return self.driver.find_element(*self.USERNAME_FIELD).get_attribute("placeholder")
        except:
            return None

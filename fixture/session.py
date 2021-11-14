from selenium.webdriver.common.by import By
import time     # необходим для функции ожидания после логаута без которой тесты падают


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.driver
        self.app.open_home_page()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value=\'Login\']").click()

    def logout(self):
        wd = self.app.driver
        wd.find_element(By.LINK_TEXT, "Logout").click()
        time.sleep(0.5)     # замена на функцию wd.find_element(By.NAME, "user") не помогает, тесты все равно падают

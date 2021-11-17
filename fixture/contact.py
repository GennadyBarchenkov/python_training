from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_home_page(self):
        wd = self.app.driver
        if not (wd.current_url.endswith("/addressbook/")):
            wd.find_element(By.LINK_TEXT, "home").click()

    def create(self, contact):
        wd = self.app.driver
        # open add new page
        wd.find_element(By.LINK_TEXT, "add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element(By.XPATH, "(//input[@name=\'submit\'])[2]").click()
        self.open_home_page()

    def fill_contact_form(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.home_telephone)
        self.change_field_value("mobile", contact.mobile_telephone)
        self.change_field_value("work", contact.work_telephone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_datafield_value("bday", contact.bday)
        self.change_datafield_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_datafield_value("aday", contact.aday)
        self.change_datafield_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)

    def change_field_value(self, field_name, text):
        wd = self.app.driver
        if text is not None:
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def change_datafield_value(self, data_field_name, text):
        wd = self.app.driver
        if text is not None:
            Select(wd.find_element(By.NAME, data_field_name)).select_by_visible_text(text)

    def delete_first(self):
        wd = self.app.driver
        self.open_home_page()
        # select first contact
        wd.find_element(By.NAME, "selected[]").click()
        # submit deletion
        wd.find_element(By.XPATH, "//input[@value=\'Delete\']").click()
        # confirm deletion
        wd.switch_to.alert.accept()
        self.open_home_page()

    def modify_first_contact(self, new_contact_data):
        wd = self.app.driver
        self.open_home_page()
        # open edit contact
        wd.find_element(By.XPATH, "//img[@title=\'Edit\']").click()
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element(By.NAME, "update").click()
        self.open_home_page()

    def count(self):
        wd = self.app.driver
        self.open_home_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

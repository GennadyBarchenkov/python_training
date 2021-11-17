from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.driver
        # open add new page
        wd.find_element(By.LINK_TEXT, "add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element(By.XPATH, "(//input[@name=\'submit\'])[2]").click()
        self.return_to_home_page()

    def delete_first(self):
        wd = self.app.driver
        self.return_to_home_page()
        # select first contact
        wd.find_element(By.NAME, "selected[]").click()
        # submit deletion
        wd.find_element(By.XPATH, "//input[@value=\'Delete\']").click()
        # confirm deletion
        wd.switch_to.alert.accept()
        self.return_to_home_page()

    def edit_first(self, contact):
        wd = self.app.driver
        self.return_to_home_page()
        # open edit contact
        wd.find_element(By.XPATH, "//img[@title=\'Edit\']").click()
        self.fill_contact_form(contact)
        # submit contact update
        wd.find_element(By.NAME, "update").click()
        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.app.driver
        wd.find_element(By.LINK_TEXT, "home").click()

    def fill_contact_form(self, contact):
        wd = self.app.driver
        wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        wd.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        wd.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        wd.find_element(By.NAME, "title").send_keys(contact.title)
        wd.find_element(By.NAME, "company").send_keys(contact.company)
        wd.find_element(By.NAME, "address").send_keys(contact.address)
        wd.find_element(By.NAME, "home").send_keys(contact.home_telephone)
        wd.find_element(By.NAME, "mobile").send_keys(contact.mobile_telephone)
        wd.find_element(By.NAME, "work").send_keys(contact.work_telephone)
        wd.find_element(By.NAME, "fax").send_keys(contact.fax)
        wd.find_element(By.NAME, "email").send_keys(contact.email)
        wd.find_element(By.NAME, "email2").send_keys(contact.email2)
        wd.find_element(By.NAME, "email3").send_keys(contact.email3)
        wd.find_element(By.NAME, "homepage").send_keys(contact.homepage)
        select_element = wd.find_element(By.NAME, "bday")
        select_object = Select(select_element)
        select_object.select_by_visible_text('%s' % contact.bday)
        select_element = wd.find_element(By.NAME, "bmonth")
        select_object = Select(select_element)
        select_object.select_by_visible_text('%s' % contact.bmonth)
        wd.find_element(By.NAME, "byear").send_keys(contact.byear)
        select_element = wd.find_element(By.NAME, "aday")
        select_object = Select(select_element)
        select_object.select_by_visible_text('%s' % contact.aday)
        select_element = wd.find_element(By.NAME, "amonth")
        select_object = Select(select_element)
        select_object.select_by_visible_text('%s' % contact.amonth)
        wd.find_element(By.NAME, "byear").send_keys(contact.byear)
        wd.find_element(By.NAME, "ayear").send_keys(contact.ayear)
        wd.find_element(By.NAME, "address2").send_keys(contact.address2)
        wd.find_element(By.NAME, "phone2").send_keys(contact.phone2)

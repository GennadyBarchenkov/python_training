from selenium import webdriver
from selenium.webdriver.common.by import By
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.vars = {}
        self.session = SessionHelper(self)

    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")

    def open_groups_page(self):
        self.driver.find_element(By.LINK_TEXT, "groups").click()

    def create_group(self, group):
        self.open_groups_page()
        # init group creation
        self.driver.find_element(By.NAME, "new").click()
        # fill group form
        self.driver.find_element(By.NAME, "group_name").send_keys(group.name)
        self.driver.find_element(By.NAME, "group_header").send_keys(group.header)
        self.driver.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        self.driver.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        self.driver.find_element(By.LINK_TEXT, "group page").click()

    def create_new_contact(self, contact):
        # open add new page
        self.driver.find_element(By.LINK_TEXT, "add new").click()
        # fill contact form
        self.driver.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        self.driver.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        self.driver.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        self.driver.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        self.driver.find_element(By.NAME, "title").send_keys(contact.title)
        self.driver.find_element(By.NAME, "company").send_keys(contact.company)
        self.driver.find_element(By.NAME, "address").send_keys(contact.address)
        self.driver.find_element(By.NAME, "home").send_keys(contact.home_telephone)
        self.driver.find_element(By.NAME, "mobile").send_keys(contact.mobile_telephone)
        self.driver.find_element(By.NAME, "work").send_keys(contact.work_telephone)
        self.driver.find_element(By.NAME, "fax").send_keys(contact.fax)
        self.driver.find_element(By.NAME, "email").send_keys(contact.email)
        self.driver.find_element(By.NAME, "email2").send_keys(contact.email2)
        self.driver.find_element(By.NAME, "email3").send_keys(contact.email3)
        self.driver.find_element(By.NAME, "homepage").send_keys(contact.homepage)
        dropdown = self.driver.find_element(By.NAME, "bday")
        dropdown.find_element(By.XPATH, "//option[. = '%s']" % contact.bday).click()
        dropdown = self.driver.find_element(By.NAME, "bmonth")
        dropdown.find_element(By.XPATH, "//option[. = '%s']" % contact.bmonth).click()
        self.driver.find_element(By.NAME, "byear").send_keys(contact.byear)
        dropdown = self.driver.find_element(By.NAME, "aday")
        dropdown.find_element(By.XPATH, "//option[. = '%s']" % contact.aday).click()
        dropdown = self.driver.find_element(By.NAME, "amonth")
        dropdown.find_element(By.XPATH, "//option[. = '%s']" % contact.amonth).click()
        self.driver.find_element(By.NAME, "ayear").send_keys("%s" % contact.ayear)
        self.driver.find_element(By.NAME, "address2").send_keys(contact.address2)
        self.driver.find_element(By.NAME, "phone2").send_keys(contact.phone2)
        # submit contact creation
        self.driver.find_element(By.XPATH, "(//input[@name=\'submit\'])[2]").click()
        self.return_to_home_page()

    def return_to_home_page(self):
        self.driver.find_element(By.LINK_TEXT, "home").click()

    def destroy(self):
        self.driver.quit()

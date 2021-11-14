from selenium.webdriver.common.by import By


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.driver
        # open add new page
        wd.find_element(By.LINK_TEXT, "add new").click()
        # fill contact form
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
        dropdown = wd.find_element(By.NAME, "bday")
        dropdown.find_element(By.XPATH, "//option[. = '%s']" % contact.bday).click()
        dropdown = wd.find_element(By.NAME, "bmonth")
        dropdown.find_element(By.XPATH, "//option[. = '%s']" % contact.bmonth).click()
        wd.find_element(By.NAME, "byear").send_keys(contact.byear)
        dropdown = wd.find_element(By.NAME, "aday")
        dropdown.find_element(By.XPATH, "//option[. = '%s']" % contact.aday).click()
        dropdown = wd.find_element(By.NAME, "amonth")
        dropdown.find_element(By.XPATH, "//option[. = '%s']" % contact.amonth).click()
        wd.find_element(By.NAME, "ayear").send_keys("%s" % contact.ayear)
        wd.find_element(By.NAME, "address2").send_keys(contact.address2)
        wd.find_element(By.NAME, "phone2").send_keys(contact.phone2)
        # submit contact creation
        wd.find_element(By.XPATH, "(//input[@name=\'submit\'])[2]").click()
        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.app.driver
        wd.find_element(By.LINK_TEXT, "home").click()

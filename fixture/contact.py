from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from model.contact import Contact
import re


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
        wd.find_element(By.XPATH, "(//input[@name='submit'])[2]").click()
        self.open_home_page()
        self.contact_cache = None

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

    def select_first_contact(self):
        wd = self.app.driver
        wd.find_element(By.NAME, "selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.driver
        wd.find_elements(By.NAME, "selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.driver
        wd.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click()

    def delete_first(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.driver
        self.open_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        # confirm deletion
        wd.switch_to.alert.accept()
        wd.find_element(By.CSS_SELECTOR, "div.msgbox")
        self.open_home_page()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.driver
        self.open_home_page()
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        # confirm deletion
        wd.switch_to.alert.accept()
        wd.find_element(By.CSS_SELECTOR, "div.msgbox")
        self.open_home_page()
        self.contact_cache = None

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.driver
        self.open_home_page()
        # open edit contact
        wd.find_elements(By.XPATH, "//img[@title='Edit']")[index].click()
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element(By.NAME, "update").click()
        self.open_home_page()
        self.contact_cache = None

    def modify_contact_by_id(self, id, new_contact_data):
        wd = self.app.driver
        self.open_home_page()
        # open edit contact
        wd.find_element(By.CSS_SELECTOR, "a[href='edit.php?id=%s']" % id).click()
        self.fill_contact_form(new_contact_data)
        # submit modification
        wd.find_element(By.NAME, "update").click()
        self.open_home_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.driver
        self.open_home_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.driver
            self.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements(By.NAME, "entry"):
                cells = element.find_elements(By.TAG_NAME, "td")
                lastname_text = cells[1].text
                firstname_text = cells[2].text
                address_text = cells[3].text
                all_emails = cells[4].text
                id = cells[0].find_element(By.TAG_NAME, "input").get_attribute("value")
                all_phones = cells[5].text
                self.contact_cache.append(Contact(id=id, lastname=lastname_text, firstname=firstname_text,
                                                  address=address_text, all_emails_from_home_page=all_emails,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.driver
        self.open_home_page()
        row = wd.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[7]
        cell.find_element(By.TAG_NAME, "a").click()

    def open_contact_to_view_by_index(self, index):
        wd = self.app.driver
        self.open_home_page()
        row = wd.find_elements(By.NAME, "entry")[index]
        cell = row.find_elements(By.TAG_NAME, "td")[6]
        cell.find_element(By.TAG_NAME, "a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.driver
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element(By.NAME, "firstname").get_attribute("value")
        lastname = wd.find_element(By.NAME, "lastname").get_attribute("value")
        id = wd.find_element(By.NAME, "id").get_attribute("value")
        address = wd.find_element(By.NAME, "address").get_attribute("value")
        email = wd.find_element(By.NAME, "email").get_attribute("value")
        email2 = wd.find_element(By.NAME, "email2").get_attribute("value")
        email3 = wd.find_element(By.NAME, "email3").get_attribute("value")
        home_telephone = wd.find_element(By.NAME, "home").get_attribute("value")
        mobile_telephone = wd.find_element(By.NAME, "mobile").get_attribute("value")
        work_telephone = wd.find_element(By.NAME, "work").get_attribute("value")
        phone2 = wd.find_element(By.NAME, "phone2").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                       email=email, email2=email2, email3=email3,
                       home_telephone=home_telephone, mobile_telephone=mobile_telephone,
                       work_telephone=work_telephone, phone2=phone2)

    def get_contact_frow_view_page(self, index):
        wd = self.app.driver
        self.open_contact_to_view_by_index(index)
        text = wd.find_element(By.ID, "content").text
        home_telephone = re.search("H: (.*)", text).group(1)
        mobile_telephone = re.search("M: (.*)", text).group(1)
        work_telephone = re.search("W: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(home_telephone=home_telephone, mobile_telephone=mobile_telephone,
                       work_telephone=work_telephone, phone2=phone2)

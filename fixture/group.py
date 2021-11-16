from selenium.webdriver.common.by import By


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.driver
        wd.find_element(By.LINK_TEXT, "groups").click()

    def create(self, group):
        wd = self.app.driver
        self.open_groups_page()
        # init group creation
        wd.find_element(By.NAME, "new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

    def fill_group_form(self, group):
        wd = self.app.driver
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)

    def delete_first(self):
        wd = self.app.driver
        self.open_groups_page()
        # select first group
        wd.find_element(By.NAME, "selected[]").click()
        # submit deletion
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()

    def edit_first(self, group):
        wd = self.app.driver
        self.open_groups_page()
        # select first group
        wd.find_element(By.NAME, "selected[]").click()
        # submit edit
        wd.find_element(By.NAME, "edit").click()
        self.fill_group_form(group)
        # update group edit
        wd.find_element(By.NAME, "update").click()
        self.return_to_groups_page()

    def return_to_groups_page(self):
        wd = self.app.driver
        wd.find_element(By.LINK_TEXT, "group page").click()

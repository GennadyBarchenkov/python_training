import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name,user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.Connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname, nickname, company, title, address, home, mobile,"
                           "work, fax, email, email2, email3, homepage, bday, bmonth, byear, aday, amonth, ayear,"
                           "address2, phone2 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, company, title, address, home, mobile, work, fax, email,
                 email2, email3, homepage, bday, bmonth, byear, aday, amonth, ayear, address2, phone2) = row
                list.append(Contact(id=str(id), firstname=firstname, middlename=middlename, lastname=lastname,
                                    nickname=nickname, title=title, company=company, address=address, home_telephone=home,
                                    mobile_telephone=mobile, work_telephone=work, fax=fax, email=email, email2=email2,
                                    email3=email3, homepage=homepage, bday=bday, bmonth=bmonth, byear=byear, aday=aday,
                                    amonth=amonth, ayear=ayear, address2=address2, phone2=phone2))
        finally:
            cursor.close()
        return list

    def get_list_contacts_in_group(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, id from address_in_groups where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (group_id, id) = row
                list.append(Group(id=str(group_id)))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

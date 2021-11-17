from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.modify_first_contact(Contact(firstname="edit1", middlename="edit2", lastname="edit3",
                                   nickname="edit4", title="edit5", company="edit6", address="edit7",
                                   home_telephone="edit8", mobile_telephone="edit9", work_telephone="edit10",
                                   fax="edit11", email="edit12", email2="edit13", email3="edit14",
                                   homepage="edit15", bday="13", bmonth="December", byear="2000", aday="13",
                                   amonth="January", ayear="2000", address2="edit16", phone2="edit17"))

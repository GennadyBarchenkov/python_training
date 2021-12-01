from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="imya", middlename="otchestvo", lastname="familiya",
                      nickname="prozvishe", title="zagolovok", company="kompaniya", address="adres",
                      home_telephone="domashnii", mobile_telephone="mobilnii", work_telephone="rabochii",
                      fax="faks", email="miloraz", email2="milodva", email3="milotri",
                      homepage="domashnay_stranica", bday="1", bmonth="January", byear="2021", aday="1",
                      amonth="January", ayear="2021", address2="eshe_odin_adres", phone2="houm")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                      address="", home_telephone="", mobile_telephone="", work_telephone="", fax="",
                      email="", email2="", email3="", homepage="", bday="", bmonth="-", byear="", aday="",
                      amonth="-", ayear="", address2="", phone2="")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

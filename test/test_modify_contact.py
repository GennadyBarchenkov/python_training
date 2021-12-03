from time import sleep

from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", middlename="test", lastname="test", nickname="test", title="test",
                                   company="test", address="test", home_telephone="test", mobile_telephone="test",
                                   work_telephone="test", fax="test", email="test", email2="test", email3="test",
                                   homepage="test", bday="7", bmonth="May", byear="1900", aday="7", amonth="May",
                                   ayear="1900", address2="test", phone2="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="edit1", middlename="edit2", lastname="edit3",
                      nickname="edit4", title="edit5", company="edit6", address="edit7",
                      home_telephone="edit8", mobile_telephone="edit9", work_telephone="edit10",
                      fax="edit11", email="edit12", email2="edit13", email3="edit14",
                      homepage="edit15", bday="13", bmonth="December", byear="2000", aday="13",
                      amonth="January", ayear="2000", address2="edit16", phone2="edit17")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="New firstname")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="test"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(lastname="New lastname")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_bday(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(bday="7"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(bday="30")
    contact.id = old_contacts[0].id
    app.contact.modify_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

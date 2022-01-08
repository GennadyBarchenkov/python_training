from model.contact import Contact
import random


def test_full_edit_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test", middlename="test", lastname="test", nickname="test", title="test",
                                   company="test", address="test", home_telephone="test", mobile_telephone="test",
                                   work_telephone="test", fax="test", email="test", email2="test", email3="test",
                                   homepage="test", bday="7", bmonth="May", byear="1900", aday="7", amonth="May",
                                   ayear="1900", address2="test", phone2="test"))
    old_contacts = db.get_contact_list()
    contact = Contact(firstname="edit1", middlename="edit2", lastname="edit3",
                      nickname="edit4", title="edit5", company="edit6", address="edit7",
                      home_telephone="edit8", mobile_telephone="edit9", work_telephone="edit10",
                      fax="edit11", email="edit12", email2="edit13", email3="edit14",
                      homepage="edit15", bday="13", bmonth="December", byear="2000", aday="13",
                      amonth="January", ayear="2000", address2="edit16", phone2="edit17")
    select_contact = random.choice(old_contacts)
    index = old_contacts.index(Contact(id="%s" % select_contact.id))
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    old_contacts.remove(select_contact)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


def test_modify_contact_firstname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = Contact(firstname="New_firstname")
    select_contact = random.choice(old_contacts)
    index = old_contacts.index(Contact(id="%s" % select_contact.id))
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    old_contacts.remove(select_contact)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


def test_modify_contact_lastname(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(lastname="test"))
    old_contacts = db.get_contact_list()
    contact = Contact(lastname="New_lastname")
    select_contact = random.choice(old_contacts)
    index = old_contacts.index(Contact(id="%s" % select_contact.id))
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    old_contacts.remove(select_contact)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


def test_modify_contact_bday(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(bday="7"))
    old_contacts = db.get_contact_list()
    contact = Contact(bday="30")
    select_contact = random.choice(old_contacts)
    index = old_contacts.index(Contact(id="%s" % select_contact.id))
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = db.get_contact_list()
    old_contacts.remove(select_contact)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

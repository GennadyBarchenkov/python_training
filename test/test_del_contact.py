from model.contact import Contact
import random


def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    select_contact = random.choice(old_contacts)
    index = old_contacts.index(Contact(id="%s" % select_contact.id))
    app.contact.delete_contact_by_index(index)
    new_contacts = db.get_contact_list()
    old_contacts.remove(select_contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)

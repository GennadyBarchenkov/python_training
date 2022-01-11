from model.contact import Contact
from model.group import Group
import random


def test_add_contact_to_group(app, orm, db):
    # precondition
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    # choice random elements
    select_group = random.choice(db.get_group_list())
    select_contact = app.contact.random_contact_from_none_group()
    # get the contact list of a group before adding
    contacts_in_select_group = orm.get_contacts_in_group(Group(id="%s" % select_group.id))
    # adding a contact to a group
    app.contact.add_contact_to_group(select_contact.id, select_group.id)
    # get the contact list of a group after adding
    select_group_with_contact = orm.get_contacts_in_group(Group(id="%s" % select_group.id))
    # editing old list and assert
    contacts_in_select_group.append(select_contact)
    assert sorted(contacts_in_select_group, key=Contact.id_or_max) == sorted(select_group_with_contact, key=Contact.id_or_max)


def test_del_contact_from_group(app, orm, db):
    # precondition
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    # getting a list of groups that have contacts and check availability
    groups_with_contacts = db.get_list_contacts_in_group()
    if len(groups_with_contacts) == 0:
        random_contact = app.contact.random_contact_from_none_group()
        app.contact.add_contact_to_group(random_contact.id, random.choice(db.get_group_list()).id)
        groups_with_contacts = db.get_list_contacts_in_group()
    # choice random group from list
    select_group = random.choice(groups_with_contacts)
    # getting the contact list of a group before removing
    contacts_in_select_group = orm.get_contacts_in_group(Group(id="%s" % select_group.id))
    # choice random contact from list
    select_contact = random.choice(contacts_in_select_group)
    # removing a contact from a group
    app.contact.remove_contact_from_group(select_contact.id, select_group.id)
    # getting the contact list of a group after removing
    select_group_without_contact = orm.get_contacts_in_group(Group(id="%s" % select_group.id))
    # editing old list and assert
    contacts_in_select_group.remove(select_contact)
    assert sorted(contacts_in_select_group, key=Contact.id_or_max) == sorted(select_group_without_contact, key=Contact.id_or_max)

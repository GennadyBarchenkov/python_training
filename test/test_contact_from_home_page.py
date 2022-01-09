import re
from model.contact import Contact


def test_all_contacts_from_home_page_vs_db(app, db):
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    for i in range(len(contacts_from_home_page)):
        assert contacts_from_home_page[i].firstname == clear_space(contacts_from_db[i].firstname)
        assert contacts_from_home_page[i].lastname == clear_space(contacts_from_db[i].lastname)
        assert contacts_from_home_page[i].address == clear_space(contacts_from_db[i].address)
        assert contacts_from_home_page[i].all_emails_from_home_page == clear_space(merge_emails_like_on_home_page(
            contacts_from_db[i]))
        assert contacts_from_home_page[i].all_phones_from_home_page == clear_space(merge_phones_like_on_home_page(
            contacts_from_db[i]))


def clear(s):
    return re.sub("[() -]", "", s)


def clear_space(s):
    return re.sub(r'\s+$', "", s)


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None, [contact.email, contact.email2, contact.email3])))


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                     map(lambda x: clear(x),
                         filter(lambda x: x is not None,
                                [contact.home_telephone, contact.mobile_telephone, contact.work_telephone, contact.phone2]))))

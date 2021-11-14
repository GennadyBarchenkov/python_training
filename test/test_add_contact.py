import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_new_contact(Contact(firstname="imya", middlename="otchestvo", lastname="familiya",
                                   nickname="prozvishe", title="zagolovok", company="kompaniya", address="adres",
                                   home_telephone="domashnii", mobile_telephone="mobilnii", work_telephone="rabochii",
                                   fax="faks", email="miloraz", email2="milodva", email3="milotri",
                                   homepage="domashnay_stranica", bday="1", bmonth="January", byear="2021", aday="5",
                                   amonth="December", ayear="2022", address2="eshe_odin_adres", phone2="houm"))
    app.logout()


def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_new_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                                   address="", home_telephone="", mobile_telephone="", work_telephone="", fax="",
                                   email="", email2="", email3="", homepage="", bday="", bmonth="", byear="", aday="",
                                   amonth="", ayear="", address2="", phone2=""))
    app.logout()

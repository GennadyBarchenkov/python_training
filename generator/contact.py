from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_day():
    return "%s" % (random.randrange(1, 31))


def random_month():
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return random.choice(months)


def random_year():
    return "%s" % (random.randrange(1900, 2200))


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", home_telephone="",
                    mobile_telephone="", work_telephone="", fax="", email="", email2="", email3="", homepage="", bday="",
                    bmonth="-", byear="", aday="", amonth="-", ayear="", address2="", phone2="")] + [
    Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10), lastname=random_string("lastname", 10),
            nickname=random_string("nickname", 10), title=random_string("title", 10), company=random_string("company", 10),
            address=random_string("address", 10), home_telephone=random_string("home_telephone", 10), mobile_telephone=random_string("mobile_telephone", 10),
            work_telephone=random_string("work_telephone", 10), fax=random_string("fax", 10), email=random_string("email", 10),
            email2=random_string("email2", 10), email3=random_string("email3", 10), homepage=random_string("homepage", 10),
            bday=random_day(), bmonth=random_month(), byear=random_year(), aday=random_day(), amonth=random_month(), ayear=random_year(),
            address2=random_string("address2", 10), phone2=random_string("phone2", 10))
    for i in range(n)
]

#testdata = [
    #Contact(firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname, title=title, company=company,
    #                   address=address, home_telephone=home_telephone, mobile_telephone=mobile_telephone, work_telephone=work_telephone, fax=fax,
    #                   email=email, email2=email2, email3=email3, homepage=homepage, bday=bday, bmonth=bmonth, byear=byear, aday=aday,
    #                   amonth=amonth, ayear=ayear, address2=address2, phone2=phone2)
        #for firstname in ["", random_string("firstname", 10)]
    #for middlename in ["", random_string("middlename", 20)]
    #for lastname in ["", random_string("lastname", 20)]
    #for nickname in ["", random_string("nickname", 20)]
    #for title in ["", random_string("title", 20)]
    #for company in ["", random_string("company", 20)]
    #for address in ["", random_string("address", 20)]
    #for home_telephone in ["", random_string("home_telephone", 20)]
    #for mobile_telephone in ["", random_string("mobile_telephone", 20)]
    #for work_telephone in ["", random_string("work_telephone", 20)]
    #for fax in ["", random_string("fax", 20)]
    #for email in ["", random_string("email", 20)]
    #for email2 in ["", random_string("email2", 20)]
    #for email3 in ["", random_string("email3", 20)]
    #for homepage in ["", random_string("homepage", 20)]
    #for bday in ["", random_day()]
    #for bmonth in ["-", random_month()]
    #for byear in ["", random_year()]
    #for aday in ["", random_day()]
    #for amonth in ["-", random_month()]
    #for ayear in ["", random_year()]
    #for address2 in ["", random_string("address2", 20)]
    #for phone2 in ["", random_string("phone2", 20)]
#]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)


with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))

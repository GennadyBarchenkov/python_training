from model.group import Group


def test_edit_first_group(app):
    app.group.modify_first_group(Group(name="edit1", header="edit2", footer="edit3"))

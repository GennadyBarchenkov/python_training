from model.group import Group
import random


def test_full_edit_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test", header="test", footer="test"))
    old_groups = db.get_group_list()
    group = Group(name="edit1", header="edit2", footer="edit3")
    select_group = random.choice(old_groups)
    group.id = select_group.id
    app.group.modify_group_by_id(select_group.id, group)
    new_groups = db.get_group_list()
    old_groups.remove(select_group)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    group = Group(name="New Group")
    select_group = random.choice(old_groups)
    group.id = select_group.id
    app.group.modify_group_by_id(select_group.id, group)
    new_groups = db.get_group_list()
    old_groups.remove(select_group)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_modify_group_header(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(header="test"))
    old_groups = db.get_group_list()
    group = Group(header="New header")
    select_group = random.choice(old_groups)
    group.id = select_group.id
    app.group.modify_group_by_id(select_group.id, group)
    new_groups = db.get_group_list()
    old_groups.remove(select_group)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_modify_group_footer(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(footer="test"))
    old_groups = db.get_group_list()
    group = Group(footer="New footer")
    select_group = random.choice(old_groups)
    group.id = select_group.id
    app.group.modify_group_by_id(select_group.id, group)
    new_groups = db.get_group_list()
    old_groups.remove(select_group)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

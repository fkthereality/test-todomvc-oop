from tests import app


def test_open():
    app.open()


def test_add():
    app.open()
    app.add('a', 'b')
    app.assert_todos('a', 'b')
    app.items_left_should_be(2)


def test_edit_by_enter():
    app.open()
    app.add('a')
    app.edit('a', 'a edited')
    app.assert_todos('a edited')
    app.items_left_should_be(1)


def test_edit_by_tab():
    app.open()
    app.add('a')
    app.edit_by_tab('a', 'a edited')
    app.assert_todos('a edited')
    app.items_left_should_be(1)


def test_edit_by_control_enter():
    app.open()
    app.add('a')
    app.edit_by_control_enter('a', 'a edited')
    app.assert_todos('a edited')
    app.items_left_should_be(1)


def test_edit_by_click_outside():
    app.open()
    app.add('a')
    app.edit_by_click_outside('a', 'a edited')
    app.assert_todos('a edited')
    app.items_left_should_be(1)


def test_cancel_editing():
    app.open()
    app.add('a')
    app.cancel_editing_by_escape('a', 'a to be canceled')
    app.assert_todos('a')
    app.items_left_should_be(1)


def test_complete():
    app.open()
    app.add('a')
    app.complete('a')
    app.items_left_should_be(0)
    app.complete('a')
    app.items_left_should_be(1)


def test_toggle_all():
    app.open()
    app.add('a', 'b')
    app.toggle_all()
    app.items_left_should_be(0)
    app.toggle_all()
    app.items_left_should_be(2)


def test_clear_completed():
    app.open()
    app.add('a')
    app.complete('a')
    app.clear_completed()
    app.assert_todos()
    app.has_no_items_left_displayed()


def test_delete():
    app.open()
    app.add('a', 'b')
    app.delete('a')
    app.assert_todos('b')
    app.items_left_should_be(1)


def test_delete_edit_to_blanc():
    app.open()
    app.add('a', 'b')
    app.edit('a', '')
    app.edit('b', '')
    app.assert_todos()
    app.has_no_items_left_displayed()

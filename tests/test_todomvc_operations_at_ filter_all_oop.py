from tests import app

"""
Suppositions

NOTE: asserts names are configured as simplest read. 
Not consistent but readable

I use a minimum of todo in all tests.
In addition to tests, where need to check several todos 

NOTE: we need to know that ALL preconditions are worked properly
"""


def test_open():

    app.open()

    app.todos_should_be()
    app.footer_should_be_hidden()


def test_add():
    app.open()

    app.add('a')

    app.todos_should_be('a')
    app.items_left_should_be(1)
    app.footer_should_be_visible()
    app.clear_completed_should_be_hidden()


def test_add_several():
    app.open()

    app.add('a', 'b', 'c')

    app.todos_should_be('a', 'b', 'c')
    app.items_left_should_be(3)
    app.footer_should_be_visible()
    app.clear_completed_should_be_hidden()


def test_add_nothing():
    app.open()

    app.add()

    app.todos_should_be()
    app.footer_should_be_hidden()
    app.clear_completed_should_be_hidden()


def test_edit_by_enter():
    app.open()
    app.add('a')

    app.edit('a', 'a edited')

    app.todos_should_be('a edited')
    app.items_left_should_be(1)
    app.footer_should_be_visible()
    app.clear_completed_should_be_hidden()


def test_edit_by_tab():
    app.open()
    app.add('a')

    app.edit_by_tab('a', 'a edited')

    app.todos_should_be('a edited')
    app.items_left_should_be(1)
    app.footer_should_be_visible()
    app.clear_completed_should_be_hidden()


def test_edit_by_click_outside():
    app.open()
    app.add('a')

    app.edit_by_click_outside('a', 'a edited')

    app.todos_should_be('a edited')
    app.items_left_should_be(1)
    app.footer_should_be_visible()
    app.clear_completed_should_be_hidden()


def test_edit_by_control_enter():
    app.open()
    app.add('a')

    app.edit_by_control_enter('a', 'a edited')

    app.todos_should_be('a edited')
    app.items_left_should_be(1)
    app.footer_should_be_visible()
    app.clear_completed_should_be_hidden()


def test_edit_border_conditions():
    app.open()
    app.add('a', 'b', 'c', 'd')

    app.edit('a', 'a edited')
    app.edit('b', 'b edited')
    app.edit('d', 'd edited')

    app.todos_should_be('a edited', 'b edited', 'c', 'd edited')
    app.items_left_should_be(4)
    app.footer_should_be_visible()
    app.clear_completed_should_be_hidden()


def test_cancel_editing():
    app.open()
    app.add('a')

    app.cancel_editing_by_escape('a', 'a to be canceled')

    app.todos_should_be('a')
    app.items_left_should_be(1)
    app.footer_should_be_visible()
    app.clear_completed_should_be_hidden()


def test_complete():
    app.open()
    app.add('a', 'b')

    app.toggle('a')

    app.items_left_should_be(1)
    app.footer_should_be_visible()
    app.clear_completed_should_be_visible()


def test_activate():
    app.open()
    app.add('a', 'b')
    app.toggle('a')

    app.toggle('a')

    app.items_left_should_be(2)
    app.footer_should_be_visible()
    app.clear_completed_should_be_hidden()


def test_complete_all():
    app.open()
    app.add('a', 'b')

    app.toggle_all()

    app.items_left_should_be(0)
    app.footer_should_be_visible()
    app.clear_completed_should_be_visible()


def test_activate_all():
    app.open()
    app.add('a', 'b')
    app.toggle_all()

    app.toggle_all()

    app.items_left_should_be(2)
    app.footer_should_be_visible()
    app.clear_completed_should_be_hidden()


def test_complete_all_with_some_completed():
    app.open()
    app.add('a', 'b')
    app.toggle('b')

    app.toggle_all()

    app.items_left_should_be(0)
    app.footer_should_be_visible()
    app.clear_completed_should_be_visible()


def test_clear_completed():
    app.open()
    app.add('a', 'b')
    app.toggle('a')
    app.toggle('b')

    app.clear_completed()

    app.todos_should_be()
    app.footer_should_be_hidden()
    app.clear_completed_should_be_hidden()


def test_delete():
    app.open()
    app.add('a', 'b')

    app.delete('a')

    app.todos_should_be('b')
    app.items_left_should_be(1)
    app.footer_should_be_visible()
    app.clear_completed_should_be_hidden()


def test_delete_by_edit_to_blanc():
    app.open()
    app.add('a', 'b')

    app.edit('a', '')

    app.todos_should_be('b')
    app.items_left_should_be(1)
    app.footer_should_be_visible()
    app.clear_completed_should_be_hidden()


def test_delete_all():
    app.open()
    app.add('a', 'b')

    app.delete('a')
    app.delete('b')

    app.todos_should_be()
    app.footer_should_be_hidden()
    app.clear_completed_should_be_hidden()

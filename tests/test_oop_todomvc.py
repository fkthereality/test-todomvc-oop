from test_todomvc_oop.helpers.app import All


def test_open():
    All().open()
    All().close()


def test_add():
    All().open()
    All().add('a', 'b')
    All().assert_todos('a', 'b')
    All().close()


def test_edit():
    All().open()
    All().add('a')
    All().edit('a', 'a edited')
    All().assert_todos('a edited')
    All().close()


def test_complete():
    All().open()
    All().add('a')
    All().complete('a')
    All().items_left_should_be(0)
    All().close()


def test_toggle_all():
    All().open()
    All().add('a', 'b')
    All().toggle_all()
    All().items_left_should_be(0)
    All().toggle_all()
    All().items_left_should_be(2)
    All().close()


def test_clear_completed():
    All().open()
    All().add('a')
    All().complete('a')
    All().clear_completed()
    All().assert_todos()
    All().close()


def test_cancel_editing():
    All().open()
    All().add('a')
    All().cancel_editing('a', 'a to be canceled')
    All().assert_todos('a')
    All().close()


def test_delete():
    All().open()
    All().add('a', 'b')
    All().delete('a')
    All().assert_todos('b')
    All().close()

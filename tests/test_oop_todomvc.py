from test_todomvc_oop.helpers.app import All


def test_open():
    All().open()


def test_add():
    All().open()
    All().add('a', 'b')
    All().assert_todos('a', 'b')


def test_edit():
    All().open()
    All().add('a')
    All().edit('a', 'a edited')
    All().assert_todos('a edited')


def test_complete():
    All().open()
    All().add('a')
    All().complete('a')
    All().items_left_should_be(0)


def test_toggle_all():
    All().open()
    All().add('a', 'b')
    All().toggle_all()
    All().items_left_should_be(0)
    All().toggle_all()
    All().items_left_should_be(2)


def test_clear_completed():
    All().open()
    All().add('a')
    All().complete('a')
    All().clear_completed()
    All().assert_todos()


def test_cancel_editing():
    All().open()
    All().add('a')
    All().cancel_editing('a', 'a to be canceled')
    All().assert_todos('a')


def test_delete():
    All().open()
    All().add('a', 'b')
    All().delete('a')
    All().assert_todos('b')

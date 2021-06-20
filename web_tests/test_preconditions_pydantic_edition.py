


def test_add_and_restart_browser():
    app.open()

    app.add('a')
    app.restart_page()

    app.todos_should_be('a')
    app.items_left_should_be(1)
    app.footer_should_be_visible()
    app.clear_completed_should_be_hidden()


def test_open():

    app.open()

    app.todos_should_be()
    app.footer_should_be_hidden()

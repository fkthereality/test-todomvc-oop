from tests import app


def test_todomvc_lifecycle_e2e():
    app.open()

    app.add('a', 'b', 'c')
    app.todos_should_be('a', 'b', 'c')

    app.edit('b', 'b edited')

    app.toggle('b edited')
    app.clear_completed()
    app.todos_should_be('a', 'c')

    app.cancel_editing_by_escape('a', 'a to be canceled')

    app.delete('a')
    app.todos_should_be('c')

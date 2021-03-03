from tests import app


def test_common_todos_management():
    app.open()

    app.add('a', 'b', 'c')
    app.assert_todos('a', 'b', 'c')

    app.edit('b', 'b edited')

    app.complete('b edited')
    app.clear_completed()
    app.assert_todos('a', 'c')

    app.cancel_editing_by_escape('a', 'a to be canceled')

    app.delete('a')
    app.assert_todos('c')

from selene import have, command
from selene.support.shared import browser
from selenium.webdriver.common.keys import Keys

todo_list = browser.all('#todo-list>li')


class App:

    def open(self):
        browser.open('https://todomvc4tasj.herokuapp.com/')
        window_uploaded = "return $._data($('#clear-completed')[0], 'events')"\
                          ".hasOwnProperty('click') " \
                          "& " \
                          "Object.keys(require.s.contexts._.defined).length" \
                          " == 39"
        browser.should(have.js_returned(True, window_uploaded))
        return self

    def add(self, *texts):
        for text in texts:
            browser.element('#new-todo').type(text).press_enter()
        return self

    def assert_todos(self, *texts):
        todo_list.should(have.exact_texts(*texts))
        return self

    def start_editing(self, text, added_text):
        todo_list.element_by(have.exact_text(text)). \
            double_click()
        return todo_list.element_by(have.css_class('editing')). \
            element('.edit').perform(command.js.set_value(added_text))

    def cancel_editing_by_escape(self, text, added_text):
        self.start_editing(text, added_text).press_escape()
        return self

    def edit(self, text, added_text):
        self.start_editing(text, added_text).press_enter()

    def edit_by_tab(self, text, added_text):
        self.start_editing(text, added_text).press_tab()

    def edit_by_control_enter(self, text, added_text):
        self.start_editing(text, added_text).send_keys(Keys.CONTROL + '\ue007')

    def edit_by_click_outside(self, text, added_text):
        self.start_editing(text, added_text)
        browser.element('#new-todo').click()

    def delete(self, text):
        todo_list.element_by(have.exact_text(text)).hover(). \
            element('.destroy').click()
        return self

    def complete(self, text):
        todo_list.element_by(have.exact_text(text)). \
            element('.toggle').click()
        return self

    def clear_completed(self):
        browser.element('#clear-completed').click()
        return self

    def items_left_should_be(self, value: int):
        browser.element('#todo-count>strong').should(
            have.exact_text(str(value)))
        return self

    def has_no_items_left_displayed(self):
        browser.element('#todo-count>strong').is_displayed()
        return self

    def toggle_all(self):
        browser.element('#toggle-all').click()
        return self

    def close(self):
        browser.close()
        return self

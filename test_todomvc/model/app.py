from selene import have, command, be
from selene.support.shared import browser
from selenium.webdriver.common.keys import Keys

todo_list = browser.all('#todo-list>li')
clear_completed_button = browser.element('#clear-completed')
footer = browser.element('#footer')
items_left_counter = browser.element('#todo-count>strong')

class App:
    def open(self):
        browser.open('https://todomvc4tasj.herokuapp.com/')
        window_uploaded = "return $._data($('#clear-completed')[0], 'events')" \
                          ".hasOwnProperty('click') " \
                          "& " \
                          "Object.keys(require.s.contexts._.defined).length" \
                          " == 39"
        browser.should(have.js_returned(True, window_uploaded))
        return self

    def restart_page(self):
        browser.execute_script("location.reload()")
        return self

    def add(self, *texts):
        for text in texts:
            browser.element('#new-todo').type(text).press_enter()
        return self

    def todos_should_be(self, *texts):
        todo_list.should(have.exact_texts(*texts))
        return self

    def start_editing(self, text, added_text):
        todo_list.element_by(have.exact_text(text)). \
            double_click()
        return todo_list.element_by(have.css_class('editing')). \
            element('.edit').perform(command.js.set_value(added_text))

    def cancel_editing_by_escape(self, text, new_text):
        self.start_editing(text, new_text).press_escape()
        return self

    def edit(self, text, added_text):
        self.start_editing(text, added_text).press_enter()

    def edit_by_tab(self, text, added_text):
        self.start_editing(text, added_text).press_tab()

    def edit_by_click_outside(self, text, added_text):
        self.start_editing(text, added_text)
        browser.element('#new-todo').click()

    def edit_by_control_enter(self, text, added_text):
        self.start_editing(text, added_text).send_keys(Keys.CONTROL + '\ue007')

    def delete(self, text):
        todo_list.element_by(have.exact_text(text)).hover(). \
            element('.destroy').click()
        return self

    def toggle(self, text):
        todo_list.element_by(have.exact_text(text)). \
            element('.toggle').click()
        return self

    def clear_completed(self):
        clear_completed_button.click()
        return self

    def clear_completed_should_be_hidden(self):
        clear_completed_button.should(be.hidden)
        return self

    def clear_completed_should_be_visible(self):
        clear_completed_button.should(be.visible)
        return self

    def items_left_should_be(self, value: int):
        items_left_counter.should(have.exact_text(str(value)))
        return self

    def items_left_should_be_visible(self):
        footer.items_left_counter.is_displayed()
        return self

    def footer_should_be_hidden(self):
        footer.should(be.hidden)
        return self

    def footer_should_be_visible(self):
        footer.should(be.visible)
        return self

    def toggle_all(self):
        browser.element('#toggle-all').click()
        return self

    def close(self):
        browser.close()
        return self

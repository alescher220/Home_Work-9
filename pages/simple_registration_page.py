from selene import browser, have


class SimpleRegistrationPage:          # упрощённый пример
    def open(self):
        browser.open('/automation-practice-form')
        return self

    def fill_name(self, name: str):
        browser.element('#firstName').type(name)
        return self

    def submit(self):
        browser.element('#submit').click()
        return self

    def should_have_success_message(self):
        browser.element('.modal-header').should(have.text('Thanks'))

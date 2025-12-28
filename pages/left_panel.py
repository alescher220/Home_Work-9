from selene import browser, by, have


class LeftPanel:
    def open(self, *path: str):
        """
        Раскрывает разделы дерева: open('Elements', 'Text Box')
        """
        for p in path:
            browser.element(by.text(p)).click()
        return self

    # шорткат для конкретной формы
    def open_simple_registration_form(self):
        return self.open('Forms', 'Practice Form')

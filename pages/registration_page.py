from selene import browser, have, be
import os
from pathlib import Path
from data.user import User


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')
        return self

    # mid-level шаги
    def fill_first_name(self, value: str):
        browser.element('#firstName').should(be.blank).type(value)
        return self

    def fill_last_name(self, value: str):
        browser.element('#lastName').should(be.blank).type(value)
        return self

    def fill_email(self, value: str):
        browser.element('#userEmail').type(value)
        return self

    def select_gender(self, *, male=True):
        browser.element('label[for="gender-radio-1"]').click()
        return self

    def fill_mobile(self, value: str):
        browser.element('#userNumber').type(value)
        return self

    def fill_date_of_birth(self, year: int, month: int, day: int):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').element(f'option[value="{year}"]').click()
        browser.element('.react-datepicker__month-select').element(f'option[value="{month-1}"]').click()
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()
        return self

    def fill_subjects(self, *subjects: str):
        for subj in subjects:
            browser.element('#subjectsInput').type(subj).press_enter()
        return self

    def select_hobbies(self, *indexes: int):
        for idx in indexes:
            browser.element(f'label[for="hobbies-checkbox-{idx}"]').click()
        return self

    def upload_picture(self, file_name: str):
        path = str(Path(__file__).parent.parent.joinpath('resources', file_name).resolve())
        browser.element('#uploadPicture').send_keys(path)
        return self

    def fill_address(self, value: str):
        browser.element('#currentAddress').type(value)
        return self

    def scroll_to_bottom(self):
        browser.element('#submit').execute_script('element.scrollIntoView()')
        return self

    def select_state(self, name: str):
        browser.element('#state').click()
        browser.all('[id^="react-select-3-option"]').element_by(have.exact_text(name)).click()
        return self

    def select_city(self, name: str):
        browser.element('#city').click()
        browser.all('[id^="react-select-4-option"]').element_by(have.exact_text(name)).click()
        return self

    def submit(self):
        browser.element('#submit').click()
        return self

    # проверка
    def should_have_registered(self, *rows: tuple[str, str]):
        browser.element('.modal-header').should(have.text('Thanks for submitting the form'))
        browser.all('.table-responsive td:nth-child(2)').should(have.texts(*[r[1] for r in rows]))

    def register(self, user: User):
        return self.fill_first_name(user.first_name) \
            .fill_last_name(user.last_name) \
            .fill_email(user.email) \
            .select_gender(male=user.gender is Gender.MALE) \
            .fill_mobile(user.mobile) \
            .fill_date_of_birth(user.birth_date.year,
                                user.birth_date.month,
                                user.birth_date.day) \
            .fill_subjects(*user.subjects) \
            .select_hobbies(*(h.value for h in user.hobbies)) \
            .upload_picture(user.picture) \
            .fill_address(user.address) \
            .scroll_to_bottom() \
            .select_state(user.state) \
            .select_city(user.city) \
            .submit()

    def should_have_registered(self, user: User):
        rows = [
            ('Student Name', f'{user.first_name} {user.last_name}'),
            ('Student Email', user.email),
            ('Gender', user.gender.value),
            ('Mobile', user.mobile),
            ('Date of Birth', f'{user.birth_date.day} {user.birth_date:%B},{user.birth_date.year}'),
            ('Subjects', ','.join(user.subjects)),
            ('Hobbies', ','.join(h.name.capitalize() for h in user.hobbies)),
            ('Picture', user.picture),
            ('Address', user.address),
            ('State and City', f'{user.state} {user.city}'),
        ]
        self.should_have_registered(*rows)
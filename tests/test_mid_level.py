from pages.registration_page import RegistrationPage


def test_mid_level():
    yasha_rows = [
        ('Student Name',      'Yasha Kramarenko'),
        ('Student Email',     'yashaka@gmail.com'),
        ('Gender',            'Male'),
        ('Mobile',            '0123456789'),
        ('Date of Birth',     '20 February,2002'),
        ('Subjects',          'English'),
        ('Hobbies',           'Sports'),
        ('Picture',           'test.jpg'),
        ('Address',           'Moscow, Veshnyaki 18'),
        ('State and City',    'NCR Delhi'),
    ]

    RegistrationPage().open()\
        .fill_first_name('Yasha')\
        .fill_last_name('Kramarenko')\
        .fill_email('yashaka@gmail.com')\
        .select_gender()\
        .fill_mobile('0123456789')\
        .fill_date_of_birth(2002, 2, 20)\
        .fill_subjects('English')\
        .select_hobbies(1)\
        .upload_picture('test.jpg')\
        .fill_address('Moscow, Veshnyaki 18')\
        .scroll_to_bottom()\
        .select_state('NCR')\
        .select_city('Delhi')\
        .submit()\
        .should_have_registered(*yasha_rows)

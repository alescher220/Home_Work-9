from data.user import User, Gender, Hobby
from pages.registration_page import RegistrationPage


def test_high_level():
    yasha = User(
        first_name='Yasha',
        last_name='Kramarenko',
        email='yashaka@gmail.com',
        gender=Gender.MALE,
        mobile='0123456789',
        birth_date=date(2002, 2, 20),
        subjects=['English'],
        hobbies=[Hobby.SPORTS],
        picture='test.jpg',
        address='Moscow, Veshnyaki 18',
        state='NCR',
        city='Delhi',
    )

    RegistrationPage().open()\
        .register(yasha)\
        .should_have_registered(yasha)

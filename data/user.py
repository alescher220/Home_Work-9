from dataclasses import dataclass
from datetime import date
from enum import Enum


class Gender(Enum):
    MALE   = 'Male'
    FEMALE = 'Female'
    OTHER  = 'Other'


class Hobby(Enum):
    SPORTS  = 1
    READING = 2
    MUSIC   = 3


@dataclass
class User:
    first_name: str
    last_name:  str
    email:      str
    gender:     Gender
    mobile:     str
    birth_date: date
    subjects:   list[str]
    hobbies:    list[Hobby]
    picture:    str
    address:    str
    state:      str
    city:       str

import random

from data.data import Person
from faker import Faker

faker_en = Faker('en')
Faker.seed()


def generated_person():
    yield Person(
        fist_name=faker_en.first_name(),
        last_name=faker_en.last_name(),
        full_name=faker_en.first_name() + " " + faker_en.last_name(),
        email=faker_en.email(),
        current_address=faker_en.street_address(),
        permanent_address=faker_en.street_address(),
        mobile=faker_en.msisdn(),
        subject='English'
    )


def generated_file():
    path = rf'/Users/mba/tmp/DemoQA/File_to_input{random.randint(5, 23)}.txt'
    file = open(path, 'w')
    file.write(f'Helloworld{random.randint(23, 100)}')
    file.close()
    return path

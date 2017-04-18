from django.test import TestCase
from .models import Person


class SomeTests(TestCase):
    def test_math(self):
        "put docstrings in your tests"
        assert(2 + 2 == 4)


class TestPerson(TestCase):
    def test_person_data(self):
        "test of Person model"
        person = Person()
        person.name = "Misha"
        person.last_name = "Kuznietsov"
        person.email = "kuznecov513@gmail.com"
        person.jabber = "miando@42cc.co"
        person.save()
        person = Person.objects.get(name="Misha")
        self.assertEquals(person.name, "Misha")
        self.assertEquals(person.last_name, "Kuznietsov")
        self.assertEquals(person.email, "kuznecov513@gmail.com")
        self.assertEquals(person.jabber, "miando@42cc.co")

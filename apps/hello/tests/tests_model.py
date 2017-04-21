from django.test import TestCase

from apps.hello.models import Person


class PersonModelTest(TestCase):
    """return __str__ of Person model"""
    def test_string_representation(self):
        full_name = Person(name="Mykhailo", last_name="Kuznietsov")
        self.assertEqual(str(full_name), "Mykhailo Kuznietsov")

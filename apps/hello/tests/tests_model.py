from django.test import TestCase

from apps.hello.models import Person


class PersonModelTest(TestCase):

    def test_string_representation(self):
        """return __str__ of Person model"""
        full_name = Person(name="Mykhailo", last_name="Kuznietsov")
        self.assertEqual(str(full_name), "Mykhailo Kuznietsov")

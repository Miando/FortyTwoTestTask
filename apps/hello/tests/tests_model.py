from django.test import TestCase

from apps.hello.models import Person


class EntryModelTest(TestCase):

    def test_string_representation(self):
        full_name = Person(name="Mykhailo", last_name="Kuznietsov")
        self.assertEqual(str(full_name), full_name.title)

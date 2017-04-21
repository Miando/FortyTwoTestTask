from django.test import TestCase

# Create your tests here.


class SomeTests(TestCase):
    def test_math(self):
        "put docstrings in your tests"
        assert(2 + 2 == 4)

class ProjectTests(TestCase):

    def test_status_200(self):
        "test status code"
        requests = [
            '/',
        ]
        for request in requests:
            response = self.client.get(request)
            self.assertEqual(response.status_code, 200)

    def tests_template_index(self):
        "test for index template"
        response = self.client.get('/')
        self.assertContains(response, 'title')
        self.assertContains(response, 'kuznecov513@gmail.com')

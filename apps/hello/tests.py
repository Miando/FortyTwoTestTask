from django.test import TestCase
from .models import Person, RequestModel


class SomeTests(TestCase):
    def test_math(self):
        "put docstrings in your tests"
        assert(2 + 2 == 4)


class TestModel(TestCase):
    def test_person_data(self):
        "test of adding data to Person model"
        person = Person.objects.get(name="Misha")
        self.assertEquals(person.name, "Misha")
        self.assertEquals(person.last_name, "Kuznietsov")
        self.assertEquals(person.email, "kuznecov513@gmail.com")
        self.assertEquals(person.jabber, "miando@42cc.co")

    def test_request_model(self):
        "cheking middleware"
        self.client.get('/request/')
        req = RequestModel.objects.latest("id")
        self.assertEquals(req.url, "/request/")


class ProjectTests(TestCase):

    def test_status_200(self):
        "test status code"
        requests = [
            '/',
            '/request/',
            '/login/',
            '/edit/',
        ]
        for request in requests:
            response = self.client.get(request)
            self.assertEqual(response.status_code, 200)

    def tests_template_index(self):
        "test for index template"
        response = self.client.get('/')
        self.assertContains(response, 'title')
        self.assertContains(response, 'body')

    def tests_template_requests(self):
        "test fo last_request template"
        response = self.client.get('/request/')
        self.assertContains(response, '/request/')

    def tests_template_login(self):
        "test fo login template"
        response = self.client.get('/login/')
        self.assertContains(response, 'button')

    def tests_template_edit(self):
        "test fo edit template"
        response = self.client.get('/edit/')
        self.assertContains(response, 'form')
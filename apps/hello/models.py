from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    contacts = models.TextField(null=True, blank=True)
    jabber = models.CharField(max_length=50, null=True, blank=True)
    skype = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name + ' ' + self.last_name


class RequestModel(models.Model):
    url = models.CharField(max_length=1000, null=True, blank=True)
    method = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return self.url

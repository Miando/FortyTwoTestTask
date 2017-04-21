from django.shortcuts import render
from .models import Person


def index(request):
    person = Person.objects.get(user="1")
    context = {'person': person}
    return render(request, 'hello/index.html', context)

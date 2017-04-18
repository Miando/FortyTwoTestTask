from django.shortcuts import render
from .models import Person


def index(request):
    person = Person.objects.get(name="Misha")
    context = {'person': person}
    return render(request, 'hello/index.html', context)

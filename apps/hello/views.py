from django.shortcuts import render
from .models import Person, RequestModel


def index(request):
    person = Person.objects.get(name="Misha")
    context = {'person': person}
    return render(request, 'hello/index.html', context)


def last_requests(request):
    requests = RequestModel.objects.all()[:10:-1]
    context = {'requests': requests}
    return render(request, 'hello/last_requests.html', context)

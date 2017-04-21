from django.shortcuts import render
from .models import Test


def index(request):
    #test = Test.objects.all()
    #context = {'test': test}
    return render(request, 'hello/index.html')

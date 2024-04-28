from django.shortcuts import render
from django.http import HttpResponse


tasks = ['Go shopping', 'Do homework', 'Go to the GYM']
def index(request):
    return render(request, 'index.html', {
        'tasks': tasks
    })


def add(request):
    return render(request, 'add.html')
    

from django.shortcuts import render
from django.http import HttpResponse

def test(request, name):
    return render(request, 'test/index.html')
    
    
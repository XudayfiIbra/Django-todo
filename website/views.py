from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse

class NewTask(forms.Form):
    task = forms.CharField(label="Add a task",max_length=300)
    


def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, 'index.html', {
        'tasks': request.session["tasks"]
    })


def add(request):
    if request.method == 'POST':
        form = NewTask(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task] 
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'add.html', {
                'form': form
            })
    return render(request, 'add.html', {
        'form': NewTask
    })
    

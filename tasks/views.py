from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Task,Quote
import random

from .forms import TaskForm

# Create your views here.


def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method=="POST":
        form = TaskForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('/')
    
    myid = random.randint(1,10)
    quote = Quote.objects.get(id=myid)
    context = {'tasks':tasks, 'form':form, 'quote':quote}
    return render (request, 'tasks/index.html',context) 


def editTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method=="POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid:
            form.save()
        return redirect('/')

    context = {'task':task,'form':form}
    return render (request, 'tasks/edit_task.html', context) 

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    form = TaskForm(instance=item)
    if request.method=="POST":
        item.delete()
        return redirect('/')

    context = {'item':item,'form':form}
    return render (request, 'tasks/delete_task.html', context) 
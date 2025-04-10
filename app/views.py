from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import TodoItem

def home(request):
    return render(request, "home.html")

def startGame(request):
    return HttpResponse("COMEÇOU O JOGO")

def todos(request):
    todos_list = TodoItem.objects.all()
    return render(request, 'adicionarItem.html', context={'todosList': todos_list})

def todos_add(request):
    todo_task = request.POST.get("todo-task")
    task = TodoItem(title=todo_task)
    task.save()
    return HttpResponseRedirect(reverse('todos'))

def todos_delete(request, id):
    task = TodoItem.objects.get(id=id)
    task.delete()
    return HttpResponseRedirect(reverse('todos'))

def todos_check(request, id):
    task = TodoItem.objects.get(id=id)
    task.completed = True
    task.save()
    return HttpResponseRedirect(reverse('todos'))

def todos_uncheck(request, id):
    task = TodoItem.objects.get(id=id)
    task.completed = False
    task.save()
    return HttpResponseRedirect(reverse('todos'))

from django.shortcuts import render, HttpResponse, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
@login_required
def home(request):

    queryset = Task.objects.filter(user=request.user)

    return render(request, 'todo_app/index.html', context = {'task' : queryset})

def register_view(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    form = RegisterForm()
    context = {
        'form' : form
    }
    return render(request, 'todo_app/register.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password = password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'todo_app/login.html') 

    return render(request, 'todo_app/login.html')  

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def delete_task(request,id):
    task_to_delete = Task.objects.get(id=id, user=request.user)
    task_to_delete.delete()
    return redirect("home")

@login_required
def add_task(request):
    if request.method == "POST":
        data = request.POST
        title = data.get("title")
        description = data.get("description")
        due_date = data.get("due_date") if data.get("due_date") else None
        status = data.get("status" ,"Pending")
        priority = data.get("priority", "Low")
        Task.objects.create(
            user = request.user,
            title = title,
            description = description,
            due_date = due_date,
            status = status.capitalize(),
            priority = priority.capitalize()
        )
        return redirect('home')
    
    
    return render(request, 'todo_app/add_task.html', context={'user' : request.user})
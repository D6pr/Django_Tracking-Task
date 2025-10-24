from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Task
from django import forms
from .forms import RegisterForm
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'priority', 'date']

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'
    ordering = ['-date']

class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task_list')

def register(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, "Такий користувач уже існує.")
        else:
            User.objects.create_user(username=username, password=password)
            messages.success(request, "")
            return redirect('login')  # после регистрации — на логин
    return render(request, 'register.html', {'form': form})


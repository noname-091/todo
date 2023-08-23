from distutils.text_file import TextFile
from statistics import mode
from turtle import title
from xml.parsers.expat import model
from django.shortcuts import render
from .models import works
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

class Worklist(ListView):
    model = works
    template_name = 'todo.html'
    context_object_name = 'works'

class Workdetail(DetailView):
    model = works
    template_name = 'work.html'
    context_object_name = 'work'

class WorkCreate(CreateView):
    model = works
    template_name = 'work_create.html'
    fields = '__all__'
    success_url = reverse_lazy('works')

class WorkUpdate(UpdateView):
    model = works
    template_name = 'work_update.html'
    fields = ['title', 'description', 'status']
    success_url = reverse_lazy('works')

class WorDelete(DeleteView):
    model = works
    template_name = 'delete.html'
    success_url = reverse_lazy('works')
    context_object_name = 'work'

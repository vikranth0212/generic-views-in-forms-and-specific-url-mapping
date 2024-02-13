from django.shortcuts import render
from app.models import *
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.
from django.urls import reverse_lazy

class Schoollist(ListView):
    model=School
    #here we need to mention table name
    context_object_name='skools'
    #whatever obj name we are giving that 1 need to mention in html page jinja tag
    #it is object having data
    #template_name='app/school_list.html'
    #queryset=School.objects.filter(id=1)
    #queryset=School.objects.filter(sname='pragathi')
    #queryset=School.objects.filter(id=2)

class schooldetail(DetailView):
    model=School
    context_object_name='sclobject'
    #it is used to store the objects in the form of dict 

class SchoolCreate(CreateView):
    model=School
    fields='__all__'    

class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'    

#DeleteView is used for delete the existing data  or instance
#reverse lazy is used to after completing the action it will send to particular url
#success url is a inbulit variable
class SchoolDelete(DeleteView):
    model=School
    context_object_name='sklobj'
    success_url=reverse_lazy('Schoollist')
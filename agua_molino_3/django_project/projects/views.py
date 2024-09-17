from django.shortcuts import render
from django.views import View
# Create your views here.

class ProjectsGridView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Projects Grid"
        greeting['pageview'] = "Projects"
        return render (request,'projects/projectsgrid.html',greeting)

class ProjectsListView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Projects List"
        greeting['pageview'] = "Projects"
        return render (request,'projects/projectslist.html',greeting)

class ProjectOverviewView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Projects Overview"
        greeting['pageview'] = "Projects"
        return render (request,'projects/projectsoverview.html',greeting)

class CreateViewView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Create New"
        greeting['pageview'] = "Projects"
        return render (request,'projects/createnew.html',greeting)

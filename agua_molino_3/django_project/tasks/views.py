from django.shortcuts import render
from django.views import View
# Create your views here.

class TaskListView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Task List"
        greeting['pageview'] = "Tasks"
        return render (request,'tasks/tasklist.html',greeting)

class KanbanBoardView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "kanban Board"
        greeting['pageview'] = "Tasks"
        return render (request,'tasks/kanbanboard.html',greeting)

class CreateTaskView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Create Task"
        greeting['pageview'] = "Tasks"
        return render (request,'tasks/createtask.html',greeting)
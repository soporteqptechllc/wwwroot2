from django.shortcuts import render
from django.views import View
# Create your views here.

class UserGridView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "User Grid"
        greeting['pageview'] = "Contacts"
        return render (request,'contacts/usergrid.html',greeting)

class UserListView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "User List"
        greeting['pageview'] = "Contacts"
        return render (request,'contacts/userlist.html',greeting)

class ProfileView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Profile"
        greeting['pageview'] = "Contacts"
        return render (request,'contacts/profile.html',greeting)
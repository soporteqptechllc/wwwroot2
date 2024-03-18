from django.http import request
from django.shortcuts import redirect, render
from django.views import View   


class DashboardView(View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "Dashboard"
        greeting['pageview'] = "Dashboards"

        if 'username' in request.session:
            return render(request, 'dashboard/dashboard.html',greeting)
        else:
            return redirect('pages-login')

        # return render(request, 'dashboard/dashboard.html',greeting)

class SaasView(View):
    def get(self,request):
        greeting = {}
        greeting['heading'] = "Saas"
        greeting['pageview'] = "Dashboards"
        return render (request,'dashboard/dashboard-saas.html',greeting)

class CryptoView(View):
    def get(self,request):
        greeting = {}
        greeting['heading'] = "Crypto" 
        greeting['pageview'] = "Dashboards"
        return render (request,'dashboard/dashboard-crypto.html',greeting)

class BlogView(View):
    def get(self,request):
        greeting = {}
        greeting['heading'] = "Blog" 
        greeting['pageview'] = "Dashboards"
        return render (request,'dashboard/dashboard-blog.html',greeting)

class CalendarView(View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "Calendar"
        greeting['pageview'] = "Apps"
        return render (request, 'calendar.html',greeting)
class ChatView(View):
    def get(self, request):
        greeting = {}
        greeting['heading'] = "Chat"
        greeting['pageview'] = "Apps"
        return render (request, 'chat-view.html',greeting)

class FileManagerView(View):
    def get(self,request):
        greeting = {}
        greeting['heading'] = "File Manager"
        greeting['pageview'] = "Apps"
        return render (request,'filemanager.html',greeting)
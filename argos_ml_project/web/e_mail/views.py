from django.shortcuts import render
from django.views import View
# Create your views here.

class InboxView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Inbox"
        greeting['pageview'] = "Email"
        return render (request,'e_mail/e_mail-inbox.html',greeting)

class ReadEmailView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Read Email"
        greeting['pageview'] = "Email"
        return render (request,'e_mail/e_mail-reademail.html',greeting)

class BasicActionView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Basic Action"
        greeting['pageview'] = "Email Template"
        return render (request,'e_mail/templates/e_mail-templates-basicaction.html',greeting)

class AlertEmailView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Alert Email"
        greeting['pageview'] = "Email Template"
        return render (request,'e_mail/templates/e_mail-templates-alertemail.html',greeting)

class BillingEmailView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Billing Email"
        greeting['pageview'] = "Email Template"
        return render (request,'e_mail/templates/e_mail-templates-billingemail.html',greeting)
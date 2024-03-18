from django.shortcuts import render
from django.views import View
# Create your views here.

class StarterPageView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Starter Page"
        greeting['pageview'] = "Utility"
        return render (request,'utility/utility-starterpage.html',greeting)

class MaintainanceView(View):
    def get(self , request):
        return render (request,'utility/utility-maintainance.html')  

class ComingSoonView(View):
    def get(self , request):    
        return render (request,'utility/utility-comingsoon.html')              

class TimeLineView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Timeline"
        greeting['pageview'] = "Utility"
        return render (request,'utility/utility-timeline.html',greeting) 

class FaqView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "FAQs"
        greeting['pageview'] = "Utility"
        return render (request,'utility/utility-faq.html',greeting)  

class PricingView(View):
    def get(self , request):
        greeting = {}
        greeting['heading'] = "Pricing"
        greeting['pageview'] = "Utility"
        return render (request,'utility/utility-pricing.html',greeting)                       

class ErrorPageView(View):
    def get(self , request):    
        return render (request,'utility/utility-404error.html')    

class ErrorPageExtraView(View):
    def get(self , request):    
        return render (request,'utility/utility-500error.html')               
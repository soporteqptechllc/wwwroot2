"""skote URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from skote import views
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),

    # Dashboards View
    path('',views.DashboardView.as_view(),name='dashboard'),
    path('dashboard_saas',views.SaasView.as_view(),name='dashboard_saas'),
    path('dashboard_crypto',views.CryptoView.as_view(),name='dashboard_crypto'),
    path('dashboard_blog',views.BlogView.as_view(),name='dashboard_blog'),
    # Calender View
    path('calendar',views.CalendarView.as_view(),name='calendar'),
    # Chat View
    path('chat',views.ChatView.as_view(),name='chat'),
    # Layouts
    path('layout/',include('layout.urls')),
    # File manager View
    path('filemanager',views.FileManagerView.as_view(),name='filemanager'),
    #Ecommerce
    path('ecommerce/',include("ecommerce.urls")),
    #Crypto
    path('crypto/',include('crypto.urls')),
    #Email
    path("email/",include("e_mail.urls")),
    #Invoices
    path('invoices/',include('invoices.urls')),
    #Projects
    path('projects/',include('projects.urls')),
    #Tasks
    path('tasks/',include('tasks.urls')),
    #Blog
    path('blog/',include('blog.urls')),
    #Blog
    path('contacts/',include('contacts.urls')),
    #Authencation
    path('authentication/',include('authentication.urls')),
    #Utility
    path('utility/',include('utility.urls')),
    #Components
    path('components/',include('components.urls')),
   
]


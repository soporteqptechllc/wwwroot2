from django.urls import path
from utility import views

urlpatterns = [
    path('starterpage',views.StarterPageView.as_view(),name='utility-starterpage'),
    path('maintainance',views.MaintainanceView.as_view(),name='utility-maintainance'),
    path('comingsoon',views.ComingSoonView.as_view(),name='utility-comingsoon'),
    path('timeline',views.TimeLineView.as_view(),name='utility-timeline'),
    path('faq',views.FaqView.as_view(),name='utility-faq'),
    path('pricing',views.PricingView.as_view(),name='utility-pricing'),
    path('404error',views.ErrorPageView.as_view(),name='utility-404error'),
    path('500error',views.ErrorPageExtraView.as_view(),name='utility-500error'),
]
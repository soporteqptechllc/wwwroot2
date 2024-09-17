from django.urls import path
from authentication import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import (PasswordChangeView, PasswordChangeDoneView,PasswordResetView,PasswordResetDoneView, PasswordResetConfirmView,PasswordResetCompleteView)
urlpatterns = [
    #Viewscreen 1
    path('pages-login', views.PagesLoginView.as_view(), name="pages-login"),
    path('pages-register', views.PagesRegisterView.as_view(), name="pages-register"),
    path('pages-recoverpw', views.PagesRecoverpwView.as_view(), name="pages-recoverpw"),
    path('pages-lockscreen', views.PagesLockscreenView.as_view(), name="pages-lockscreen"),
    #path('pages-confirmmail', views.PagesConfirmmailView.as_view(), name="pages-confirmmail"),
    #path('pages-emailverification', views.PagesEmailVerificationView.as_view(), name="pages-emailverification"),
    #path('pages-twostepverification', views.PagesTwoStepVerificationView.as_view(), name="pages-twostepverification"),
    path('password_change/',auth_views.PasswordChangeView.as_view(template_name='authentication/pages-change-password-view.html'),name='password_change'),
    path('password_change/done/',auth_views.PasswordChangeDoneView.as_view(template_name='authentication/pages-change-password-done.html'),name='password_change_done'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='authentication/pages-reset-password-done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='authentication/pages-reset-password-view.html'),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='authentication/pages-confirmmail.html'),name='password_reset_complete'),
    path('pages-logout',views.logout,name ='pages-logout'),

    #Viewscreen 2
    path('pages-login-2', views.PagesLogin2View.as_view(), name="pages-login-2"),
    path('pages-register-2', views.PagesRegister2View.as_view(), name="pages-register-2"),
    path('pages-recoverpw-2', views.PagesRecoverpw2View.as_view(), name="pages-recoverpw-2"),
    path('pages-lockscreen-2', views.PagesLockscreen2View.as_view(), name="pages-lockscreen-2"),
    #path('pages-confirmmail-2', views.PagesConfirmmail2View.as_view(), name="pages-confirmmail-2"),
    #path('pages-emailverification-2', views.PagesEmailVerification2View.as_view(), name="pages-emailverification-2"),
    #path('pages-twostepverification-2', views.PagesTwoStepVerification2View.as_view(), name="pages-twostepverification-2"),
    #path('password_change/',PasswordChangeView.as_view(template_name='authentication/pages-change-password-view-2.html'),name='password_change'),
    #path('password_change/done/',PasswordChangeDoneView.as_view(template_name='authentication/pages-change-password-done-2.html'),name='password_change_done'),
    #path('password_reset/done/',PasswordResetDoneView.as_view(template_name='authentication/pages-reset-password-done-2.html'),name='password_reset_done'),
    #path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='authentication/pages-reset-password-view-2.html'),name='password_reset_confirm'),
    #path('reset/done/',PasswordResetCompleteView.as_view(template_name='authentication/pages-confirmmail-2.html'),name='password_reset_complete'),
    #path('',views.logout2,name ='logout-2'),
]   
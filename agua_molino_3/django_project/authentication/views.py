from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth import SESSION_KEY, authenticate, login
from django.views import View
from django.views.generic.base import View
from authentication.forms import UserRegistrationForm, UserLoginForm, PasswordResetForm
from django.contrib.auth.models import User,auth
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail, BadHeaderError
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.db.models.query_utils import Q


username ='';
class PagesLoginView(View):
    template_name = "authentication/pages-login.html"

    def get(self, request):
        if 'username' in request.session:
            return redirect('dashboard')
        else:
            return render(request, self.template_name, {'form': UserLoginForm})
    def post(self, request):

  
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            if username =='':
                messages.error(request,'Please enter your username')
                return redirect('pages-login')
            elif password == '':
                messages.error(request,'Please enter your password')
                return redirect('pages-login')
            else:
                user = auth.authenticate(username=username, password=password)
                if user is not None:              
                    request.session['username'] = username
                    auth.login(request, user)
                    return redirect('dashboard')
                else:
                    messages.error(request, 'Invalid Credentials')
                    return redirect('pages-login')
        else:
            return render(request, self.template_name)

class PagesRegisterView(View):
    template_name = 'authentication/pages-register.html'

    def get(self, request):
        if 'username' in request.session:
            return redirect('dashboard')
        else:
            return render(request, self.template_name, {'form': UserRegistrationForm})

    def post(self, request):
        if 'username' in request.session:
            return redirect('dashboard')
        else:
            if request.method == 'POST':
                username = request.POST['username']
                email = request.POST['email']
                password1 = request.POST['password1']
                password2 = request.POST['password2']
                if username == '':
                    messages.error(request, 'username field is empty')
                    return redirect('pages-register')
                elif email == '':
                    messages.error(request, 'email field is empty')
                    return redirect('pages-register')
                elif password1 and password2 == '' :
                    messages.error(request, 'password field is empty')
                    return redirect('pages-register')
                else:
                    # if password1 and password2 != username :
                    #     messages.info(request,'successfully registered please login')
                         
                    if User.objects.filter(username=username).exists():
                        messages.error(request, 'Username Is Allready Exists')
                        return redirect('pages-register')
                    elif User.objects.filter(email=email).exists():
                        messages.error(request, 'Email Is Allready Exists')
                        return redirect('pages-register')
                    else:
                        form = UserRegistrationForm(request.POST)
                        if form.is_valid():
                            subject = "Welcome to Skote  Membership"
                            email_template_name = "authentication/Register-email.txt"

                            c = {
                                'username': username,
                                'password': password1
                            }
                            email_1 = render_to_string(email_template_name, c)
                            send_mail(subject, email_1, 'skote@skote.com',
                                    [email], fail_silently=False)
                            user = User.objects.create_user(
                                username=username, email=email, password=password1)
                            user.save()
                            messages.success(request,"Successfully registered please login")
                            return redirect('pages-login')
                        else:
                            messages.error(request,"Passwords are similar to username or email")
                            return redirect('pages-register')
            else:
                return render(request, 'authentication/pages-register.html')

class PagesRecoverpwView(View):
    template_name = 'authentication/pages-recoverpw.html'

    def get(self, request):
        if 'username' in request.session:
            return redirect('dashboard')
        else:
            return render(request, self.template_name, {'form': PasswordResetForm})

    def post(self, request):
        if request.method == "POST":
            email = request.POST.get("email", "default value")
            if User.objects.filter(email=email).exists():
                password_reset_form = PasswordResetForm(request.POST)
                if password_reset_form.is_valid():
                    data = password_reset_form.cleaned_data['email']
                    associated_users = User.objects.filter(Q(email=data))
                    if associated_users.exists():
                        for user in associated_users:
                            subject = "Password Reset Requested"
                            email_template_name = "authentication/email.txt"
                            c = {
                                "username": user.username,
                                "email": user.email,
                                'domain': '127.0.0.1:8000',
                                'site_name': 'Website',
                                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                                "user": user,
                                'token': default_token_generator.make_token(user),
                                'protocol': 'http',
                            }
                            email = render_to_string(email_template_name, c)
                            try:
                                send_mail(subject, email, 'admin@example.com',
                                          [user.email], fail_silently=False)
                            except BadHeaderError:
                                messages.info(request, "Email Doesn't Exists ")
                                return redirect('pages-recoverpw')
                            return redirect("password_reset_done")
                password_reset_form = PasswordResetForm()
                return render(request=request, template_name="authentication/pages-recoverpw.html", context={"password_reset_form": password_reset_form})
            else:
                if email == "":
                    messages.info(request, 'Please Enter Your Email')
                    return redirect('pages-recoverpw')
                else:
                    messages.info(request, "Email doesn't  exist")
                    return redirect('pages-recoverpw')
        else:
            return render(request, 'authentication/pages-recoverpw.html')

class PagesLockscreenView(View):
    def get(self, request):
        return render(request, 'authentication/pages-lockscreen.html')

class PagesConfirmmailView(View):
    def get(self, request):
        return render(request, 'authentication/pages-confirmmail.html')

class PagesEmailVerificationView(View):
    def get(self, request):
        return render(request, 'authentication/pages-emailverificationmail.html')

class PagesTwoStepVerificationView(View):
    def get(self, request):
        return render(request, 'authentication/pages-twostepverificationmail.html')

def logout(request):
    auth.logout(request)
    return render(request,'authentication/pages-logout.html')

# Viewscreen 2

class PagesLogin2View(View):
    template_name = "authentication/pages-login-2.html"

    def get(self, request):
        if 'username' in request.session:
            return redirect('dashboard')
        else:
            return render(request, self.template_name, {'form': UserLoginForm})

    def post(self, request):
        if 'username' in request.session:
            return redirect('dashboard')
        else:
            if request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']
                if username == '':
                    messages.info(request, 'Please enter your username')
                    return redirect('pages-login-2')
                elif password == '':
                    messages.info(request, 'Please enter your password')
                    return redirect('pages-login-2')
                else:
                    user = auth.authenticate(
                        username=username, password=password)
                    if user is not None:
                        request.session['username'] = username
                        auth.login(request, user)
                        return redirect('dashboard')
                    else:
                        messages.info(request, 'Invalid Credentials')
                        return redirect('pages-login-2')
            else:
                return render(request, self.template_name)


class PagesRegister2View(View):
    template_name = 'authentication/pages-register-2.html'

    def get(self, request):
        if 'username' in request.session:
            return redirect('dashboard')
        else:
            return render(request, self.template_name, {'form': UserRegistrationForm})

    def post(self, request):
            if 'username' in request.session:
                return redirect('dashboard')
            else:
                if request.method == 'POST':
                    username = request.POST['username']
                    email = request.POST['email']
                    password1 = request.POST['password1']
                    password2 = request.POST['password2']
                    if username == '':
                        messages.error(request, 'username field is empty')
                        return redirect('pages-register-2')
                    elif email == '':
                        messages.error(request, 'email field is empty')
                        return redirect('pages-register-2')
                    elif password1 and password2 == '' :
                        messages.error(request, 'password field is empty')
                        return redirect('pages-register-2')
                    else:
                        # if password1 and password2 != username :
                        #     messages.info(request,'successfully registered please login')
                            
                        if User.objects.filter(username=username).exists():
                            messages.error(request, 'Username Is Allready Exists')
                            return redirect('pages-register-2')
                        elif User.objects.filter(email=email).exists():
                            messages.error(request, 'Email Is Allready Exists')
                            return redirect('pages-register-2')
                        else:
                            form = UserRegistrationForm(request.POST)
                            if form.is_valid():
                                subject = "Welcome to Skote  Membership"
                                email_template_name = "authentication/Register-email.txt"

                                c = {
                                    'username': username,
                                    'password': password1
                                }
                                email_1 = render_to_string(email_template_name, c)
                                send_mail(subject, email_1, 'skote@skote.com',
                                        [email], fail_silently=False)
                                user = User.objects.create_user(
                                    username=username, email=email, password=password1)
                                user.save()
                                messages.success(request,"Successfully registered please login")
                                return redirect('pages-login-2')
                            else:
                                messages.error(request,"Passwords are similar to username or email")
                                return redirect('pages-register-2')
                else:
                    return render(request, 'authentication/pages-register-2.html')

class PagesRecoverpw2View(View):
    template_name = 'authentication/pages-recoverpw2.html'

    def get(self, request):
        if 'username' in request.session:
            return redirect('dashboard')
        else:
            return render(request, self.template_name, {'form': PasswordResetForm})

    def post(self, request):
        if request.method == "POST":
            email = request.POST.get("email", "default value")
            if User.objects.filter(email=email).exists():
                password_reset_form = PasswordResetForm(request.POST)
                if password_reset_form.is_valid():
                    data = password_reset_form.cleaned_data['email']
                    associated_users = User.objects.filter(Q(email=data))
                    if associated_users.exists():
                        for user in associated_users:
                            subject = "Password Reset Requested"
                            email_template_name = "authentication/email.txt"
                            c = {
                                "username": user.username,
                                "email": user.email,
                                'domain': '127.0.0.1:8000',
                                'site_name': 'Website',
                                "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                                "user": user,
                                'token': default_token_generator.make_token(user),
                                'protocol': 'http',
                            }
                            email = render_to_string(email_template_name, c)
                            try:
                                send_mail(subject, email, 'admin@example.com',
                                          [user.email], fail_silently=False)
                            except BadHeaderError:
                                messages.info(request, "Email Doesn't Exists ")
                                return redirect('pages-recoverpw')
                            return redirect("password_reset_done")
                password_reset_form = PasswordResetForm()
                return render(request=request, template_name="authentication/pages-recoverpw2.html", context={"password_reset_form": password_reset_form})
            else:
                if email == "":
                    messages.info(request, 'Please Enter Your Email')
                    return redirect('pages-recoverpw2')
                else:
                    messages.info(request, "Email doesn't  exist")
                    return redirect('pages-recoverpw2')
        else:
            return render(request, self.template_name, {'form': PasswordResetForm})

class PagesLockscreen2View(View):
    def get(self, request):
        return render(request, 'authentication/pages-lockscreen2.html')

class PagesConfirmmail2View(View):
    def get(self, request):
        return render(request, 'authentication/pages-confirmmail-2.html')

class PagesEmailVerification2View(View):
    def get(self, request):
        return render(request, 'authentication/pages-emailverificationmail-2.html')

class PagesTwoStepVerification2View(View):
    def get(self, request):
        return render(request, 'authentication/pages-twostepverificationmail-2.html')

def logout2(request):
    auth.logout(request)
    return redirect('dashboard')

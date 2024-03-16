from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm ,UserCreationForm
from django.contrib.auth.decorators import login_required
import random
from accounts.forms import UserForm
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import EmailMessage , send_mail
from django.contrib import messages
import re
# Create your views here.
def login_view(request):
    msg = None
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        # Check if the username is an email address
        if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', username):
            email = username
            user = User.objects.filter(email=email).first()
            if user:
                username = user.username
            user = authenticate(request, username=username, password=password)
        else:
            user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            msg = messages.error(request, "User not found. Please try again.")
    form = AuthenticationForm()
    context = {'form': form, 'msg': msg}
    return render(request, 'accounts/login.html', context)
@login_required
def logout_view(request):
# if request.user.is_authenticated:
    logout(request)
    return redirect('/') # redirect to the main page
def signup_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = UserForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                username = data['username']
                email = data['email']
                password = data['password']
                first_name = data['first_name']
                last_name = data['last_name']
                confirm = request.POST.get('confirm')
                if not User.objects.filter(email = email) and password == confirm :
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    return redirect('/accounts/login')
                else :
                    msg = messages.warning(request, "passwords not match")
                    return render(request, 'accounts/signup.html',{'msg':msg})
        form = UserForm()
        return render(request, 'accounts/signup.html',{'form':form})
    else:
        return redirect('/')

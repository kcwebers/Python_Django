from django.shortcuts import render, redirect
from datetime import datetime
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'login_app/index.html')

def success_reg(request):
    if request.method == "POST":
        errors = User.objects.reg_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect("/")
        else: # no errors then this
            User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode(),birthday=request.POST['birthday'])

            request.session['first_name'] = request.POST['first_name']
            return redirect('/success')

def success_log(request):
    if request.method == "POST":
        errors = User.objects.log_validator(request.POST)
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        if len(errors) > 0:
            return redirect("/")
        else: # no errors than this 

            user_email = request.POST['email_input']
            user = User.objects.get(email=user_email)
            request.session['first_name'] = user.first_name
            request.session['last_name'] = user.last_name

            return redirect('/success')

def success(request):
    if not 'first_name' in request.session:
        errors = User.objects.not_logged(request.POST)
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/")
    elif not 'last_name' in request.session:
        errors = User.objects.success_login_validation(request.POST)
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
            return render(request, "login_app/success.html")
    else: 
        errors = User.objects.success_reg_validation(request.POST)
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
            return render(request, "login_app/success.html")

def logout(request):
    request.session.clear()
    return redirect('/')
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, "wish_app/index.html")

def success_reg(request):
    if request.method == "POST":
        errors = User.objects.reg_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect("/")
        else: # no errors then this
            user = User.objects.create(first_name=request.POST["first_name"], last_name=request.POST["last_name"], email=request.POST["email"], password=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode())

            request.session['id'] = user.id
            request.session['first_name'] = request.POST['first_name']
            return redirect('/wishes')

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
            request.session['id'] = user.id

            return redirect('/wishes')

def wishes(request):
    if not 'first_name' in request.session:
        errors = User.objects.not_logged(request.POST)
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/")
    else: 
        your_wishes = User.objects.get(id=request.session['id']).wishes_made.all()
        all_wishes = Wish.objects.all()

        all_your_wishes = []
        for wish in your_wishes:
            if len(wish.granted_by.all()) < 1:
                all_your_wishes.append(wish)

        all_other_wishes = []
        for wish in all_wishes:
            if len(wish.granted_by.all()) > 0:
                all_other_wishes.append(wish)

        all_liked = []
        for wish in all_wishes:
            likes = wish.liked_by.all()
            for like in likes:
                all_liked.append(like)

        # liked_by_count = 0
        # for wish in all_other_wishes:
        #     liked_by_count = len(wish.liked_by.all())

        # already_liked = 0
        # for wish in all_wishes:
        #     if len(wish.liked_by.all()) > 0:
        #         if wish.liked_by.get(id=request.session['id']):
        #             already_liked = 1

        context = {
            "your_wishes": all_your_wishes,
            "all_wishes": all_other_wishes,
            "liked_by": all_liked
        }
        print(your_wishes)
        return render(request, "wish_app/wishes.html", context)

def new_wish(request):
    return render(request, "wish_app/new_wish.html")

def add_wish(request):
    if request.method == "POST":
        errors = User.objects.wish_validator(request.POST)
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        if len(errors) > 0:
            return redirect("/wishes/new")
        else:
            wisher = User.objects.get(id=request.session['id'])

            new_wish = Wish.objects.create(wish=request.POST['wish'],desc=request.POST['desc'], wished_by=wisher)
            
            return redirect('/wishes')

def edit_wish(request, wish_id):
    selected_wish = Wish.objects.get(id=wish_id)
    context = {
        "wish_to_update": selected_wish
    }
    return render(request, "wish_app/edit_wish.html", context)

def update_wish(request, wish_id):
    if request.method == "POST":
        errors = User.objects.wish_validator(request.POST)
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        if len(errors) > 0:
            return redirect("/wishes/edit_wish/" + wish_id)
        else:
            selected_wish = Wish.objects.get(id=wish_id)
            selected_wish.wish = request.POST['wish']
            selected_wish.desc = request.POST['desc']
            selected_wish.save()
            return redirect("/wishes")

def granted(request, wish_id):
    wish_grantor = User.objects.get(id=request.session['id'])
    wish = Wish.objects.get(id=wish_id)
    wish.granted_by.add(wish_grantor)
    wish.save()

    return redirect("/wishes")

def like(request, wish_id):
    liker = User.objects.get(id=request.session['id'])
    wish = Wish.objects.get(id=wish_id)

    wish.liked_by.add(liker)

    return redirect("/wishes")
    

def stats(request):
    your_wishes = User.objects.get(id=request.session['id']).wishes_made.all()
    numb_wishes = len(your_wishes)

    all_your_wishes = []
    for wish in your_wishes:
        if len(wish.granted_by.all()) > 0:
            all_your_wishes.append(wish)
    numb_wishes = numb_wishes - len(all_your_wishes)
    # represents the total number of granted wishes for the that user

    all_wishes = Wish.objects.all()
    all_other_wishes = []
    for wish in all_wishes:
        if len(wish.granted_by.all()) > 0:
            all_other_wishes.append(wish)
    total_granted_wishes = len(all_other_wishes)
    # represents the total number of wishes granted across the site!

    g_wishes = Wish.objects.filter(granted_by=request.session['id'])
    granted_wishes = len(g_wishes)
    # representes the total number of wishes the user has granted to others
    context = {
        "numb_wishes": numb_wishes,
        "total_granted_wishes": total_granted_wishes,
        "granted_wishes": granted_wishes
    }
    return render(request, "wish_app/stats.html", context)

def remove(request, wish_id):
    this_book = Wish.objects.get(id=wish_id)
    this_book.delete()

    return redirect("/wishes")

def logout(request):
    request.session.clear()
    return redirect('/')
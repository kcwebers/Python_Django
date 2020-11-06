from django.shortcuts import render, redirect
import random
from datetime import datetime


def index(request):
    if 'gold_amount' not in request.session or 'activity' not in request.session:
        request.session['gold_amount'] = 0
        request.session['activity'] = ''
    return render(request, "ninja_app/index.html")

def process_money(request):
    # add 10-20 gold for farm, i.e. hidden input = 1
    if request.method == 'POST':
        if request.POST['location'] == 'farm':
            amount_earned = random.randint(10, 20)
            request.session['gold_amount'] =  request.session['gold_amount'] + amount_earned
            # total = request.session['gold_amount']

            request.session['activity'] = request.session['activity'] + '<p class="list-group-item list-group-item-success"> Worked on a farm and earned $'+ str(amount_earned) + ' ' + '(' + str(datetime.now().strftime("%B, %d %Y %H:%M %p")) + ') </br> </p>'

        # add 5-10 gold
        elif request.POST['location'] == 'cave':
            amount_earned = random.randint(5, 10)
            request.session['gold_amount'] =  request.session['gold_amount'] + amount_earned
            # total = request.session['gold_amount']

            request.session['activity'] = request.session['activity'] + '<p class="list-group-item list-group-item-success"> Chilled in a cave and earned $'+ str(amount_earned) + ' ' + '(' + str(datetime.now().strftime("%B, %d %Y %H:%M %p")) + ') </br> </p>'

        # add 2-5 gold
        elif request.POST['location'] == 'home':
            amount_earned = random.randint(2, 5)
            request.session['gold_amount'] =  request.session['gold_amount'] + amount_earned
            # total = request.session['gold_amount']

            request.session['activity'] = request.session['activity'] + '<p class="list-group-item list-group-item-success"> Relaxed at home and earned $'+ str(amount_earned) + ' ' + '(' + str(datetime.now().strftime("%B, %d %Y %H:%M %p")) + ') </br> </p>'

        # add/take 0-50 gold
        elif request.POST['location'] == 'casino':
            amount_earned = random.randint(-50, 50)
            request.session['gold_amount'] =  request.session['gold_amount'] + amount_earned
            # total = request.session['gold_amount']

            if amount_earned < 0:
                request.session['activity'] = request.session['activity'] + '<p class="list-group-item list-group-item-danger"> Went to the casino and lost -$'+ str(amount_earned * -1) + ' ' + '(' + str(datetime.now().strftime("%B, %d %Y %H:%M %p")) + ') </br></p>'
            else:
                request.session['activity'] = request.session['activity'] + '<p class="list-group-item list-group-item-success"> Went to the casino and won $'+ str(amount_earned) + ' ' + '(' + str(datetime.now().strftime("%B, %d %Y %H:%M %p")) + ') </br> </p>'

    # request.session['gold_amount']: total
    # request.session["activity"]: result

    return redirect("/")

def clear(request):
    request.session.clear()
    return redirect("/")
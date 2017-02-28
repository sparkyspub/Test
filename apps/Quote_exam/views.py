from django.shortcuts import render, redirect
from .models import User, Quote, Favorites
from django.contrib import messages
from django.core.urlresolvers import reverse
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
ALPHA_REGEX = re.compile(r'^[a-zA-Z]+$')

# Create your views here.
def index(request):
    return render(request, "Quote_exam/index.html")
    # *****************************REG AND SIGN IN**************************

def Reg(request):
    nologinerrors = True
    if len(request.POST['first_name']) < 2:
        messages.add_message(request, messages.ERROR, "Invalid input")
        nologinerrors = False
    if len(request.POST['last_name']) < 2:
        messages.add_message(request, messages.ERROR, "Invalid input")
        nologinerrors = False
    if not ALPHA_REGEX.match(request.POST['first_name']):
        messages.add_message(request, messages.ERROR, "First name can not have a number in it")
        nologinerrors = False
    if not ALPHA_REGEX.match(request.POST['last_name']):
        messages.add_message(request, messages.ERROR, "Last name can not have a number in it")
        nologinerrors = False
    if not EMAIL_REGEX.match(request.POST['email']):
        messages.add_message(request, messages.ERROR,"Your email does not match")
        nologinerrors = False
    if request.POST['password'] < 8:
        messages.add_messages(request, messages.ERROR, "Your password is not long enough")
        nologinerrors = False
    if request.POST['password'] != request.POST['confirm']:
        messages.add_message(request, messages.ERROR, "Your passwords don't match")
        nologinerrors = False
    if nologinerrors == False:
        return redirect ('/')

    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    email = request.POST['email']
    password = request.POST['password']
    User.objects.create(
    first_name = request.POST['first_name'],
    last_name = request.POST['last_name'],
    email = request.POST['email'],
    password = request.POST['password'])
    request.session['first_name'] = request.POST['first_name']
    return redirect ('quotes')

def SignIn(request):
    email = request.POST['email']
    password = request.POST['password']
    if user == User.objects.get(email = email):
        request.session['first_name'] = user.first_name
        request.session['id'] = user.id
        return redirect ('Quote_exam:quotes')
    else:
        messages.add_message(request, messages.ERROR, "Login doesn't match")
        return redirect ('index')

def quotes (request):
    return  render (request, "Quote_exam/profile.html")

# ****************************CLEAR SESSION***********************************
# def success (request):
#     return render (request, 'Quote_exam/profile.html')

def clear (request):
    if 'first_name' in request.session:
        del request.session['first_name']
    return redirect ('/')

# ***********************ADDING A QUOTE******************************

def quote_addon (request):
    nologinerrors = True
    user = User.objects.get(first_name = request.session['first_name'])

    if len(request.POST['quotes']) < 1:
        messages.add_message(request, messages.ERROR, "You need something to quote")
        nologinerrors = False

    if nologinerrors == False:
        return redirect ('Quote_exam/profile.html')
    else:
        Quote.objects.create(quotes = request.POST['quotes'], user = user)
        return redirect('quotes')

# *************************SHOWING THE QUOTES******************************

def quote_show (request):
    context = {
    'quotes_log' : Quote.objects.all(),
    'profile_favs' : Favorites.object.filter(userfavorites_id = request.session['id'])
    }
    return render (request, 'profile.html', context)

# ***************************ADDING TO FAVORITES******************************
def favorites(request, quotes_id):
    quotes = Quote.objects.filter(id = quote_id)
    Favorites.objects.create(quotefavorite = quote.quotes)
    return redirect ('quotes')

# *************************QUOTES THE USER COLLECTED*****************************
def quotes_collected(request, quote_user_id):
    userpost = User.objects.filter(id = quote_user_id)
    context = {
    'user_post' : userpost
    }
    return render (request, 'Quote_exam/home.html', context)

# *********************************DELETE QUOTES************************************
def delete (request, favorite_id):
    Favorites.objects.filter(id = favorite_id).delete()
    return redirect ('index')

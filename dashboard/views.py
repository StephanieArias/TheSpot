from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

from IPython import embed


def dashboard(request):
    return render(request, 'dashboard.html')

def LoginHome(request):
    return render(request, 'login.html')

def register(request):
    if request.method == "GET":
        return redirect('/LoginHome')
    errors = User.objects.validate(request.POST)
    if errors:
        for e in errors.values():
            messages.error(request, e)
        return redirect('/LoginHome')
    else:
        new_user = User.objects.register(request.POST)
        request.session['user_id'] = new_user.id
        messages.success(request, "You have successfully registered!")
        return redirect('/success')

def login(request):
    if request.method == "GET":
        return redirect('/LoginHome')
    if not User.objects.authenticate(request.POST['email'], request.POST['password']):
        messages.error(request, 'Invalid Email/Password')
        return redirect('/LoginHome')
    user = User.objects.get(email=request.POST['email'])
    request.session['user_id'] = user.id
    messages.success(request, "You have successfully logged in!")
    return redirect('/success')

def logout(request):
    request.session.clear()
    return redirect('/')

def success(request):
    if 'user_id' not in request.session:
        return redirect('login.html')
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user': user
    }
    return render(request, 'success.html', context)


def categoryPage(request, catName):
    # pull information from modals
    context ={

    }
    return render(request, 'categories.html', context) 

## Search Functions 
def search(request):
    return render(request, 'ticket_master_api/dashboard.html')

def list_concerts(request):
    embed()
    
def eventInfo(request):
    return render(request, 'event-info.html')
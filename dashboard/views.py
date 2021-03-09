from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

import requests as req


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


def about(request):
    return render(request, 'about.html')

def categoryPage(request, catName):
    # pull information from modals
    context ={

    }
    return render(request, 'categories.html', context) 


def list_concerts(request):
    embed()
    
def eventInfo(request):
    return render(request, 'event-info.html')
# Search Functions
def search_form(request):
    return render(request, 'concerts/search_form.html')


def concerts_list(request):
    artist = request.POST['artist']
    ticketmaster_url = _generate_ticketmaster_url(artist)
    response = req.get(ticketmaster_url)
    data = response.json()
    if data['page']['totalElements'] == 0:
        return render(request, 'concerts_list.html', {'artist': artist})
    event_data=[]
    for event in data['_embedded']['events'][:5]:
        new_event={
            'name': event['name'],
            'location': event['_embedded']['venues'][0]['location'],
            'venue': event['_embedded']['venues'][0]['name'],
        }
        event_data.append(new_event)
    modified_event_data=_generate_google_maps_url(event_data)
    html_data={
        'artist': artist,
        'concerts': modified_event_data
    }
    return render(request, 'concerts_list.html', html_data)


def _generate_ticketmaster_url(artist):
    modified_artist=artist.replace(' ', '+')
    ticketmaster_key='2f3ueG8j04S9LIVd8lbILPUlU77AphrA'
    return f"https://app.ticketmaster.com/discovery/v2/events.json?keyword={ modified_artist }&apikey={ ticketmaster_key }"


def _generate_google_maps_url(event_data):
    googlemaps_key="AIzaSyC9djNoR364Rl5eADIkHOt5IcXORxWMyrw"
    for event in event_data:
        latitude=event['location']['latitude']
        longitude=event['location']['longitude']
        event['location']=f"https://www.google.com/maps/embed/v1/place?key={ googlemaps_key }&q={latitude},{longitude}&zoom=18&maptype=satellite"
    return event_data



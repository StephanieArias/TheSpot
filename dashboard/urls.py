from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.dashboard),
    path('about', views.about,  name='about'),
    path('search', views.search_form, name='search_form'),
    path('concerts_list', views.concerts_list, name='concerts_list'),
    path('category_list', views.category_list, name='category_list'),
    path('LoginHome', views.LoginHome),
    path('cart', views.cart),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('success', views.success),
    path('eventInfo', views.eventInfo),
    path('editAccount', views.editAccount),
    path('nearby', views.nearby)
]



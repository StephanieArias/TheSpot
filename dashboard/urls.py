from . import views
from django.urls import path

urlpatterns = [
    path('', views.dashboard),
    path('LoginHome', views.LoginHome),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('success', views.success),
    path('category-<str:catName>', views.categoryPage),
    path('eventInfo', views.eventInfo),
]
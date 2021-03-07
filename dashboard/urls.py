<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    ('', views.index),
=======
from . import views
from django.urls import path

urlpatterns = [
    path('', views.dashboard),
    path('LoginHome', views.LoginHome),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('success', views.success)
>>>>>>> 1ba613e603729dc12f028d284654d6a26ae4f65a
]
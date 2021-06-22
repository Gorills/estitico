
from os import name
from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('contacts/', views.contact, name='contacts'),
    path('special/', views.special, name='special'),
    path('special/special_view', views.special_view, name='special_view'),
    path('price/', views.price, name='price'),
]
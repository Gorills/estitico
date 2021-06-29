
from os import name
from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('review_list', views.review_list, name='review_list'),
    path('contacts/', views.contact, name='contacts'),
    path('special/', views.special, name='special'),
    path('special/<slug:slug>', views.special_detail, name='special_detail'),
    path('price/', views.price, name='price'),
    path('<slug:slug>/', views.services_detail, name='services_detail'),
]
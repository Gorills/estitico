
from os import name
from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.home, name='home'),
    
    path('review/', views.review_list, name='review_list'),
    path('contacts/', views.contact, name='contacts'),
    path('special/', views.special, name='special'),
    path('special/<slug:slug>/', views.special_detail, name='special_detail'),
    path('price/', views.price, name='price'),
    path('services/<slug:slug>/', views.services_detail, name='services_detail'),
    path('privacy/', views.privacy, name='privacy'),
    path('user_agreement/', views.user_agreement, name='user_agreement'),
    path('pravovaya-informaciya', views.pravovaya_informaciya, name='pravovaya_informaciya')
]
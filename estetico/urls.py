
from os import name
from django.urls import path
from . import views


urlpatterns = [
    
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('review_list', views.review_list, name='review_list'),
    path('contacts/', views.contact, name='contacts'),
    path('special/', views.special, name='special'),
    path('special/special_view', views.special_view, name='special_view'),
    path('price/', views.price, name='price'),
    path('servises_detail/', views.servises_detail, name='servises_detail'),
]
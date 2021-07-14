from django.urls import path
from . import views


urlpatterns = [
    path('', views.specialist, name='specialist'),
    path('<slug:slug>/', views.specialist_detail, name='specialist_detail'),

]

from django.urls import path
from . import views

app_name='lidlstatsApp'  #lidlApp
urlpatterns = [

    path('', views.index, name='index'),
    path('user/', views.user_settings, name='user'),
    path('data/', views.data, name='data'),



]

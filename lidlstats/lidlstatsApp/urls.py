from background_task import background
from django.urls import path
from . import views
from .filehandler import FileHandler
from .statisticdevil import StatisticDevil

app_name = 'lidlstatsApp'  # lidlApp
urlpatterns = [

    path('', views.index, name='index'),
    path('user/', views.user_settings, name='user'),
    path('data/', views.data, name='data'),

]

FileHandler.manage_files()
StatisticDevil.take_out_my_json("hej")


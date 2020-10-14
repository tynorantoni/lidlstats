from background_task import background
from django.urls import path
from . import views
from .filehandler import FileHandler
from .receiptocr import ReceiptOCR

app_name = 'lidlstatsApp'  # lidlApp
urlpatterns = [

    path('', views.index, name='index'),
    path('user/', views.user_settings, name='user'),
    path('data/', views.data, name='data'),

]

# FileHandler.manage_files()
# FileHandler.data_transfer()

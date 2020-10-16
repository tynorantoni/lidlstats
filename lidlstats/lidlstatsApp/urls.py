from background_task import background
from django.urls import path
from . import views
from .filehandler import FileHandler
from .models import BasicDataModel
from .statisticdevil import StatisticDevil

app_name = 'lidlstatsApp'  # lidlApp
urlpatterns = [

    path('', views.index, name='index'),
    path('user/', views.user_settings, name='user'),
    path('details/', views.details, name='details'),
    path('upload/',views.upload_file,name='upload_file')

]

# FileHandler.manage_files()
# data_from_db = BasicDataModel.objects.get(id=18)
# table_df = StatisticDevil()
# table_to_show = table_df.make_yourself_a_table(data_from_db.product_data)
# print(table_to_show.head())


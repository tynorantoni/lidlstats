from background_task import background
from django.conf import settings
from django.conf.urls.static import static
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
    # path('details/<str:id_of_shopping>/',views.detail_of_shopping, name='detail_of_shopping'),
    path('upload/',views.upload_file,name='upload_file')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# FileHandler.manage_files()
# data_from_db = BasicDataModel.objects.get(id=18)
# table_df = StatisticDevil()
# table_to_show = table_df.make_yourself_a_table(data_from_db.product_data)
# print(table_to_show.head())


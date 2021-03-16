from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('drop_data', views.drop_data, name='drop_data'),
    path('load_data', views.load_data, name='load_data'),
]

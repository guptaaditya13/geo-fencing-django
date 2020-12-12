from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all', views.get_data, name='getAllData'),
    path('add', views.save_data, name='add')
]
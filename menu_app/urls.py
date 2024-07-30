from django.urls import path
from . import views

app_name = 'menu_app'

urlpatterns = [
    path('', views.index, name='index'),
]

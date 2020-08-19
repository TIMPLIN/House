from django.urls import path
from . import views

app_name = 'house'

urlpatterns = [
    path('', views.house_filter, name = 'house_filter')
]
from django.urls import path
from . import views

# namespace
app_name = 'house'

urlpatterns = [
    path('', views.house_filter, name='house_filter'),
]
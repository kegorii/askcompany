from django.urls import path
from . import views

urlpatterns = [
    path('',views.insub_list,name='insub_list')
]

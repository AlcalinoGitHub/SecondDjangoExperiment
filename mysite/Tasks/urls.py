from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.main),
    path('delete/', views.delete, name='delete'),
]
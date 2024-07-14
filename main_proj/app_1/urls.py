from django.urls import path
from . import views

urlpatterns = [
    path('', views.app_1,name='app_1home'),
    path('<int:anime_id>/', views.anime_detail,name='detail'),
    path('stream/', views.stream,name='stream'),
]

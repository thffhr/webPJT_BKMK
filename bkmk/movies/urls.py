from django.urls import path
from . import views


app_name = 'movies'

urlpatterns = [
    path('', views.main, name='main'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('genre_list/<int:genre_pk>/', views.genre_list, name='genre_list'),
    path('recommend/', views.recommend, name='recommend'),
]

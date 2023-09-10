from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('posts/', views.posts, name='posts'),
    path('article/<slug:s>/', views.article, name='article'),
]

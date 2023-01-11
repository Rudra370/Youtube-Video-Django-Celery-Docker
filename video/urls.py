from django.urls import path, include
from video import views

urlpatterns = [
    path('', views.VideoApiView.as_view()),
    path('query/', views.QueryVideoApiView.as_view()),
]
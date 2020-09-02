from django.urls import path

from .views import ListAgenda, DetailAgenda

urlpatterns = [
    path('', ListAgenda.as_view()),
    path('<int:pk>/', DetailAgenda.as_view()),
]

# api/urls.py
from django.urls import path
from .views import PollsList, PollsDetail

urlpatterns = [
    path('polls/', PollsList.as_view()),
    path('polls/<int:pk>/', PollsDetail.as_view()),
]

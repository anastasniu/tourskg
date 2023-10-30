from django.urls import path
from . import views

urlpatterns = [
    path('tours/', views.ToursList.as_view()),
]
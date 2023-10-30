from django.urls import path
from . import views

urlpatterns = [
    path('alltourslist/', views.ToursList.as_view()),

    # Auth
    path('signup/', views.signup),
    path('login/', views.login),
]
from django.urls import path
from . import views

urlpatterns = [
    path('alltourslist/', views.ToursList.as_view()),
    path('allcomments/', views.ReviewsList.as_view()),


    # Auth
    path('accounts/signup/', views.signup),
    path('accounts/login/', views.login),
]


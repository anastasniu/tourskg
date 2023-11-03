from django.urls import path
from . import views
from django.urls import path, include


urlpatterns = [
    path('alltourslist/', views.ToursList.as_view()),
    path('',include('comments.urls')),


    # Auth
    path('accounts/signup/', views.signup),
    path('accounts/login/', views.login),
]


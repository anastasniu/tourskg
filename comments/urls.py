from django.urls import path
from comments import views


urlpatterns = [
    path('api/comments/',views.ReviewList.as_view()),
]
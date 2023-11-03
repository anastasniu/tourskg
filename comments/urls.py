from django.urls import path
from . import views


urlpatterns = [
    path("review/<int:pk>/", views.create_review.as_view(), name="add_review"),
]
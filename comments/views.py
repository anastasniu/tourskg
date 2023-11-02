from django.shortcuts import redirect
from django.views.generic.base import View
from .models import Tour
from .forms import ReviewForm

# class AddReview(View):
#     """Отзывы"""
#     def post(self, request, pk):
#         form = ReviewForm(request.POST)
#         movie = Tour.objects.get(id=pk)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.movie = movie
#             form.save()
#         return redirect(movie.get_absolute_url())

from django.shortcuts import render, redirect
from .models import Review

def create_review(request, tour_id):
    if request.method == 'POST':
        user = request.user
        text = request.POST.get('text')
        tour = Tour.objects.get(id=tour_id)
        Review.objects.create(user=user, text=text, tour=tour)
    return redirect('tour_detail', tour_id=tour_id)

def view_reviews(request, tour_id):
    tour = Tour.objects.get(id=tour_id)
    reviews = Review.objects.filter(tour=tour, parent=None)

    return render(request, 'reviews.html', {'tour': tour, 'reviews': reviews})

from rest_framework import generics
from .serializers import ToursSerializer, ReviewsSerializer
from tours.models import Tour
from comments.models import Review
# Auth signup
from django.db import IntegrityError
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
# Auth login 
from django.contrib.auth import authenticate

class ToursList(generics.ListAPIView):

    serializer_class = ToursSerializer
    queryset = Tour.objects.all()

class ReviewsList(generics.ListAPIView):

    serializer_class = ReviewsSerializer
    queryset = Review.objects.all()

    
@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(
            username=data['username'],
            password=data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return JsonResponse({'token':str(token)},status=201)
        except IntegrityError:
            return JsonResponse({'error':'username taken. choose another username'},status=400)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(request, username=data['username'],
        password=data['password'])
        if user is None:
            return JsonResponse({'error':'unable to login. check username and password'},status=400)
        else:
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token.objects.create(user=user)
            return JsonResponse({'token':str(token)}, status=201)
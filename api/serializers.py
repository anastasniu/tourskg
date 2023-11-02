from rest_framework import serializers
from tours.models import Tour
from comments.models import Review

class ToursSerializer(serializers.ModelSerializer):
    region = serializers.StringRelatedField()
    class Meta:
        model = Tour
        fields = '__all__'



class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
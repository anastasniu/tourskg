from django.db import models
from django.contrib.auth.models import User
from tours.models import Tour
from datetime import datetime  

class Review(models.Model):  
    tours = models.ForeignKey(Tour, on_delete=models.CASCADE, related_name='comments',default=None)  
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='имя',default=None)  
    body = models.TextField("Сообщение", max_length=5000,default=None)  
    created = models.DateTimeField(default=datetime.now())  
    updated = models.DateTimeField(default=datetime.now())  
    active = models.BooleanField(default=True)  
      
    class Meta:  
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
        ordering = ('created',)  
          
    def __str__(self):  
        return f'Comment by {self.name} on {self.tours}'
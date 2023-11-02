from django.db import models
from django.contrib.auth.models import User
from tours.models import Tour

class Review(models.Model):
    """Отзывы"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    tour = models.ForeignKey(Tour, verbose_name="тур", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.tour}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
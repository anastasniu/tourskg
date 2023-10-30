from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _


class Region(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Tour(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название тура")
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    City = models.ForeignKey(City, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(
        verbose_name=_('Цена тура'),
        validators=[
            MinValueValidator(0, _("Цена не может быть меньше 0")),
            MaxValueValidator(100, _("Цена не может быть больше 10000"))
        ]
    )
    description = models.CharField(max_length=200, verbose_name="Описание тура")
    img = models.ImageField("Постер", upload_to='media/', null=True)

    def __str__(self) -> str:
        return self.title



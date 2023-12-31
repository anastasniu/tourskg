# Generated by Django 4.2.3 on 2023-11-01 17:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0006_address_remove_city_region_remove_tour_region_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tour',
            old_name='img',
            new_name='photo',
        ),
        migrations.RemoveField(
            model_name='tour',
            name='description',
        ),
        migrations.AddField(
            model_name='tour',
            name='desc',
            field=models.TextField(blank=True, null=True, verbose_name='Описание тура'),
        ),
        migrations.AddField(
            model_name='tour',
            name='distance',
            field=models.IntegerField(blank=True, null=True, verbose_name='Рассторяние от Бишкека'),
        ),
        migrations.AddField(
            model_name='tour',
            name='featured',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='tour',
            name='maxGroupSize',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0, 'Вместимость не может быть меньше 0'), django.core.validators.MaxValueValidator(15, 'Вместимость не может быть больше 15')], verbose_name='Вместимость группы'),
        ),
    ]

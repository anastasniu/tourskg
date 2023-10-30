# Generated by Django 4.2.3 on 2023-10-30 13:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название тура')),
                ('price', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0, 'Цена не может быть меньше 0'), django.core.validators.MaxValueValidator(100, 'Цена не может быть больше 10000')], verbose_name='Цена тура')),
                ('description', models.CharField(max_length=200, verbose_name='Описание тура')),
                ('img', models.ImageField(null=True, upload_to='media/', verbose_name='Постер')),
                ('City', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.city')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.region')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.region'),
        ),
    ]
# Generated by Django 4.2.7 on 2023-11-03 14:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0006_rename_post_review_tours_alter_review_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 3, 20, 37, 58, 535545)),
        ),
        migrations.AlterField(
            model_name='review',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 3, 20, 37, 58, 535545)),
        ),
    ]
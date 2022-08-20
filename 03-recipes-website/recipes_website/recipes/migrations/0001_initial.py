# Generated by Django 4.0.6 on 2022-08-20 16:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe_name', models.CharField(max_length=100)),
                ('ingredients', models.TextField()),
                ('directions', models.TextField()),
                ('prep', models.IntegerField()),
                ('servings', models.CharField(max_length=20)),
                ('date_recipe', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
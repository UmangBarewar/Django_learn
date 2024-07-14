# Generated by Django 5.0.6 on 2024-07-07 07:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fav_Anime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('1', 'Naruto'), ('1', 'Bleach'), ('1', 'Fullmetal'), ('1', 'Tokyo Revengers'), ('1', 'Highschool DXD')], max_length=25)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.TextField(max_length=500)),
                ('rating', models.IntegerField()),
                ('genre', models.CharField(max_length=25)),
                ('year', models.IntegerField()),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('episodes', models.IntegerField()),
            ],
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-08 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fav_anime',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='fav_anime',
            name='name',
            field=models.CharField(choices=[('Naruto', 'Naruto'), ('Bleach', 'Bleach'), ('Fullmetal', 'Fullmetal'), ('Tokyo Revengers', 'Tokyo Revengers'), ('Highschool DXD', 'Highschool DXD')], max_length=25),
        ),
    ]
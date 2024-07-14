from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
 
# Create your models here.
class Fav_Anime(models.Model):
    namez=[('Naruto','Naruto'),
           ('Bleach','Bleach'),
           ('Fullmetal','Fullmetal'),
           ('Tokyo Revengers','Tokyo Revengers'),
           ('Highschool DXD','Highschool DXD')] 
    #  this is enum
    name = models.CharField(max_length=25, choices=namez)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(default='')
    rating = models.IntegerField()
    genre = models.CharField(max_length=25)
    year = models.IntegerField()
    time = models.DateTimeField(default=timezone.now)
    episodes = models.IntegerField()

    def __str__(self):
        return self.name
    
# One to many

class Anime_Review(models.Model):
    anime=models.ForeignKey(Fav_Anime, on_delete=models.CASCADE\
                                ,related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating=models.IntegerField()
    description = models.TextField(default='')
          
    def __str__(self):
        return f'{self.user.username} review for {self.anime}'
# Many to many

class Stream(models.Model):
    name=models.CharField(max_length=100)
    origin=models.CharField(max_length=30)
    anime=models.ManyToManyField(Fav_Anime, related_name='streams')

    def __str__(self):
        return self.name

# One to One
class Censor_Certificate(models.Model):
    anime=models.OneToOneField(Fav_Anime,on_delete=models.CASCADE,\
                               related_name='certificate')
    certificate_no = models.CharField(max_length=10)
    issue_date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Certificate for {self.anime}'


from django import forms
from .models import Fav_Anime


class Stream_Form(forms.Form):
    Stream_Name = forms.ModelChoiceField(queryset=Fav_Anime.objects.all(),\
                                         label="Selecting anime")
#  for auto-linking any model from exisiting model we can simply 
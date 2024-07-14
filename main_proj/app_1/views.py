from django.shortcuts import render
from .models import Fav_Anime
from django.shortcuts import get_object_or_404
from .forms import Stream_Form

# Create your views here.
def app_1(request):
    animes = Fav_Anime.objects.all()
    return render(request, 'app_1/app_1.html', {'animes': animes})

def anime_detail(request, anime_id):
    anime = get_object_or_404(Fav_Anime, pk=anime_id)
    return render(request, 'app_1/detail.html', {'anime': anime})

def stream(request):
    selected_anime = None
    if request.method == 'POST':
        form = Stream_Form(request.POST)
        if form.is_valid():
            selected_anime = form.cleaned_data['Stream_Name']
    # this is done to deal the aftermath of submission of the form
    else:
        form = Stream_Form()
    #  this is done so that the form appears even if the user doesn't submits it 
    return render(request, 'app_1/stream.html', {'form': form, 'selected_anime': selected_anime})

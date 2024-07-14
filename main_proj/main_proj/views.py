from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # return HttpResponse("Hello World. I am Umang Barewar")
    return render(request,'website/index.html')
def about(request):
    return HttpResponse("about page")
def contact(request):
    return HttpResponse("contact page")
    
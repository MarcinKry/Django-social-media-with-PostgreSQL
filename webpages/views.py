from django.shortcuts import render
from .models import Slider, Team, HeaderDetail, AboutUsText
from youtubers.models import Youtuber

def home(request):
    sliders = Slider.objects.all()
    teams = Team.objects.all()
    featured_youtubers = Youtuber.objects.order_by('-created_date').filter(is_featured=True)
    all_tubers = Youtuber.objects.order_by('-created_date')
    data = {
        'sliders' : sliders, 
        'teams' : teams,
        'featured_youtubers': featured_youtubers,
        'all_tubers': all_tubers,
    }
    return render(request, 'webpages/home.html', data)

def about(request):
    teams = Team.objects.all()
    text = AboutUsText.objects.all()
    data = {
        'teams' : teams,
        'text' : text,
    }
    return render(request, 'webpages/about.html', data)

def services(request):
    return render(request, 'webpages/services.html')

def contact(request):
    return render(request, 'webpages/contact.html')

def header(request):
    header = HeaderDetail.objects.all()
    data = {
        'header' : header,
    }
    return render(request, 'includes/header.html', data)

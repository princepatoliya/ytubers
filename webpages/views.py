from django.shortcuts import render
from .models import Slider, Team
from youtubers.models import Youtuber

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')  
def home(request):
  sliders = Slider.objects.all()
  teams = Team.objects.all()
  features_youtubers = Youtuber.objects.order_by('-created_date').filter(is_featured = True)
  youtubers = Youtuber.objects.order_by('-created_date')

  data = {
    'sliders' : sliders,
    'teams' : teams,
    'features_youtubers' : features_youtubers,
    'youtubers' : youtubers,
  }

  return render(request, 'webpages/home.html', data)

def about(request):
  teams = Team.objects.all()
  data = {
    'teams':teams,
    }

  return render(request, 'webpages/about.html', data)

def profile(request):
  return render(request, 'webpages/profile.html')

def contact(request):
  return render(request, 'webpages/contact.html')
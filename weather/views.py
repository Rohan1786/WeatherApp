from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import City
from .forms import CityForm
import requests

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1'

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['name']
            if not City.objects.filter(name=city_name).exists():
                form.save()

    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:
        try:
            r = requests.get(url.format(city.name)).json()
            if 'main' in r and 'temp' in r['main'] and 'weather' in r and len(r['weather']) > 0:
                city_weather = {
                    'id': city.id,
                    'city': city.name,
                    'temperature': r['main']['temp'],
                    'description': r['weather'][0]['description'],
                    'icon': r['weather'][0]['icon'],
                }
            else:
                city_weather = {
                    'id': city.id,
                    'city': city.name,
                    'temperature': 'N/A',
                    'description': 'N/A',
                    'icon': 'N/A',
                }
        except requests.exceptions.RequestException as e:
            city_weather = {
                'id': city.id,
                'city': city.name,
                'temperature': 'N/A',
                'description': f'Error: {e}',
                'icon': 'N/A',
            }

        weather_data.append(city_weather)

    context = {'weather_data': weather_data, 'form': form}

    return render(request, 'weather/weather.html', context)

def delete_city(request, city_id):
    city = get_object_or_404(City, id=city_id)
    city.delete()
    return redirect('index')

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import City
from .forms import CityForm
import requests

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=271d1234d3f497eed5b1d80a07b3fcd1'

    query = request.GET.get('q')
    if query:
        searched_cities = City.objects.filter(name__icontains=query).order_by('name')
    else:
        searched_cities = City.objects.none()

    all_cities = City.objects.all().order_by('name')
    remaining_cities = [city for city in all_cities if city not in searched_cities]

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city_name = form.cleaned_data['name']
            if not City.objects.filter(name=city_name).exists():
                form.save()
        return redirect('index')

    form = CityForm()

    weather_data = []

    for city in list(searched_cities) + remaining_cities:
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

    context = {'weather_data': weather_data, 'form': form, 'query': query}

    return render(request, 'weather/weather.html', context)

def delete_city(request, city_id):
    city = get_object_or_404(City, id=city_id)
    city.delete()
    return redirect('index')

import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import *


# Create your views here.

def index(request):
  api_key = '2fc4e20dda5047a1875172648220108'
  city = 'Moscow'
  url = 'https://api.weatherapi.com/v1/forecast.json?key={}&q={}&days=7&aqi=no&alerts=no'

  form = GetCity()
  if request.method == 'POST':
    form = GetCity(request.POST)
    if form.is_valid():
      city = form.cleaned_data['city']
  else:
    form = GetCity()

  

  res = requests.get(url.format(api_key, city)).json()



  all_info = []

  for i in range(0, 7):
    date = res["forecast"]["forecastday"][i]["hour"][0]["time"].split('-')
    last_date = date[-1].split(' ')
    date.pop()
    date.append(last_date[0])
    date.append(last_date[1])

    monthes = {
      '01': ['January', 'Jan'],
      '02': ['February', 'Feb'],
      '03': ['March', 'Mar'],
      '04': ['April', 'Apr'],
      '05': ['May', 'May'],
      '06': ['June', 'June'],
      '07': ['July', 'July'],
      '08': ['August', 'Aug'],
      '09': ['September', 'Sept'],
      '10': ['October', 'Oct'],
      '11': ['November', 'Nov'],
      '12': ['December', 'Dec'],
    }

    my_hour = 22
    day_info = {
      'name': res["location"]["name"],
      'min_date': monthes[date[1]][1]+" "+date[2],
      'mid_date': monthes[date[1]][0]+" "+date[2],
      'max_date': res["forecast"]["forecastday"][i]["hour"][my_hour]["time"],
      'temp': res["forecast"]["forecastday"][i]["hour"][my_hour]["temp_c"],
      'feels': res["forecast"]["forecastday"][i]["hour"][my_hour]["feelslike_c"],
      'status': res["forecast"]["forecastday"][i]["hour"][my_hour]["condition"]["text"],
      'status_icon': res["forecast"]["forecastday"][i]["hour"][my_hour]["condition"]["icon"],
      'wind_speed': res["forecast"]["forecastday"][i]["hour"][my_hour]["wind_kph"],
      'cloud': res["forecast"]["forecastday"][i]["hour"][my_hour]["cloud"]
    }
    all_info.append(day_info)

  all_day_info = { 'day_info': all_info, 'city': city, 'form': form }

  return render(request, 'wheather/index.html', all_day_info)
  #return render(request, 'wheather/index2.html')
import requests
from django.shortcuts import render

# Create your views here.

def index(request):
  api_key = '2fc4e20dda5047a1875172648220108'
  city = 'Moscow'

  url = 'https://api.weatherapi.com/v1/forecast.json?key={}&q={}&days=7&aqi=no&alerts=no'

  res = requests.get(url.format(api_key, city)).json()

  print(res["forecast"]["forecastday"][0]["hour"][0]["temp_c"])

  day_info = {
    'name': res["location"]["name"],
    # 'min_date': ,
    # 'mid_date': ,
    'max_date': res["forecast"]["forecastday"][0]["hour"][0]["time"],
    'temp': res["forecast"]["forecastday"][0]["hour"][0]["temp_c"],
    'feels': res["forecast"]["forecastday"][0]["hour"][0]["feelslike_c"],
    'status': res["forecast"]["forecastday"][0]["hour"][0]["condition"]["text"],
    'status_icon': res["forecast"]["forecastday"][0]["hour"][0]["condition"]["icon"],
    'wind_speed': res["forecast"]["forecastday"][0]["hour"][0]["wind_kph"],
    'cloud': res["forecast"]["forecastday"][0]["hour"][0]["cloud"]
  }

  all_info = { 'day_info': day_info }

  return render(request, 'wheather/index.html', all_info)
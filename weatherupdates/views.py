import requests
import json
from datetime import datetime
from django.shortcuts import render

# the index() will handle all the app's logic
def index(request):
    # if there are no errors the code inside try will execute
    try:
  
        if request.method == 'POST':
              
            city_name = request.POST.get('city')
             
            url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid=e307084c4507dcec68f39adf684659b9&units=metric'
              
            response = requests.get(url)
            x = response.json()
            print(x)
           
            current_time = datetime.now()
           
            formatted_time = current_time.strftime("%A, %B %d %Y, %H:%M:%S %p")
            
            city_weather_update = {
                'city': city_name,
                'description': x['weather'][0]['description'],
                'icon': x['weather'][0]['icon'],
                'temperature': 'Temperature: ' + str(x['main']['temp']) + ' °C',
                'country_code': x['sys']['country'],
                'wind': 'Wind: ' + str(x['wind']['speed']) + 'km/h',
                'humidity': 'Humidity: ' + str(x['main']['humidity']) + '%',
                'time': formatted_time
            }
        
        else:
            city_weather_update = {}
        context = {'city_weather_update': city_weather_update}
        return render(request, 'weatherupdates/home.html', context)

    except:
        return render(request, 'weatherupdates/404.html')



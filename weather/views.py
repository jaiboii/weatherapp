import requests
from django.shortcuts import render

def home(request):
    weather_data = None
    error_message = None
    if request.method == 'POST':
        city = request.POST.get('city')
        api_key = '5e844432275f51a06d32164ee5b12946'
        api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'
        
        response = requests.get(api_url)
        print(response.url)  # Print the URL to ensure it's correct
        print(response.status_code)  # Print the status code
        print(response.json())  # Print the response content
        
        if response.status_code == 200:
            weather_data = response.json()
        else:
            error_message = response.json().get('message', 'An error occurred')
    
    context = {'weather_data': weather_data, 'error_message': error_message}
    return render(request, 'weather/home.html', context)

import requests
import json

def get_weather(api_key, city, units='metric'):
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'q': city,
        'units': 'metric',
        'appid': api_key
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: Unable to fetch weather data for {city}.")
        return None

def display_weather(weather_data):
    
        
    if units == 'celsius' :
        temperature = weather_data['main']['temp']
        unit_symbol = '°C'
    else:
    # Convert from Celsius to Fahrenheit
        temperature = (weather_data['main']['temp'] * 9/5) + 32
        unit_symbol = '°F'
    
    print(f"Temperature: {temperature}{unit_symbol}")

    if weather_data:
        print(f"Weather in {weather_data['name']}, {weather_data['sys']['country']}:")
       # print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print(f"Wind Speed: {weather_data['wind']['speed']} m/s")
        print(f"Conditions: {weather_data['weather'][0]['description']}")
    else:
        print("Weather data not available.")

if __name__ == "__main__":
    api_key = 'c007a2217ecb118f330c3a382e60217f'  # Replace with your OpenWeatherMap API key
    city = input("Enter a city ")
    units = input("Choose units (Celsius/Fahrenheit): ").lower()

    if units not in ['celsius', 'fahrenheit']:
        print("Invalid unit. Defaulting to Celsius.")
        units = 'celsius'

    weather_data = get_weather(api_key, city, units)

    display_weather(weather_data)

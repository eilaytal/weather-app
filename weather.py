import requests

# Function to get coordinates and country for a city
def get_coordinates(city):
    url = "https://geocoding-api.open-meteo.com/v1/search"
    params = {"name": city, "count": 1, "language": "en", "format": "json"}
    data = requests.get(url, params=params).json()['results'][0]
    return data['latitude'], data['longitude'], data['country']

# Function to get weather data for a city
def get_weather_data(city):
    latitude, longitude, country = get_coordinates(city)
    url_of_weather = "https://api.open-meteo.com/v1/forecast"
    params_of_weather = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": ["temperature_2m_max", "temperature_2m_min", "relative_humidity_2m_mean"],
        "timezone": "auto"
    }
    data_of_weather = requests.get(url_of_weather, params=params_of_weather).json()
    return {
        "times": data_of_weather['daily']['time'],
        "temp_max": data_of_weather['daily']['temperature_2m_max'],
        "temp_min": data_of_weather['daily']['temperature_2m_min'],
        "humidity": data_of_weather['daily']['relative_humidity_2m_mean'],
        "country": country
    }

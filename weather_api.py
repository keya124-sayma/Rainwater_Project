import requests

# Replace 'YOUR_API_KEY' with the actual API key you got from OpenWeatherMap
API_KEY = "YOUR7b8c713dfbd35562f838707bff0e4550_API_KEY"

def get_current_rainfall(city):
    """
    Fetch the current rainfall (in mm) for a given city.
    """
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,             # City name (e.g., Dhaka)
        'appid': API_KEY,      # Your API key
        'units': 'metric'      # We want the rainfall in millimeters
    }

    try:
        # Send a request to OpenWeatherMap API
        response = requests.get(base_url, params=params)
        data = response.json()

        # Check if there's rainfall data in the response
        if 'rain' in data and '1h' in data['rain']:
            return data['rain']['1h']  # Return rainfall in last 1 hour (in mm)
        else:
            return 0  # No rainfall in the last hour
    except:
        return None  # If there's an error (e.g., no internet), return None

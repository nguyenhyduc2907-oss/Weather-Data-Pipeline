import requests
key = "bd70422068c988c1dc9b11c6b3a13bd8"
lat = "51.48"
lon = "7.222"
api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={key}"

# Uncomment the following function to fetch data from the Weatherstack API
def fetch_data ():
    print ("Fetching Bochum weather data from the OpenWeatherMap API...")
    try:
        response = requests.get(api_url)
        response.raise_for_status() # Raise an error for bad responses (4xx or 5xx)
        print("API response received successfully.")
        return response.json()  # Return the JSON data from the response
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data from the API: {e}")
        raise

fetch_data() 

def mock_fetch_data():
    return {'coord': {'lon': 7.222, 'lat': 51.48}, 
            'weather': [{'id': 501, 'main': 'Rain', 'description': 'moderate rain', 'icon': '10n'}], 
            'base': 'stations', 
            'main': {'temp': 280.93, 'feels_like': 280.17, 'temp_min': 279.5, 'temp_max': 281.91, 'pressure': 994, 'humidity': 92, 'sea_level': 994, 'grnd_level': 983}, 
            'visibility': 4179, 
            'wind': {'speed': 1.59, 'deg': 281, 'gust': 2.87}, 
            'rain': {'1h': 1.15}, 'clouds': {'all':100}, 
            'dt': 1795127335, 
            'sys': {'type': 5, 'id': 50000597, 'country': 'DE', 'sunrise': 1795071335, 'sunset': 1795102658}, 
            'timezone': 3600, 
            'id': 2947416, 
            'name': 'Bochum', 
            'cod': 200}
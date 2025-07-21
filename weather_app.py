import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # or "imperial" for Fahrenheit
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None

def weather_app():
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"  # Replace with your actual API key

    if api_key == "YOUR_OPENWEATHERMAP_API_KEY":
        print("Please get an API key from OpenWeatherMap (https://openweathermap.org/api) and replace 'YOUR_OPENWEATHERMAP_API_KEY' in the code.")
        return

    while True:
        city = input("Enter city name (or 'quit' to exit): ")
        if city.lower() == 'quit':
            break

        weather_data = get_weather(city, api_key)

        if weather_data:
            main_weather = weather_data["weather"][0]["main"]
            description = weather_data["weather"][0]["description"]
            temp = weather_data["main"]["temp"]
            feels_like = weather_data["main"]["feels_like"]
            humidity = weather_data["main"]["humidity"]

            print(f"\nWeather in {city}:")
            print(f"Condition: {main_weather} ({description})")
            print(f"Temperature: {temp}°C (Feels like: {feels_like}°C)")
            print(f"Humidity: {humidity}%")
        else:
            print("Could not retrieve weather data for that city. Please check the city name.")

if __name__ == "__main__":
    weather_app()

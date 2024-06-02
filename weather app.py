import requests

def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    return requests.get(url).json()

def display_weather(data):
    if data["cod"] != 200:
        print(f"Error: {data['message']}")
        return

    city = data["name"]
    country = data["sys"]["country"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"]

    print(f"Weather in {city}, {country}:")
    print(f"Temperature: {temp}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {condition.capitalize()}")

def main():
    api_key = "cc8f6fa435b74c5e108178cbc2584171" 
    location = input("Enter city name or ZIP code: ")
    weather_data = get_weather(api_key, location)
    display_weather(weather_data)

if __name__ == "__main__":
    main()

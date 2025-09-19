import requests
import matplotlib.pyplot as plt

API_KEY = "7da66a3909914b192d84bac641ef9fcf"  
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    try:
        params = {"q": city, "appid": API_KEY, "units": "metric"}
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data.get("cod") != 200:
            return None

        return {
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "temp_min": data["main"]["temp_min"],
            "temp_max": data["main"]["temp_max"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "condition": data["weather"][0]["description"].title()
        }
    except Exception as e:
        print("Error:", e)
        return None

def show_weather_chart(city):
    data = get_weather(city)
    if not data:
        print("❌ Could not fetch weather data. Check city name or API key.")
        return

    print(f"\n📍 Weather in {city}")
    print(f"🌡 Temperature: {data['temperature']}°C")
    print(f"🤒 Feels Like: {data['feels_like']}°C")
    print(f"🔼 Max Temp: {data['temp_max']}°C")
    print(f"🔽 Min Temp: {data['temp_min']}°C")
    print(f"💧 Humidity: {data['humidity']}%")
    print(f"📊 Pressure: {data['pressure']} hPa")
    print(f"☁ Condition: {data['condition']}")

    labels = ["Temp", "Feels Like", "Min Temp", "Max Temp", "Humidity"]
    values = [
        data["temperature"],
        data["feels_like"],
        data["temp_min"],
        data["temp_max"],
        data["humidity"]
    ]

    plt.bar(labels, values, color=["orange", "red", "blue", "green", "cyan"])
    plt.title(f"Weather in {city}")
    plt.ylabel("Values")
    plt.show()

if __name__ == "__main__":
    city = input("Enter city name: ")
    show_weather_chart(city)

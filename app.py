import tkinter as tk
from tkinter import messagebox
import requests
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def show_weather():
    city = entry_city.get().strip()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name")
        return

    try:
        API_KEY = "7da66a3909914b192d84bac641ef9fcf"  
        BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
        params = {"q": city, "appid": API_KEY, "units": "metric"}

        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data.get("cod") != 200:
            messagebox.showerror("Error", f"❌ Could not fetch weather for {city}")
            return

        weather_data = {
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "temp_min": data["main"]["temp_min"],
            "temp_max": data["main"]["temp_max"],
            "humidity": data["main"]["humidity"],
            "pressure": data["main"]["pressure"],
            "condition": data["weather"][0]["description"].title()
        }

        details = (
            f"📍 Weather in {city}\n"
            f"🌡 Temperature: {weather_data['temperature']}°C\n"
            f"🤒 Feels Like: {weather_data['feels_like']}°C\n"
            f"🔼 Max Temp: {weather_data['temp_max']}°C\n"
            f"🔽 Min Temp: {weather_data['temp_min']}°C\n"
            f"💧 Humidity: {weather_data['humidity']}%\n"
            f"📊 Pressure: {weather_data['pressure']} hPa\n"
            f"☁ Condition: {weather_data['condition']}"
        )
        weather_output.config(text=details)

        for widget in frame_chart.winfo_children():
            if widget != weather_output:
                widget.destroy()

        fig = Figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(111)

        labels = ["Temp", "Feels Like", "Min", "Max", "Humidity"]
        values = [
            weather_data["temperature"],
            weather_data["feels_like"],
            weather_data["temp_min"],
            weather_data["temp_max"],
            weather_data["humidity"]
        ]
        colors = ["orange", "red", "blue", "green", "cyan"]
        ax.bar(labels, values, color=colors)

        ax.set_title(f"Weather Chart for {city}")
        ax.set_ylabel("Values")

        canvas = FigureCanvasTkAgg(fig, master=frame_chart)
        canvas.draw()
        canvas.get_tk_widget().pack(side="right", fill="both", expand=True, padx=10)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

root = tk.Tk()
root.title("🌦 Weather Dashboard")
root.geometry("800x500")

frame_input = tk.Frame(root, bg="white")
frame_input.pack(fill="x", padx=10, pady=10)

tk.Label(frame_input, text="Enter City:", bg="white").pack(side="left")
entry_city = tk.Entry(frame_input)
entry_city.pack(side="left", padx=5)
btn_weather = tk.Button(frame_input, text="Check Weather", bg="blue", fg="white", command=show_weather)
btn_weather.pack(side="left", padx=5)

frame_chart = tk.Frame(root, bg="white")
frame_chart.pack(fill="both", expand=True, padx=10, pady=10)

weather_output = tk.Label(
    frame_chart,
    text="",
    bg="white",
    justify="left",
    font=("Arial", 11),
    anchor="nw"
)
weather_output.pack(side="left", fill="both", expand=True, padx=10, pady=10)

root.mainloop()

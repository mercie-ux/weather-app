import tkinter as tk
from tkinter import messagebox
import requests
# city search
def get_weather(city):
    # API call
    api_key = "your_actual_api_key_here"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    response = requests.get(complete_url)
    return response.json()
    # fetch weather details for city requested by user
def show_weather():
    city = city_entry.get()
    weather = get_weather(city)
    # temperature
    if weather.get("cod") != "404":
        main = weather.get("main", {})
        wind = weather.get("wind", {})
        weather_desc = weather.get("weather", [{}])[0].get("description", "No description available")
        temp = main.get("temp", "N/A")
        pressure = main.get("pressure", "N/A")
        humidity = main.get("humidity", "N/A")
        wind_speed = wind.get("speed", "N/A")

        weather_info = f"Temperature: {temp}°C\nPressure: {pressure}hPa\nHumidity: {humidity}%\nWind Speed: {wind_speed}m/s\nDescription: {weather_desc}"
    else:
        weather_info = "City Not Found!"

    messagebox.showinfo("Weather Info", weather_info)
# adding the received info into the screen
app = tk.Tk()
app.title("Weather App")
# search bar and button
city_label = tk.Label(app, text="Enter city name:")
city_label.pack()

city_entry = tk.Entry(app)
city_entry.pack()

get_weather_button = tk.Button(app, text="Get Weather", command=show_weather)
get_weather_button.pack()

app.mainloop()
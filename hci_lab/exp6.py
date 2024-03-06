import tkinter as tk
from tkinter import ttk, messagebox
import requests
import os

current_unit= 'C'
def get_weather():
    global current_unit
    api_key = '5cc55aa0a18fcbac035128efb4996d1a'
    city = city_combobox.get()

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    weather_data = response.json()

    if weather_data["cod"] == 200:
        if current_unit == "C":
            temperature_label.config(text=f"Temperature: {weather_data['main']['temp']}°C")
        else:
            temperature_in_fahrenheit = (weather_data['main']['temp'] * 9 / 5) + 32
            temperature_in_fahrenheit = round(temperature_in_fahrenheit, 2)
            temperature_label.config(text=f"Temperature: {temperature_in_fahrenheit}°F")
        humidity_label.config(text=f"Humidity: {weather_data['main']['humidity']}%")
        wind_label.config(text=f"Wind Speed: {weather_data['wind']['speed']} m/s")
        condition_label.config(text=f"Weather Condition: {weather_data['weather'][0]['main']}")
        city_weather_label.config(text=f"Weather in {city}: {weather_data['weather'][0]['description']}")
    else:
        messagebox.showerror("Error", "City not found!")


def clear_weather():
    temperature_label.config(text="Temperature: ")
    humidity_label.config(text="Humidity: ")
    wind_label.config(text="Wind Speed: ")
    condition_label.config(text="Weather Condition: ")
    city_weather_label.config(text="Weather in Selected City: ")

def switch_unit():
    global current_unit
    
    if current_unit == "C":
        current_unit = "F"
    else:
        current_unit = "C"
    
    city = city_combobox.get()
    get_weather()


# Create the main window
root = tk.Tk()
root.title("Weather App by Shubharthak")
root.geometry("400x400")
root.configure(bg="#E0FFFF")  # Set background color to light blue

# Define pastel colors
pastel_blue = "#AEEEEE"
pastel_pink = "#FFB6C1"
pastel_green = "#98FB98"
pastel_yellow = "#FFFFE0"

# Create the header
header_label = tk.Label(root, text="Gestalt Principles", font=("Arial", 18, "bold"), bg=pastel_yellow)
header_label.pack(pady=10)

# Create frames
input_frame = tk.Frame(root, bg=pastel_blue)
input_frame.pack(pady=10)

output_frame = tk.Frame(root, bg=pastel_pink)
output_frame.pack(pady=20)

city_label = tk.Label(input_frame, text="Select City: ", font=("Arial", 14), bg=pastel_blue)
city_label.grid(row=0, column=0, padx=10, pady=10)

cities = ["Punjab", "Delhi", "New York", "London", "Paris", "Tokyo", "Sydney"]
city_combobox = ttk.Combobox(input_frame, values=cities, width=30, font=("Arial", 12))
city_combobox.grid(row=0, column=1, padx=10, pady=10)
city_combobox.current(0)

get_weather_button = tk.Button(input_frame, text="Get Weather", command=get_weather, font=("Arial", 12), bg=pastel_green)
get_weather_button.grid(row=0, column=2, padx=10, pady=10)

# Additional label for displaying city weather
city_weather_label = tk.Label(input_frame, text="Weather in Selected City: ", font=("Arial", 14), bg=pastel_blue)
city_weather_label.grid(row=1, column=0, columnspan=3, pady=5)

# Create output labels
temperature_label = tk.Label(output_frame, text="Temperature: ", font=("Arial", 14), bg=pastel_pink)
temperature_label.pack(pady=5)

humidity_label = tk.Label(output_frame, text="Humidity: ", font=("Arial", 14), bg=pastel_pink)
humidity_label.pack(pady=5)

wind_label = tk.Label(output_frame, text="Wind Speed: ", font=("Arial", 14), bg=pastel_pink)
wind_label.pack(pady=5)

condition_label = tk.Label(output_frame, text="Weather Condition: ", font=("Arial", 14), bg=pastel_pink)
condition_label.pack(pady=5)

# Buttons for additional functionality
switch_unit_button = tk.Button(output_frame, text="Switch Unit", command=switch_unit, font=("Arial", 12), bg=pastel_green)
switch_unit_button.pack(pady=5)

clear_weather_button = tk.Button(output_frame, text="Clear Weather", command=clear_weather, font=("Arial", 12), bg=pastel_green)
clear_weather_button.pack(pady=5)


root.mainloop()
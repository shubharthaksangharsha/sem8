import tkinter as tk
from tkinter import ttk, messagebox
import requests
import os 

def get_weather():
    api_key = os.environ.get('OPENWEATHERMAP_API_KEY')  # Replace "YOUR_API_KEY" with your actual API key
    city = city_combobox.get()

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    weather_data = response.json()

    if weather_data["cod"] == 200:
        temperature_label.config(text=f"Temperature: {weather_data['main']['temp']}°C")
        humidity_label.config(text=f"Humidity: {weather_data['main']['humidity']}%")
        wind_label.config(text=f"Wind Speed: {weather_data['wind']['speed']} m/s")
        condition_label.config(text=f"Weather Condition: {weather_data['weather'][0]['main']}")
    else:
        messagebox.showerror("Error", "City not found!")

# Create the main window
root = tk.Tk()
root.title("Weather App by Shubharthak")

style = ttk.Style()
style.configure('TCombobox', font=('Arial', 14))  # Adjust the font size here

# Create frames
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

output_frame = tk.Frame(root)
output_frame.pack(pady=20)

city_label = tk.Label(input_frame, text="Select City: ", font=("Arial", 18))
city_label.grid(row=0, column=0)

cities = ["Punjab", "Delhi", "New York", "London", "Paris", "Tokyo", "Sydney"]
city_combobox = ttk.Combobox(input_frame, values=cities, width=50, font=("Arial", 23))
city_combobox.grid(row=0, column=1)
city_combobox.current(0)
city_combobox.config(font=("Arial", 23))  # Set font size for dropdown text


get_weather_button = tk.Button(input_frame, text="Get Weather", command=get_weather, font=("Arial", 22))
get_weather_button.grid(row=0, column=2)

# Create output labels
temperature_label = tk.Label(output_frame, text="Temperature: ", font=("Arial", 18))
temperature_label.pack()

humidity_label = tk.Label(output_frame, text="Humidity: ", font=("Arial", 18))
humidity_label.pack()

wind_label = tk.Label(output_frame, text="Wind Speed: ", font=("Arial", 18))
wind_label.pack()

condition_label = tk.Label(output_frame, text="Weather Condition: ", font=("Arial", 18))
condition_label.pack()
root.geometry('1280x720')
root.mainloop()

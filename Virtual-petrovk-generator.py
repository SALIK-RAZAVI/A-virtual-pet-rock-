import tkinter as tk
import random

def get_weather():
    weather_conditions = ["Sunny", "Rainy", "Cloudy", "Snowy", "Windy", "Stormy"]
    return random.choice(weather_conditions)

def get_rock_state(weather):
    if weather == "Sunny":
        return "yellow", "Happy"
    elif weather == "Rainy":
        return "blue", "Sad"
    elif weather == "Cloudy":
        return "gray", "Indifferent"
    elif weather == "Snowy":
        return "white", "Excited"
    elif weather == "Windy":
        return "green", "Energetic"
    elif weather == "Stormy":
        return "purple", "Scared"
    elif weather == "foggy":
        return "orange", "Pride"
    elif weather == "Humidity":
        return "skyblue", "Hope"

def update_rock():
    weather = get_weather()
    color, mood = get_rock_state(weather)
    canvas.itemconfig(rock, fill=color)
    mood_label.config(text=f"Mood: {mood}")
    weather_label.config(text=f"Weather: {weather}")
    root.after(3000, update_rock)  

root = tk.Tk()
root.title("Virtual Pet Rock")
root.geometry("300x300")

canvas = tk.Canvas(root, width=300, height=200)
canvas.pack()

rock = canvas.create_oval(100, 50, 200, 150, fill="gray")

mood_label = tk.Label(root, text="Mood: Indifferent", font=("Helvetica", 14))
mood_label.pack(pady=10)

weather_label = tk.Label(root, text="Weather: Cloudy", font=("Helvetica", 14))
weather_label.pack(pady=10)

update_rock()

root.mainloop()
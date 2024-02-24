import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import pygame
import os

def play_music():
    pygame.mixer.music.unpause()

def pause_music():
    pygame.mixer.music.pause()

def stop_music():
    pygame.mixer.music.stop()

def select_music():
    file_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp3 *.wav")])
    if file_path:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

def increase_volume():
    current_volume = pygame.mixer.music.get_volume()
    if current_volume < 1.0:
        pygame.mixer.music.set_volume(current_volume + 0.1)

def decrease_volume():
    current_volume = pygame.mixer.music.get_volume()
    if current_volume > 0.0:
        pygame.mixer.music.set_volume(current_volume - 0.1)

def previous_track():
    # Add functionality to play the previous track
    pass

def next_track():
    # Add functionality to play the next track
    pass

def switch_to_complex_music_app():
    os.system("python exp5_exp.py")

# Initialize Pygame mixer
pygame.mixer.init()

# Create main window
root = tk.Tk()
root.title("Music Player - Simple Screen Interface")

# Define custom style with larger font
style = ttk.Style()
style.configure('Custom.TButton', font=('Helvetica', 15, 'bold'), background='#FFD1DC', foreground='#000000') # Green button color

# Buttons
play_button = ttk.Button(root, text="Play", command=play_music, width=20, style='Custom.TButton')
pause_button = ttk.Button(root, text="Pause", command=pause_music, width=20, style='Custom.TButton')
stop_button = ttk.Button(root, text="Stop", command=stop_music, width=20, style='Custom.TButton')
select_button = ttk.Button(root, text="Select Music", command=select_music, width=20, style='Custom.TButton')
increase_volume_button = ttk.Button(root, text="+ Volume", command=increase_volume, width=20, style='Custom.TButton')
decrease_volume_button = ttk.Button(root, text="- Volume", command=decrease_volume, width=20, style='Custom.TButton')
next_button = ttk.Button(root, text="Next Track", command=next_track, width=20, style='Custom.TButton')
switch_button = ttk.Button(root, text="Switch to Complex Music App", command=switch_to_complex_music_app, width=30, style='Custom.TButton')

# Label
label_text = ttk.Label(root, text="Music App designed by Shubharthak", font=('Helvetica', 18, 'bold'), background='sky blue')

# Separator
separator = ttk.Separator(root, orient='horizontal')

# Grid layout
play_button.grid(row=0, column=0, padx=10, pady=10)
pause_button.grid(row=0, column=1, padx=10, pady=10)
stop_button.grid(row=0, column=2, padx=10, pady=10)
select_button.grid(row=1, column=0, padx=10, pady=10)
increase_volume_button.grid(row=1, column=1, padx=10, pady=10)
decrease_volume_button.grid(row=1, column=2, padx=10, pady=10)
next_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="ew")
switch_button.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="ew")
label_text.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
separator.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky="ew")
separator.config(background=None)

# Load and display image
image = Image.open("music3.png")
image = image.resize((300, 250), Image.LANCZOS)  # Resize image as needed
photo = ImageTk.PhotoImage(image)
label_image = ttk.Label(root, image=photo)
label_image.grid(row=8, column=0, columnspan=1, padx=10, pady=10)

# Load and display image
image2 = Image.open("music4.png")
image2 = image2.resize((300, 250), Image.LANCZOS)  # Resize image as needed
photo2 = ImageTk.PhotoImage(image2)
label_image = ttk.Label(root, image=photo2)
label_image.grid(row=8, column=1, columnspan=2, padx=10, pady=10)



# Set window size
root.geometry("900x600")
# root.config(background='sky blue')

# Run the application
root.mainloop()

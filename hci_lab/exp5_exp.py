import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pygame
import os

def play_music():
    global paused
    if paused:
        pygame.mixer.music.unpause()
        result_label.config(text="Music resumed", foreground="green")
        paused = False
    else:
        pygame.mixer.music.load(selected_song.get())
        pygame.mixer.music.play()
        update_current_song_label()
        result_label.config(text="Music is playing", foreground="green")

def pause_music():
    global paused
    pygame.mixer.music.pause()
    result_label.config(text="Music paused", foreground="blue")
    paused = True

def stop_music():
    pygame.mixer.music.stop()
    result_label.config(text="Music stopped", foreground="red")

def select_music():
    file_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp3 *.wav")])
    if file_path:
        selected_song.set(file_path)
        update_current_song_label()
        result_label.config(text="Selected song: " + os.path.basename(file_path), foreground="black")

def increase_volume():
    current_volume = pygame.mixer.music.get_volume()
    if current_volume < 1.0:
        pygame.mixer.music.set_volume(current_volume + 0.1)
        result_label.config(text="Volume increased", foreground="green")

def decrease_volume():
    current_volume = pygame.mixer.music.get_volume()
    if current_volume > 0.0:
        pygame.mixer.music.set_volume(current_volume - 0.1)
        result_label.config(text="Volume decreased", foreground="red")

def previous_track():
    # Add functionality to play the previous track
    result_label.config(text="Playing previous track", foreground="black")

def next_track():
    # Add functionality to play the next track
    result_label.config(text="Playing next track", foreground="black")

def toggle_repeat():
    global repeat_mode
    repeat_mode = not repeat_mode
    result_label.config(text="Repeat mode toggled", foreground="black")

def toggle_shuffle():
    # Add functionality to toggle shuffle mode
    result_label.config(text="Shuffle mode toggled", foreground="black")

def update_current_song_label():
    current_song = os.path.basename(selected_song.get())
    current_song_label.config(text="Current Song: " + current_song, foreground="black")

def music_end_event():
    global repeat_mode
    if repeat_mode:
        pygame.mixer.music.play()
    else:
        stop_music()

# Initialize Pygame mixer
pygame.mixer.init()

# Create main window
root = tk.Tk()
root.title("Music Player - Complex Screen Interfac  11111e")

# Set background wallpaper
background_image = tk.PhotoImage(file="music2.png")
# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# Calculate the zoom factors to lower the ratio
zoom_width = int(screen_width * 0.9 / background_image.width())
zoom_height = int(screen_height * 0.9 / background_image.height())
# Choose the smaller zoom factor to maintain aspect ratio
zoom_factor = min(zoom_width, zoom_height)
# Resize the image with the calculated zoom factor
background_image = background_image.zoom(zoom_factor, zoom_factor)
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)




# Global variables
selected_song = tk.StringVar()
paused = False
repeat_mode = False

# Set styles
style = ttk.Style()
# Set styles for buttons
style.configure("TButton", padding=(20, 10), font=('Helvetica', 20, 'bold'), foreground="black", background="#FFD1DC")
style.map("TButton", background=[("active", "green")])  # Change button color when active (clicked)

# Set styles for labels
style.configure("TLabel", padding=(10, 10), font=('Helvetica', 20, 'bold'), foreground="black", background="#FFD1DC")

''''''
style.configure("TButton", padding=(20, 10), font=('Helvetica', 20, 'bold'), foreground="black", background="#FFD1DC")
style.configure("TLabel", padding=(10, 10), font=('Helvetica', 20, 'bold'))

# Buttons
button_width = 30

play_button = ttk.Button(root, text="Play", command=play_music, width=button_width, style="TButton")
play_button.grid(row=0, column=0, padx=15, pady=15)

pause_button = ttk.Button(root, text="Pause", command=pause_music, width=button_width)
pause_button.grid(row=0, column=1, padx=15, pady=15)

stop_button = ttk.Button(root, text="Stop", command=stop_music, width=button_width)
stop_button.grid(row=0, column=2, padx=15, pady=15)

select_button = ttk.Button(root, text="Select Music", command=select_music, width=button_width)
select_button.grid(row=1, column=0, columnspan=3, padx=15, pady=15)

volume_label = ttk.Label(root, text="Volume Control:")
volume_label.grid(row=2, column=0, columnspan=3, padx=15, pady=15)

increase_volume_button = ttk.Button(root, text="Increase Volume", command=increase_volume, width=button_width)
increase_volume_button.grid(row=3, column=0, padx=15, pady=15)

decrease_volume_button = ttk.Button(root, text="Decrease Volume", command=decrease_volume, width=button_width)
decrease_volume_button.grid(row=3, column=1, padx=15, pady=15)

previous_button = ttk.Button(root, text="Previous", command=previous_track, width=button_width)
previous_button.grid(row=4, column=0, padx=15, pady=15)

next_button = ttk.Button(root, text="Next", command=next_track, width=button_width)
next_button.grid(row=4, column=1, padx=15, pady=15)

repeat_button = ttk.Button(root, text="Repeat", command=toggle_repeat, width=button_width)
repeat_button.grid(row=5, column=0, padx=15, pady=15)

shuffle_button = ttk.Button(root, text="Shuffle", command=toggle_shuffle, width=button_width)
shuffle_button.grid(row=5, column=1, padx=15, pady=15)

# Additional buttons
prev_next_frame = ttk.Frame(root)
prev_next_frame.grid(row=6, columnspan=3, padx=15, pady=15)

previous_button = ttk.Button(prev_next_frame, text="Previous Track", command=previous_track, width=button_width)
previous_button.grid(row=0, column=0, padx=15, pady=15)

next_button = ttk.Button(prev_next_frame, text="Next Track", command=next_track, width=button_width)
next_button.grid(row=0, column=1, padx=15, pady=15)

# Labels
current_song_label = ttk.Label(root, text="Current Song: None")
current_song_label.grid(row=7, columnspan=3, padx=15, pady=15)

result_label = ttk.Label(root, text="")
result_label.grid(row=8, columnspan=3, padx=15, pady=15)

# Event handler for music end
pygame.mixer.music.set_endevent(pygame.USEREVENT)
root.bind(pygame.USEREVENT, lambda event: music_end_event())

# Set window size
root.geometry("1600x720")

# Run the application
root.mainloop()

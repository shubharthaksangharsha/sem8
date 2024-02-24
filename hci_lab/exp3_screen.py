import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Import PIL modules for handling images

def start_timer():
    global countdown, loop_flag
    countdown = 2 # Countdown time in seconds
    loop_flag = loop_var.get()
    mail_sent_label.config(text="")  # Reset the text label for mail sent
    update_timer()

def update_timer():
    global countdown, loop_flag
    if countdown > 0:
        timer_label.config(text=f"Time left: {countdown} seconds")
        countdown -= 1
        root.after(1000, update_timer)  # Update timer after 1 second (1000 milliseconds)
    elif loop_flag:
        countdown = 60
        update_timer()
    else:
        timer_label.config(text="Time's up!")
        if send_mail_var.get():
            send_mail()
        else:
            remind_medication()

def remind_medication():
    patient_id = patient_id_entry.get()
    disease_name = disease_name_entry.get()
    
    if patient_id and disease_name:
        # Here you can implement the logic to fetch medication reminders
        # For simplicity, I'll just display a message box with dummy data
        message = f"Patient ID: {patient_id}\nDisease: {disease_name}\nReminder: Take medication X, Y, Z."
        messagebox.showinfo("Medication Reminder", message, icon='warning')
    else:
        messagebox.showwarning("Missing Information", "Please enter Patient ID and Disease Name.")

def send_mail():
    patient_id = patient_id_entry.get()
    disease_name = disease_name_entry.get()
    # Placeholder function for sending mail
    if patient_id and disease_name:
        mail_sent_label.config(text="Mail sent successfully!")
        messagebox.showinfo("Medication Reminder", f"Patient ID: {patient_id}\nDisease: {disease_name}\nReminder: Take medication X, Y, Z.")
    else:
        messagebox.showwarning("Missing Information", "Please enter Patient ID and Disease Name.")

# Create the main window
root = tk.Toplevel()
root.title("Patient ID Reminder App")
root.geometry('640x480')

# Load and resize background image
bg_image = Image.open("background.png")  # Replace "background_image.jpg" with your image file
bg_image = bg_image.resize((root.winfo_width(), root.winfo_height()), Image.LANCZOS)  # Resize image to fit window

# Convert image to Tkinter format
background_image = ImageTk.PhotoImage(bg_image)

# Create a label with the background image and place it in the window
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Add widgets with transparent background
tk.Label(root, text="Patient ID:", font=("Helvetica", 16, 'bold')).grid(row=0, column=0, padx=10, pady=(20, 5))
patient_id_entry = tk.Entry(root, font=("Helvetica", 16, 'bold'), bg="white")  # Set entry background to white
patient_id_entry.grid(row=0, column=1, padx=10, pady=(20, 5))

tk.Label(root, text="Disease Name:", font=("Helvetica", 16, 'bold')).grid(row=1, column=0, padx=10, pady=5)
disease_name_entry = tk.Entry(root, font=("Helvetica", 16, 'bold'), bg="white")  # Set entry background to white
disease_name_entry.grid(row=1, column=1, padx=10, pady=5)

loop_var = tk.BooleanVar()  # Define loop_var
send_mail_var = tk.BooleanVar()

send_mail_checkbox = tk.Checkbutton(root, text="Send Mail", font=("Helvetica", 16, 'bold'), variable=send_mail_var)  # Set checkbox background to transparent
send_mail_checkbox.grid(row=2, column=0, padx=10, pady=5)

remind_button = tk.Button(root, text="Remind Me", font=("Helvetica", 16, 'bold'), command=start_timer, bg="#4caf50", fg="white")
remind_button.grid(row=2, column=1, padx=10, pady=5)

timer_label = tk.Label(root, text="", font=("Helvetica", 16, 'bold'))  # Set label background to transparent
timer_label.grid(row=3, column=0, columnspan=2, pady=10)

mail_sent_label = tk.Label(root, text="", font=("Helvetica", 16, 'bold'))  # Set label background to transparent
mail_sent_label.grid(row=4, column=0, columnspan=2, pady=10)

# Start the GUI event loop
root.mainloop()

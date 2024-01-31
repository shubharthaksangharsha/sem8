import tkinter as tk
from tkinter import simpledialog  # Import simpledialog explicitly


class HomeApplianceInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Home Appliance by Shubharthak")

        # Set a consistent color scheme
        # button_bg = '#4CAF50'  # Green
        button_bg = '#ADD8E6'  # Light Blue

        button_fg = 'black'

        # Initialize buttons with larger size and font size
        button_width = 20
        button_height = 5
        button_font = ('Arial', 18, 'bold')
        button_border_width = 3

        # Create buttons with consistent styling
        self.light_button = self.create_button(root, "Lights", self.toggle_lights, button_width, button_height, button_font, button_border_width, button_bg, button_fg)
        self.fan_button = self.create_button(root, "Fan", self.toggle_fan, button_width, button_height, button_font, button_border_width, button_bg, button_fg)
        self.ac_button = self.create_button(root, "AC", self.toggle_ac, button_width, button_height, button_font, button_border_width, button_bg, button_fg)
        self.geyser_button = self.create_button(root, "Geyser", self.toggle_geyser, button_width, button_height, button_font, button_border_width, button_bg, button_fg)
        self.door_button = self.create_button(root, "Door", self.toggle_door, button_width, button_height, button_font, button_border_width, button_bg, button_fg)
        self.microwave_button = self.create_button(root, "Microwave", self.toggle_microwave, button_width, button_height, button_font, button_border_width, button_bg, button_fg)

        # Set initial button states
        self.set_initial_button_states()

        # Grid layout for buttons
        self.light_button.grid(row=0, column=0, padx=10, pady=10)
        self.fan_button.grid(row=0, column=1, padx=10, pady=10)
        self.ac_button.grid(row=1, column=0, padx=10, pady=10)
        self.geyser_button.grid(row=1, column=1, padx=10, pady=10)
        self.door_button.grid(row=2, column=0, padx=10, pady=10)
        self.microwave_button.grid(row=2, column=1, padx=10, pady=10)

        # Feedback label
        self.feedback_label = tk.Label(root, text="", font=('Arial', 22, 'bold'), fg='red')
        self.feedback_label.grid(row=3, columnspan=2, pady=15)

    def create_button(self, parent, text, command, width, height, font, border_width, bg, fg):
        return tk.Button(parent, text=text, command=command, width=width, height=height, font=font, bd=border_width, bg=bg, fg=fg)

    def set_initial_button_states(self):
        # Set initial button states
        self.light_button['text'] = "Lights OFF"
        self.fan_button['text'] = "Fan OFF"
        self.ac_button['text'] = "AC OFF"
        self.geyser_button['text'] = "Geyser OFF"
        self.door_button['text'] = "Door Closed"
        self.microwave_button['text'] = "Microwave OFF"

    def update_feedback_label(self, message):
        self.feedback_label.config(text=message)

    def toggle_lights(self):
        if self.light_button['text'] == "Lights OFF":
            self.light_button['text'] = "Lights On"
            self.update_feedback_label("Lights turned ON")
        else:
            self.light_button['text'] = "Lights OFF"
            self.update_feedback_label("Lights turned OFF")

    def toggle_fan(self):
        if self.fan_button['text'] == "Fan OFF":
            self.fan_button['text'] = "Fan On"
            self.update_feedback_label("Fan turned ON")
        else:
            self.fan_button['text'] = "Fan OFF"
            self.update_feedback_label("Fan turned OFF")

    def toggle_ac(self):
        if self.ac_button['text'] == "AC OFF":
            self.ac_button['text'] = "AC On"
            self.update_feedback_label("AC turned ON")
        else:
            self.ac_button['text'] = "AC OFF"
            self.update_feedback_label("AC turned OFF")

    def toggle_geyser(self):
        if self.geyser_button['text'] == "Geyser OFF":
            self.geyser_button['text'] = "Geyser On"
            self.update_feedback_label("Geyser turned ON")
        else:
            self.geyser_button['text'] = "Geyser OFF"
            self.update_feedback_label("Geyser turned OFF")

    def toggle_door(self):
        if self.door_button['text'] == "Door Closed":
            self.door_button['text'] = "Door Opened"
            self.update_feedback_label("Door turned opened!")
        else:
            self.door_button['text'] = "Door Closed"
            self.update_feedback_label("Door turned closed!")

    def toggle_microwave(self):
        if self.microwave_button['text'] == "Microwave OFF":
            self.microwave_button['text'] = "Microwave ON"
            self.update_feedback_label("Microwave turned ON!")
        else:
            self.microwave_button['text'] = "Microwave OFF"
            self.update_feedback_label("Microwave turned OFF!")


if __name__ == "__main__":
    root = tk.Tk()
    app = HomeApplianceInterface(root)

    root.geometry("800x720")

    root.mainloop()

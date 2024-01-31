import tkinter as tk

class HomeApplianceInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Tinker Home Appliance Interface by Shubharthak")

        # Entry widget for user input
        self.user_input = tk.Entry(root, width=20, font=('Arial', 14))
        self.user_input.grid(row=0, column=0, padx=10, pady=10)

        # Initialize buttons with larger size and font size
        button_width = 20
        button_height = 10
        button_font = ('Arial', 18)
        # Submit button
        self.submit_button = tk.Button(root, text="Submit", command=self.process_input, width=button_width, height=button_height, font=('Arial', 16))
        self.submit_button.grid(row=0, column=1, padx=10, pady=10)

        
        

        self.light_button = tk.Button(root, text="Light On", command=self.lights_on, width=button_width, height=button_height, font=button_font)
        self.fan_button = tk.Button(root, text="Fan On", command=self.fan_on, width=button_width, height=button_height, font=button_font)
        self.door_button = tk.Button(root, text="Lights OFF", command=self.lights_off, width=button_width, height=button_height, font=button_font)
        self.ac_button = tk.Button(root, text="Fan OFF", command=self.fan_off, width=button_width, height=button_height, font=button_font)
        self.custom_button1 = tk.Button(root, text="AC On", command=self.ac_on, width=button_width, height=button_height, font=button_font)
        self.custom_button2 = tk.Button(root, text="AC Off", command=self.ac_off, width=button_width, height=button_height, font=button_font)

        # Grid layout for buttons
        self.light_button.grid(row=1, column=0, padx=10, pady=10)
        self.fan_button.grid(row=1, column=1, padx=10, pady=10)
        self.door_button.grid(row=0, column=2, padx=10, pady=10)
        self.ac_button.grid(row=1, column=2, padx=10, pady=10)
        self.custom_button1.grid(row=0, column=3, padx=10, pady=10)
        self.custom_button2.grid(row=1, column=3, padx=10, pady=10)

    def process_input(self):
        user_value = self.user_input.get()
        # Check user input and perform corresponding action
        if user_value == '0':
            self.lights_on()

        if user_value == '1':
            self.lights_off()

        if user_value == '2':
            self.fan_on()

        if user_value == '3':
            self.fan_off()
        
        if user_value == '4':
            self.ac_on()

        if user_value == '5':
            self.ac_off()


    def lights_on(self):
        print("Lights On!")
    def lights_off(self):
        print("Lights OFF!")

    def fan_on(self):
        print("Fan On!")

    def fan_off(self):
        print("Fan OFF!")

    def ac_on(self):
        print("AC On!")
    
    def ac_off(self):
        print("AC OFF!")

    
if __name__ == "__main__":
    root = tk.Tk()
    app = HomeApplianceInterface(root)

    root.geometry("1280x720")

    root.mainloop()

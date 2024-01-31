import tkinter as tk
from tkinter import messagebox, simpledialog
import random

class Child:
    def __init__(self, name):
        self.name = name
        self.preferences = []
        self.interests = []

    def add_preference(self, preference):
        self.preferences.append(preference)

    def add_interest(self, interest):
        self.interests.append(interest)

class MathAppGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Math App for Children")
        
        self.children = []
        self.current_child = None
        
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Enter Child's Name:",font=('Arial', 22, 'bold'))
        self.label.pack()

        self.entry_name = tk.Entry(self.master, borderwidth=2, width=30, font=('Arial', 18))
        self.entry_name.pack()

        self.button_register = tk.Button(self.master, text="Register Child", command=self.register_child,font=('Arial', 22, 'bold'))
        self.button_register.pack()

        self.button_teach_math = tk.Button(self.master, text="Teach Math", state=tk.DISABLED, command=self.teach_math,font=('Arial', 22, 'bold'))
        self.button_teach_math.pack()

        self.button_analyze_behavior = tk.Button(self.master, text="Analyze Behavior", state=tk.DISABLED, command=self.analyze_behavior,font=('Arial', 22, 'bold'))
        self.button_analyze_behavior.pack()

    def register_child(self):
        name = self.entry_name.get()
        if name:
            child = Child(name)
            self.children.append(child)
            self.current_child = child
            self.button_teach_math["state"] = tk.NORMAL
            self.button_analyze_behavior["state"] = tk.NORMAL
            messagebox.showinfo("Success", f"Child {name} registered successfully.")
        else:
            messagebox.showwarning("Warning", "Please enter a valid name.")

    def teach_math(self):
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        answer = num1 + num2

        response = simpledialog.askinteger("Math Question", f"What is {num1} + {num2}?")

        if response == answer:
            messagebox.showinfo("Correct", "Well done! That's correct.")
        else:
            messagebox.showinfo("Incorrect", f"Oops! The correct answer is {answer}.")

    def analyze_behavior(self):
        preference = simpledialog.askstring("Preference", "Enter child's preference:")
        interest = simpledialog.askstring("Interest", "Enter child's interest:")

        if preference:
            self.current_child.add_preference(preference)

        if interest:
            self.current_child.add_interest(interest)

        messagebox.showinfo("Analysis", "Behavior analysis complete.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MathAppGUI(root)
    root.geometry('800x720')
    root.mainloop()

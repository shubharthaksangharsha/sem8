import tkinter as tk
from tkinter import ttk, Menu, messagebox, simpledialog
from PIL import Image, ImageTk
from tkinter import font as tkFont  



class StreetDesignApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Street Design Learning App")
        self.root.geometry("1280x720")
        
        self.create_styles()
        self.create_menu()
        self.create_widgets()

    def create_styles(self):
        self.style = ttk.Style()
        self.style.configure("Custom.TNotebook", font=("Helvetica", 30, "bold"))

    def create_menu(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Exit", command=self.root.quit)

    def create_widgets(self):
        self.notebook = ttk.Notebook(self.root, style="Custom.TNotebook")
        self.notebook.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

        topics = [
            {"title": "Pedestrian Zones", "content": "Principles of designing pedestrian-friendly areas.", "image": "pedestrian_2.png"},
            {"title": "Cycling Lanes", "content": "Importance of dedicated cycling lanes in street design.", "image": "cycling.png"},
            {"title": "Public Spaces", "content": "Designing attractive and functional public spaces.", "image": "public_spaces_areas.png"}
        ]
        for topic in topics:
            self.create_tab(topic)

    def create_tab(self, topic_info):
        helv36 = tkFont.Font(family='Helvetica', size=12, weight='bold')
        tab = ttk.Frame(self.notebook)
        self.notebook.add(tab, text=topic_info["title"])

        content_label = tk.Label(tab, text=topic_info["content"], font=("Helvetica", 26, "bold"), wraplength=800, justify=tk.LEFT, padx=20, pady=20)
        content_label.pack(fill=tk.BOTH, expand=True)

        img = Image.open(topic_info["image"])
        img = img.resize((400, 400), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(img)
        image_label = tk.Label(tab, image=photo)
        image_label.image = photo
        image_label.pack(pady=20)

        btn_show_image = tk.Button(tab, text="Show Image", command=lambda: self.show_image(photo), font=helv36)
        
        
        btn_show_image.pack(pady=10)

        btn_feedback = tk.Button(tab, text="Provide Feedback", command=lambda: self.show_feedback_dialog(topic_info["title"]), font=helv36)
        btn_feedback.pack(pady=5)

    def show_image(self, photo):
        img_window = tk.Toplevel(self.root)
        img_window.title("Street Design Image")
        image_label = tk.Label(img_window, image=photo)
        image_label.pack(pady=20)

    def show_feedback_dialog(self, topic):
        helv36 = tkFont.Font(family='Helvetica', size=12, weight='bold')

        feedback = simpledialog.askstring("Feedback", f"Provide feedback for '{topic}':")
        if feedback:
            messagebox.showinfo("Feedback Submitted", "Thank you for providing feedback!")

def main():
    root = tk.Tk()
    app = StreetDesignApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

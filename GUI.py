import customtkinter as tk

class GUI(tk.CTk):
    def __init__(self):
        super().__init__()
        tk.set_appearance_mode("dark")
        tk.set_default_color_theme('dark-blue')

        self.geometry("400x500")
        self.title("Faktura sammanställare")

    
    def on_click(self):
        print("Button clicked")
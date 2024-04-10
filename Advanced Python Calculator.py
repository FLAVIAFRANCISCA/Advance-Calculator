import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog, colorchooser, font
from math import sqrt, pow, sin, cos, tan, pi
from datetime import datetime

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("310x400")
        
        self.history = []
        self.font = font.Font(family="Arial", size=14, weight="normal")
        
        # Default theme
        self.theme_color = "#f0f0f0"
        self.text_color = "#000000"
        
        self.create_widgets()
        self.apply_theme()
        
    def create_widgets(self):
        self.display = tk.Entry(self.root, font=self.font, width=15, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        
        # Button Layout
        btn_texts = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('0', 4, 1),
            ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3),
            ('sqrt', 5, 0), ('pow', 5, 1), ('sin', 5, 2), ('cos', 5, 3),
            ('tan', 6, 0), ('pi', 6, 1), ('C', 4, 0), ('=', 4, 2)
        ]
        
        for (text, row, col) in btn_texts:
            self.add_button(text, row, col)
    
    def add_button(self, text, row, col):
        btn = tk.Button(self.root, text=text, font=self.font, width=5, height=2,
                        command=lambda: self.on_click(text))
        btn.grid(row=row, column=col, sticky="nsew")
        btn.config(bg=self.theme_color, fg=self.text_color)
    
    def on_click(self, char):
        if char == '=':
            try:
                result = str(eval(self.display.get()))
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.history.append(f"{timestamp}: {self.display.get()} = {result}")
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
        elif char == 'C':
            self.display.delete(0, tk.END)
        elif char in ['sqrt', 'pow', 'sin', 'cos', 'tan']:
            self.perform_advanced_operations(char)
        else:
            self.display.insert(tk.END, char)
    
    def perform_advanced_operations(self, operation):
        value = self.display.get()
        self.display.delete(0, tk.END)
        try:
            if operation == 'sqrt':
                result = sqrt(float(value))
            elif operation == 'pow':
                result = pow(float(value), 2)
            elif operation == 'sin':
                result = sin(float(value) * pi / 180)
            elif operation == 'cos':
                result = cos(float(value) * pi / 180)
            elif operation == 'tan':
                result = tan(float(value) * pi / 180)
            self.display.insert(0, str(result))
        except Exception as e:
            self.display.insert(0, "Error")
    
    def show_history(self):
        history_window = tk.Toplevel(self.root)
        history_window.title("Calculation History")
        history_list = tk.Listbox(history_window, font=self.font)
        history_list.pack(expand=True, fill="both")
        for item in self.history:
            history_list.insert(tk.END, item)
    
    def change_theme(self, theme):
        if theme == "dark":
            self.theme_color = "#333333"
            self.text_color = "#ffffff"
        else:  # light theme
            self.theme_color = "#f0f0f0"
            self.text_color = "#000000"
        self.apply_theme()
    
    def apply_theme(self):
        self.root.config(bg=self.theme_color)
        self.display.config(bg="white", fg="black")
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(bg=self.theme_color, fg=self.text_color)
    
    def customize_font(self):
        new_size = simpledialog.askinteger("Font Size", "Enter new font size:", initialvalue=self.font['size'])
        if new_size:
            self.font.configure(size=new_size)
            self.display.config(font=self.font)
            for widget in self.root.winfo_children():
                if isinstance(widget, tk.Button):
                    widget.config(font=self.font)
    def customize_color(self):
        color = colorchooser.askcolor(title="Choose button color")[1]
        if color:
            for widget in self.root.winfo_children():
                if isinstance(widget, tk.Button):
                    widget.config(bg=color)

def main():
    root = tk.Tk()
    app = Calculator(root)
    menu = tk.Menu(root)
    root.config(menu=menu)
    
    # History Menu
    history_menu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="History", menu=history_menu)
    history_menu.add_command(label="Show History", command=app.show_history)
    
    # Customization Menu
    customization_menu = tk.Menu(menu, tearoff=0)
    menu.add_cascade(label="Customize", menu=customization_menu)
    customization_menu.add_command(label="Dark Theme", command=lambda: app.change_theme("dark"))
    customization_menu.add_command(label="Light Theme", command=lambda: app.change_theme("light"))
    customization_menu.add_command(label="Customize Font", command=app.customize_font)
    customization_menu.add_command(label="Customize Button Color", command=app.customize_color)
    
    root.mainloop()

if __name__ == "__main__":
    main()

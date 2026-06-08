import tkinter as tk
import customtkinter as ctk
import math

# Set up the modern visual theme
ctk.set_appearance_mode("dark")  # Modes: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

# Function to update the input field when a button is clicked
def press(key):
    entry.insert(tk.END, key)

# Function to evaluate the expression entered by the user
def calculate():
    try:
        # Evaluate expression smoothly
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to clear the input field
def clear():
    entry.delete(0, tk.END)

# Function to handle trigonometric operations
def trig_operation(func):
    try:
        value = float(entry.get())
        if func == 'sin':
            result = math.sin(math.radians(value))
        elif func == 'cos':
            result = math.cos(math.radians(value))
        elif func == 'tan':
            result = math.tan(math.radians(value))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function for factorial operation
def factorial():
    try:
        value = int(entry.get())
        result = math.factorial(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to calculate percentage
def percentage():
    try:
        value = float(entry.get())
        result = value / 100
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Initialize CustomTkinter window
root = ctk.CTk()
root.title("Scientific Calculator")
root.geometry("340x540")
root.resizable(False, False)
root.configure(fg_color="#17171C")  # Deep sleek dark background

# Modern, borderless input field with internal padding
entry = ctk.CTkEntry(
    root, 
    width=310, 
    height=70, 
    font=("Segoe UI", 26, "bold"), 
    justify="right",
    fg_color="#2A2A2F",
    text_color="#FFFFFF",
    border_width=0,
    corner_radius=12
)
entry.grid(row=0, column=0, columnspan=4, padx=15, pady=(25, 15))

# High-end color palette configurations
COLOR_DIGIT = "#2A2A2F"      # Dark slate for numbers
COLOR_HOVER_DIGIT = "#3A3A40"
COLOR_OP = "#3D3D45"         # Lighter grey for operators/functions
COLOR_HOVER_OP = "#4E4E57"
COLOR_ACTION = "#FF9F0A"     # Vibrant orange for equals and clear
COLOR_HOVER_ACTION = "#CC7F08"

# Button layout coordinates (4 columns layout)
buttons = [
    ('sin', 1, 0), ('cos', 1, 1), ('tan', 1, 2), ('C', 1, 3),
    ('π', 2, 0),   ('e', 2, 1),   ('!', 2, 2),   ('√', 2, 3),
    ('%', 3, 0),   ('(', 3, 1),   (')', 3, 2),   ('^', 3, 3),
    ('7', 4, 0),   ('8', 4, 1),   ('9', 4, 2),   ('/', 4, 3),
    ('4', 5, 0),   ('5', 5, 1),   ('6', 5, 2),   ('*', 5, 3),
    ('1', 6, 0),   ('2', 6, 1),   ('3', 6, 2),   ('-', 6, 3),
    ('.', 7, 0),   ('0', 7, 1),   ('=', 7, 2),   ('+', 7, 3),
]

# Generate and style buttons dynamically
for (text, row, col) in buttons:
    # Default parameters for a premium layout
    btn_text = text
    bg_color = COLOR_OP
    hover_color = COLOR_HOVER_OP
    txt_color = "#FFFFFF"
    cmd = lambda t=text: press(t)
    
    # Contextual adjustments for specific keys
    if text == "=":
        bg_color = COLOR_ACTION
        hover_color = COLOR_HOVER_ACTION
        cmd = calculate
    elif text == "C":
        bg_color = "#E04A3A" # Distinct premium red for clear
        hover_color = "#B83B2E"
        cmd = clear
    elif text in ['sin', 'cos', 'tan']:
        cmd = lambda t=text: trig_operation(t)
    elif text == "√":
        cmd = lambda: press('math.sqrt(')
    elif text == "π":
        cmd = lambda: press(str(math.pi))
    elif text == "e":
        cmd = lambda: press(str(math.e))
    elif text == "^":
        btn_text = "xʸ" # Sleeker math label
        cmd = lambda: press('**')
    elif text == "%":
        cmd = percentage
    elif text == "!":
        cmd = factorial
    elif text in '0123456789.':
        bg_color = COLOR_DIGIT
        hover_color = COLOR_HOVER_DIGIT
        
    # Create the customized smooth button
    btn = ctk.CTkButton(
        root, 
        text=btn_text, 
        width=68, 
        height=50, 
        font=("Segoe UI", 16, "normal" if len(text) > 1 else "bold"), # Fixed "medium" bug here
        fg_color=bg_color,
        hover_color=hover_color,
        text_color=txt_color,
        corner_radius=25, # Fully rounded fluid look
        command=cmd
    )
    btn.grid(row=row, column=col, padx=6, pady=6)

# Start the upgraded fluid event loop
root.mainloop()
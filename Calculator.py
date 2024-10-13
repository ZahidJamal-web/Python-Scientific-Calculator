import tkinter as tk
import math

# Function to update the input field when a button is clicked
def press(key):
    entry.insert(tk.END, key)

# Function to evaluate the expression entered by the user
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
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
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function for factorial operation
def factorial():
    try:
        value = int(entry.get())
        result = math.factorial(value)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to calculate percentage
def percentage():
    try:
        value = float(entry.get())
        result = value /100
        entry.delete(0,tk.END)
        entry.insert(tk.END,str(result))
    except Exception as e:
        entry.delete(0,tk.END)
        entry.insert(tk.END,"Error")

# Initialize tkinter window
root = tk.Tk()
root.title("Scientific Calculator")
root.config(bg="lightgrey")

# Input field
entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=6)

# Button layout
buttons = [
    ('sin', 1, 0), ('cos', 1, 1), ('tan', 1, 2), ('√', 1, 3),
    ('π', 2, 0), ('e', 2, 1), ('!', 2, 2), ('^', 2, 3),
    ('%', 3, 0), ('(', 3, 1), (')', 3, 2), ('/', 3, 3),
    ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('*', 4, 3),
    ('4', 5, 0), ('5', 5, 1), ('6', 5, 2), ('+', 5, 3),
    ('1', 6, 0), ('2', 6, 1), ('3', 6, 2), ('-', 6, 3),
    ('.', 7, 0), ('0', 7, 1), ('C', 7, 2), ('=', 7, 3),
]

# Add buttons to the window
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=5, height=2, bg="orange", fg="white", command=calculate)
    elif text == "C":
        btn = tk.Button(root, text=text, width=5, height=2, bg="orange", fg="white", command=clear)
    elif text == "sin":
        btn = tk.Button(root, text=text, width=5, height=2, bg="blue", fg="white", command=lambda: trig_operation('sin'))
    elif text == "cos":
        btn = tk.Button(root, text=text, width=5, height=2, bg="blue", fg="white", command=lambda: trig_operation('cos'))
    elif text == "tan":
        btn = tk.Button(root, text=text, width=5, height=2, bg="blue", fg="white", command=lambda: trig_operation('tan'))
    elif text == "√":
        btn = tk.Button(root, text=text, width=5, height=2, bg="blue", fg="white", command=lambda: press('math.sqrt('))
    elif text == "π":
        btn = tk.Button(root, text=text, width=5, height=2, bg="blue", fg="white", command=lambda: press(str(math.pi)))
    elif text == "e":
        btn = tk.Button(root, text=text, width=5, height=2, bg="blue", fg="white", command=lambda: press(str(math.e)))
    elif text == "^":
        btn =tk.Button(root,text=text, width=5, height=2, bg="blue", fg="white", command=lambda: press('**'))
    elif text == "%":
        btn = tk.Button(root,text=text, width=5, height=2, bg="blue", fg="white", command=percentage)
    elif text == "!":
        btn = tk.Button(root, text=text, width=5, height=2, bg="blue", fg="white", command=factorial)
    elif text in '0123456789':
        btn = tk.Button(root, text=text, width=5, height=2, bg="white", fg="black", command=lambda t=text: press(t))
    else:
        btn = tk.Button(root, text=text, width=5, height=2, bg="orange", fg="white", command=lambda t=text: press(t))
    btn.grid(row=row, column=col)

# Run the tkinter loop
root.mainloop()

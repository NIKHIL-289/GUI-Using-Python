import tkinter as tk
from tkinter import messagebox

# Initialize the main window
window = tk.Tk()
window.title("Simple Tkinter Widgets")
window.geometry("400x300")  # Set window size

# Function triggered by button click
def button_clicked():
    username = username_entry.get()
    messagebox.showinfo("Hello!", f"Welcome, {username}!")

# Label
label = tk.Label(window, text="Enter your name:", font=("Arial", 14))
label.pack(pady=10)  # Use pack layout manager to position the widget

# Entry (input field)
username_entry = tk.Entry(window, font=("Arial", 14))
username_entry.pack(pady=5)

# Button
button = tk.Button(window, text="Submit", font=("Arial", 14), command=button_clicked)
button.pack(pady=20)

# Radio Buttons
radio_var = tk.StringVar(value="Option 1")  # Variable to store selected option
tk.Label(window, text="Choose Your Gender:", font=("Arial", 14)).pack(pady=10)

radio1 = tk.Radiobutton(window, text="Male", variable=radio_var, value="Option 1", font=("Arial", 12))
radio1.pack()

radio2 = tk.Radiobutton(window, text="Female", variable=radio_var, value="Option 2", font=("Arial", 12))
radio2.pack()

# Run the main event loop
window.mainloop()

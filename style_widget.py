import tkinter as tk
from tkinter import messagebox

# Initialize the main window
window = tk.Tk()
window.title("Styled Tkinter Widgets")
window.geometry("400x400")  # Set window size
window.configure(bg="#f0f8ff")  # Set background color for the window (AliceBlue)

# Function triggered by button click
def button_clicked():
    username = username_entry.get()
    if username.strip():
        messagebox.showinfo("Hello!", f"Welcome, {username}!")
    else:
        messagebox.showerror("Error", "Name cannot be empty!")

# Title Label
title_label = tk.Label(
    window, text="Welcome to Styled Tkinter App", font=("Arial", 16, "bold"),
    bg="#4682b4", fg="white", padx=10, pady=10  # Background and foreground colors
)
title_label.pack(pady=10, fill="x")  # Stretch across the window width

# Name Label
name_label = tk.Label(
    window, text="Enter your name:", font=("Arial", 12), bg="#f0f8ff", fg="black"
)
name_label.pack(pady=5)

# Entry (input field)
username_entry = tk.Entry(
    window, font=("Arial", 14), bg="white", fg="black", highlightbackground="#4682b4",
    highlightthickness=2, relief="solid"  # Styling the border
)
username_entry.pack(pady=5)

# Submit Button
submit_button = tk.Button(
    window, text="Submit", font=("Arial", 14, "bold"), bg="#32cd32", fg="white",
    activebackground="#228b22", activeforeground="white", padx=10, pady=5,
    command=button_clicked  # Function to execute on click
)
submit_button.pack(pady=20)

# Radio Buttons
radio_var = tk.StringVar(value="Option 1")  # Variable to store selected option

# Radio Buttons Label
radio_label = tk.Label(
    window, text="Choose Your Gender:", font=("Arial", 12), bg="#f0f8ff", fg="black"
)
radio_label.pack(pady=5)

# Radio Button 1
radio1 = tk.Radiobutton(
    window, text="Male", variable=radio_var, value="Option 1",
    font=("Arial", 12), bg="#f0f8ff", fg="black", activebackground="#f0f8ff",
    activeforeground="blue", selectcolor="lightgray", padx=10, pady=5
)
radio1.pack()

# Radio Button 2
radio2 = tk.Radiobutton(
    window, text="Female", variable=radio_var, value="Option 2",
    font=("Arial", 12), bg="#f0f8ff", fg="black", activebackground="#f0f8ff",
    activeforeground="blue", selectcolor="lightgray", padx=10, pady=5
)
radio2.pack()

# Footer Label
footer_label = tk.Label(
    window, text="Thank you for using the app!", font=("Arial", 10, "italic"),
    bg="#4682b4", fg="white", pady=5
)
footer_label.pack(side="bottom", fill="x")  # Positioned at the bottom

# Run the main event loop
window.mainloop()

#1. Importing Libraries
import tkinter
from tkinter import StringVar, Label, Button, Radiobutton, PhotoImage, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

#2. Initialize the main window
window = tkinter.Tk()
window.title('Login & Test')
window.geometry('1000x500')
window.maxsize(1000,500)
window.configure(bg="white")

#3. Test Data
questions = [
    ("WHAT IS THE PURPOSE OF THE 'window.mainloop()' IN THIS CODE?", 
     ["Make window dance", "Keep program running", "Ends program", "To confuse programmers"], 
     "Keeps program running"),
     
    ("WHY DOES THE FUNCTION 'validate_login()' CHECK THE USERNAME AND PASSWORD?", 
     ["For fun", "To annoy the user", "For security reasons", "Because the code says so"], 
     "For security reasons"),
     
    ("WHAT DOES THE FUNCTION 'show_question()' DO IN THIS CODE?", 
     ["Hides the questions", "Shows them one by one", "Sends them to NASA", "Writes a novel"], 
     "Shows them one by one"),
     
    ("WHAT WOULD HAPPEN IF 'next_question()' FORGOT TO INCREMENT 'current_question'?", 
     ["The quiz would be infinite", "The app would crash", "The user would win instantly", "The window would explode"], 
     "The quiz would be infinite"),
     
    ("WHAT IS THE NAME OF THE LIBRARY USED FOR DISPLAYING THE PIE CHART IN RESULTS?", 
     ["Pillow", "Matplotlib", "NumPy", "Pandas"], 
     "Matplotlib"),
]

current_question = 0
user_answers = []
selected_answer = StringVar()

#4. Functions for Quiz Functionality
def show_question():
    global current_question
    question_label.config(text=questions[current_question][0])
    selected_answer.set("")  # Clear previous selection

    # Update options
    options = questions[current_question][1]
    for i in range(4):
        options_buttons[i].config(text=f"{i + 1}. {options[i]}", value=options[i], state="normal")

def next_question():
    global current_question
    user_answers.append(selected_answer.get())  # Store the answer
    current_question += 1

    if current_question < len(questions):
        show_question()
    else:
        finish_test()

def finish_test():
    question_label.config(text="TEST SUBMITTED!", font=("Arial", 20))
    for btn in options_buttons:
        btn.config(state="disabled")
    next_button.grid_forget()
    submit_button.grid(row=6, column=0, columnspan=2, pady=20)

def view_results():

    window.geometry('650x850')
    window.maxsize(650,850)

    correct = sum(
        1 for i, (_, _, correct_answer) in enumerate(questions)
        if user_answers[i] == correct_answer
    )
    incorrect = len(questions) - correct

    labels = ["Correct", "Incorrect"]
    sizes = [correct, incorrect]
    colors = ["lightgreen", "tomato"]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90, colors=colors)
    ax.axis("equal")

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().grid(row=7, column=0, columnspan=3)

def validate_login():
    username = username_entry.get()
    password = password_entry.get()
    if username == "admin" and password == "password123":
        messagebox.showinfo("Login", "Login Successful!")
        clear_login_screen()
        start_test()
    else:
        messagebox.showerror("Login", "Invalid credentials.")

def clear_login_screen():
    for widget in window.winfo_children():
        widget.destroy()

def start_test():
    global question_label, options_buttons, next_button, submit_button

    question_label = Label(window, text="", font=("Arial", 30), bg="white", fg="black", wraplength=700)
    question_label.grid(row=0, column=0, columnspan=3, pady=20)

    window.geometry('650x300')
    window.maxsize(650,300)

    # Create 4 buttons for the options
    options_buttons = []
    for i in range(4):
        btn = Radiobutton(window, text="", variable=selected_answer, font=("Arial", 24), bg="white", fg="black", value="", indicatoron=0, width=20, anchor="w")
        options_buttons.append(btn)

    # Arrange the buttons in a grid
    options_buttons[0].grid(row=1, column=0, pady=10, padx=20)  # Option 1
    options_buttons[1].grid(row=2, column=0, pady=10, padx=20)  # Option 2
    options_buttons[2].grid(row=1, column=1, pady=10, padx=20)  # Option 3
    options_buttons[3].grid(row=2, column=1, pady=10, padx=20)  # Option 4

    next_button = Button(window, text="Next", command=next_question, bg="lightblue", font=("Arial", 20))
    next_button.grid(row=4, column=0, columnspan=2, pady=20)

    submit_button = Button(window, text="View Results", command=view_results, bg="green", font=("Arial", 30))

    show_question()

#5. Login UI
image = PhotoImage(file="/Users/nikhiltripathi/Downloads/login.png")  # Update to the correct path
image_label = Label(window, image=image, bg="white")
image_label.grid(row=0, column=0, rowspan=5, padx=10, pady=10)

Label(window, text="Login", font=("Arial", 24), bg="white").grid(row=0, column=1, columnspan=2, pady=20)
Label(window, text="Username:", bg="white", font=("Arial", 14)).grid(row=1, column=1, sticky="e", pady=5, padx=5)
username_entry = tkinter.Entry(window, bg="white", fg="black", font=("Arial", 14))
username_entry.grid(row=1, column=2, pady=5, padx=5)

Label(window, text="Password:", bg="white", font=("Arial", 14)).grid(row=2, column=1, sticky="e", pady=5, padx=5)
password_entry = tkinter.Entry(window, show="*", bg="white", fg="black", font=("Arial", 14))
password_entry.grid(row=2, column=2, pady=5, padx=5)

login_button = Button(window, text="Login", command=validate_login, bg="lightblue", font=("Arial", 14))
login_button.grid(row=4, column=1, columnspan=2, pady=20)

#6. Main Event Loop
window.mainloop()

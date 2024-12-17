import tkinter as tk

# Initialize the main window
window = tk.Tk()
window.title("Canvas Widget Example")
window.geometry("500x500")  # Set window size
window.configure(bg="white")  # Background color of the window

# Create a Canvas widget
canvas = tk.Canvas(window, width=400, height=400, bg="#f0f8ff", highlightthickness=2, highlightbackground="#4682b4")
canvas.pack(pady=20)

# Draw Rectangle
rect_x1, rect_y1, rect_x2, rect_y2 = 50, 50, 150, 150  # Coordinates of the rectangle
canvas.create_rectangle(rect_x1, rect_y1, rect_x2, rect_y2, fill="lightblue", outline="blue", width=3)


# Try to load the image and place it at the bottom center of the rectangle
try:
    # Load the image
    my_image = tk.PhotoImage(file="/Users/nikhiltripathi/Downloads/login.png")  # Replace with your image path
    
    # Calculate the bottom center of the rectangle
    image_x = (rect_x1 + rect_x2) // 2  # Center x-coordinate
    image_y = rect_y2 + 10  # Slightly below the bottom edge of the rectangle
    
    # Add the image to the canvas
    canvas.create_image(image_x, image_y, image=my_image, anchor="n")  # 'n' aligns image's top center to the coordinates
except:
    canvas.create_text(
        (rect_x1 + rect_x2) // 2, rect_y2 + 10,
        text="No Image Found!", font=("Arial", 12, "italic"), fill="red", anchor="n"
    )

# Run the main event loop
window.mainloop()

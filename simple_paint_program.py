
import tkinter as tk
from tkinter import Canvas, Button, Label

def simple_paint_program():
    window = tk.Tk()
    window.title("Simple Paint Program")

    canvas = Canvas(window, bg="white", width=600, height=400)
    canvas.pack()

    last_x, last_y = None, None
    current_color = "black"

    def paint(event):
        nonlocal last_x, last_y
        if last_x and last_y:
            canvas.create_line(last_x, last_y, event.x, event.y,
                               width=2, fill=current_color, capstyle=tk.ROUND, smooth=tk.TRUE)
        last_x, last_y = event.x, event.y

    def reset_last_coords(event):
        nonlocal last_x, last_y
        last_x, last_y = None, None

    def change_color(color):
        nonlocal current_color
        current_color = color

    canvas.bind("<B1-Motion>", paint)
    canvas.bind("<ButtonRelease-1>", reset_last_coords)

    color_frame = tk.Frame(window)
    color_frame.pack(pady=10)

    colors = ["black", "gray", "white", "red", "green", "blue", "yellow", "orange", "purple"]
    for color in colors:
        button = Button(color_frame, bg=color, width=2, height=1, command=lambda c=color: change_color(c))
        button.pack(side=tk.LEFT, padx=2)

    clear_button = Button(window, text="Clear", command=lambda: canvas.delete("all"))
    clear_button.pack(pady=5)

    window.mainloop()

if __name__ == "__main__":
    simple_paint_program()


import tkinter as tk
from tkinter import Label
import time

def digital_clock():
    root = tk.Tk()
    root.title("Digital Clock")

    def update_time():
        current_time = time.strftime("%H:%M:%S %p")
        label.config(text=current_time)
        label.after(1000, update_time) # Update every 1000ms (1 second)

    label = Label(root, font=("Arial", 80), bg="black", fg="cyan")
    label.pack(anchor='center')

    update_time()
    root.mainloop()

if __name__ == "__main__":
    digital_clock()

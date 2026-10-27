import tkinter as tk
from time import strftime


def update_clock():
    clock_label.config(text=strftime("%H:%M:%S"))
    window.after(1000, update_clock)


window = tk.Tk()
window.title("Digital Clock")
window.resizable(False, False)

clock_label = tk.Label(
    window,
    font=("Arial", 48, "bold"),
    foreground="green",
    background="black",
    padx=20,
    pady=20,
)
clock_label.pack()

update_clock()
window.mainloop()
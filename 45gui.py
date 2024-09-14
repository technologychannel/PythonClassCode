
import tkinter as tk

def greet():
    label.config(text="Hello, Welcome to Nepal")



root = tk.Tk()

root.title("My First App")

root.geometry("300x200")

label = tk.Label(root, text="Hello Nepal")

button = tk.Button(root, text="Greet Me", command=greet)
button.pack(pady=10)

label.pack()

root.mainloop()
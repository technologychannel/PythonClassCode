import tkinter as tk

root = tk.Tk()

root.title("My First App")

root.geometry("300x200")

label = tk.Label(root, text="Hello Nepal")

label.pack()

root.mainloop()
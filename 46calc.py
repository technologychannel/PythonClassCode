
import tkinter as tk
from tkinter import messagebox

def find_sum():
    num1 = entry1.get()
    num2 = entry2.get()
    if num1.isdigit() and num2.isdigit():
        result = int(num1) + int(num2)
        messagebox.showinfo("Result", f"Sum: {result}")
    else:
        messagebox.showerror("Error", "Enter valid numbers")

root = tk.Tk()

root.title("My First App")

root.geometry("500x500")

# Input fields
label1 = tk.Label(root,text="Num1: ")
entry1 = tk.Entry(root,)
label1.pack(pady=5)
entry1.pack(pady=5)

label2 = tk.Label(root,text="Num2: ")
entry2 = tk.Entry(root)
label2.pack(pady=5)
entry2.pack(pady=5)

button = tk.Button(root, text="Add", command=find_sum)
button.pack(pady=10)


root.mainloop()
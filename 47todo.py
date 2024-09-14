import tkinter as tk
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
    entry.delete(0, tk.END)
def delete_task():
    listbox.delete(tk.ANCHOR)

# Create the main window
root = tk.Tk()
root.title("To-Do List")
# Add widgets
entry = tk.Entry(root, width=30)
entry.pack(pady=10)
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)
listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10)
# Set window size
root.geometry("400x400")
root.mainloop()
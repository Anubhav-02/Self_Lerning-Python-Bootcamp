import tkinter as tk
from tkinter import messagebox

# Function to add tasks to the list
def add_task():
    task = task_entry.get()
    if task:
        # Create a checkbox for the task
        var = tk.BooleanVar()
        checkbox = tk.Checkbutton(frame, text=task, variable=var, onvalue=True, offvalue=False, 
                                  font=('Arial', 12), bg='#f0f0f0', padx=10)
        checkbox.var = var
        checkbox.pack(anchor='w', pady=2)
        tasks.append((checkbox, var))
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to delete completed tasks
def delete_completed_tasks():
    for task, var in tasks[:]:
        if var.get():
            task.pack_forget()
            tasks.remove((task, var))

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Set window size and background color
root.geometry("400x500")
root.configure(bg="#f0f0f0")

# Add title label
title_label = tk.Label(root, text="My To-Do List", font=('Arial', 18, 'bold'), bg='#f0f0f0')
title_label.pack(pady=10)

# Create a frame to hold tasks
frame = tk.Frame(root, bg='#f0f0f0')
frame.pack(pady=10, padx=20, fill='both', expand=True)

# Entry widget to input tasks
task_entry = tk.Entry(root, width=35, font=('Arial', 12))
task_entry.pack(pady=10, padx=10)

# Add Task button
add_button = tk.Button(root, text="Add Task", command=add_task, font=('Arial', 12), 
                       bg='#6ab7ff', fg='white', padx=20, pady=5, bd=0)
add_button.pack(pady=5)

# Delete completed tasks button
delete_button = tk.Button(root, text="Delete Completed Tasks", command=delete_completed_tasks, 
                          font=('Arial', 12), bg='#ff6f61', fg='white', padx=20, pady=5, bd=0)
delete_button.pack(pady=5)

# Add some space at the bottom of the app
tk.Label(root, bg='#f0f0f0').pack(pady=10)

# List to store tasks (as tuples of Checkbutton and BooleanVar)
tasks = []

# Run the application
root.mainloop()

# TO-Do list app with GUI
import tkinter as tk
from tkinter import messagebox
import os
#file to store tasks
TASKS_FILE= "tasks.txt"

#Function to add task
def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0,tk.END)
    else:
        messagebox.showwarning("warning", "Task cannot be empty!")

# Function to remove selected task
def remove_task():
    try:
        selected_task = task_listbox.curselection()[0]
        task_listbox.delete(selected_task)
    except IndexError:
        messagebox.showwarning('warning', "Select a task to delete! ")

#Function to save task
def save_task():
    with open(TASKS_FILE, "w") as file:
        tasks = task_listbox.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")
    messagebox.showinfo("Success", "tasks saved successfully !")


# Function to load tasks
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            tasks = file.readlines()
            for task in tasks:
                task_listbox.insert(tk.END, task.strip())

#Create main window
root = tk.Tk()
root.title("To-Do List App ~ Pranjal Tech")
root.geometry("350x450")

#Entry field
task_entry = tk.Entry(root, width=10)
task_entry.pack(pady=10)

#Buttons 
add_button = tk.Button(root, text="Add Task", command=add_task).pack()

remove_btn = tk.Button(root, text="Remove Button", command=remove_task).pack()

save_btn = tk.Button(root, text='Save Tasks', command=save_task).pack()

#Task List box
task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

load_tasks()
root.mainloop()
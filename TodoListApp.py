import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def edit_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        edited_task = task_entry.get()
        tasks_listbox.delete(selected_task_index)
        tasks_listbox.insert(selected_task_index, edited_task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please select a task to edit.")

def delete_task():
    selected_task_index = tasks_listbox.curselection()
    if selected_task_index:
        tasks_listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

root = tk.Tk()
root.title("To-Do List App")

task_entry = tk.Entry(root, width=50)
task_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

add_button = tk.Button(root, text="Add Task", width=20, command=add_task)
add_button.grid(row=0, column=2, padx=5, pady=10)

edit_button = tk.Button(root, text="Edit Task", width=20, command=edit_task)
edit_button.grid(row=1, column=2, padx=5, pady=5)

delete_button = tk.Button(root, text="Delete Task", width=20, command=delete_task)
delete_button.grid(row=2, column=2, padx=5, pady=5)

tasks_listbox = tk.Listbox(root, width=60)
tasks_listbox.grid(row=1, column=0, padx=10, pady=10, rowspan=2, columnspan=2)

root.mainloop()

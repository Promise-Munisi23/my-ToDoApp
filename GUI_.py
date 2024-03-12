import tkinter as tk


root = tk.Tk()
root.title("To-Do App")

tasks = tk.Listbox(root, width=50)
tasks.pack(pady=10)

task_entry = tk.Entry(root, width=40)
task_entry.pack()

def add_task():
    task = task_entry.get()
    if task:
        tasks.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    try:
        index = tasks.curselection()[0]
        tasks.delete(index)
    except IndexError:
        pass

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

list_button = tk.Button(root, text="List Available Tasks", command=add_task)
list_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

root.mainloop()
import tkinter as tk
from tkinter import *
import tkinter.messagebox as messagebox
from Adding import *
from tkinter import simpledialog


root = tk.Tk()
root.configure(background="#d00ef1")
root.title("Promise' To-Do App")

tasks = tk.Listbox(root, width=50)
tasks.pack(pady=10)

task_entry = tk.Entry(root, width=40)
task_entry.pack()

def add_task():
    task = task_entry.get()
    with open('todo_list.txt', 'a') as file:
        file.write(task + '\n')
    messagebox.showinfo("Success", "Event successfully added!")
def view_task():
    task = list_todo()
    
    tasks.delete(0, tk.END)
    if task:
        for i, line in enumerate(task, start=1):
            tasks.insert(tk.END, f"{i}. {line.strip()}")
        
        
        
# def delete_task():
#     # try:
   
#         index = tasks.curselection()[0:]
#         tasks.delete(index)
#     # except IndexError:
#     #     pass
    


 
        # index = tasks.curselection()[0]  
        # with open('todo_list.txt', 'r') as file:
        #     tasks_list = file.readlines()

        # if 0 <= index < len(tasks_list):
        #     deleted_task = tasks_list.pop(index)  

        #     with open('todo_list.txt', 'w') as file:
        #         file.writelines(tasks_list)  

        # #     messagebox.showinfo("Task Deleted", f"The task '{deleted_task.strip()}' was deleted successfully.")
        # else:
        #     print('ghfhfg')
            
# messagebox.showerror("Error", "Invalid task selection.")



   





def delete_task():
    number = simpledialog.askstring("User number","Enter a number")
    delete_todo(int(number))
    
    
add_button = tk.Button(root, text="Add ToDo", command=add_task)
add_button.pack(pady=5)

list_button = tk.Button(root, text="List Available ToDos", command=view_task)
list_button.pack(pady=5)


delete_button = tk.Button(root, text="Delete ToDo", command=delete_task)
delete_button.pack(pady=5)

root.mainloop()
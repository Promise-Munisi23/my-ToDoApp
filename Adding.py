from deleting import *
from exit import *

def add_todo(items, date):
    with open('todo_list.txt', 'a') as compiler:
        compiler.write(items + '\n')
    print('items added to the todo successfully!')


def list_todo():
    try:
        with open('todo_list.txt', 'r') as file:
            todo_things = file.readlines()
            if todo_things:
                print("Your To-Do List:")
                for index_number, corresponding_todo in enumerate(todo_things, start=1):
                    print(f"{index_number}. {corresponding_todo.strip()}")
            else:
                print("The to-do list is empty.")
    except FileNotFoundError:
        print("No list found. you can create one by adding to do items")


def main():
    while True:
        print("\nList of available commands:")
        print("1. Add a To-Do")
        print("2. List all To-Dos")
        print("3. Delete a ToDo")
        print("4. exit the application")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            todo_item = input("Enter the to-do: ")
            date = input("Enter the date (YYYY-MM-DD): ")
            add_todo(todo_item, date)
            break
        elif choice == '2':
            list_todo()
        elif choice == '3':
            index = int(input("Enter the index of the todo to delete: "))
            delete_todo(index)
        elif choice == '4':
            exit_app()
        else:
            print("Invalid choice. Please try again.")
        
            
if __name__ == '__main__':
    main()

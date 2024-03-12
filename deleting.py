def delete_todo(index):
    """This function deletes a todo from the list using an index number attached to that todo
    """
    try:
        with open('todo_list.txt', 'r') as file:
            todos = file.readlines()
        with open('todo_list.txt', 'w') as file:
            for i, todo in enumerate(todos, start=1):
                if i != index:
                    file.write(todo)
        print('Todo deleted successfully!')
    except FileNotFoundError:
        print("No list found. you can create one by adding to do items.")
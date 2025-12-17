
def get_todos():
    with open("todos.txt", "r") as file:
        list_of_todos = file.readlines()
        return  list_of_todos

def write_todos(list_of_todos):
    with open("todos.txt", "w") as file:
        file.writelines(list_of_todos)


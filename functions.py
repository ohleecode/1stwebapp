FILENAME = "todo.txt"

def get_todos(filename=FILENAME):
    with open(filename,"r") as file:
        todos = file.readlines()
    return todos
def put_todos(todos, filename=FILENAME):
    with open(filename,"w") as file:
        file.writelines(todos)

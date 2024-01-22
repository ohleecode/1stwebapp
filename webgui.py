import streamlit as st
import functions

todos= functions.get_todos()
def add_todo():
    todo = st.session_state["ntodo"]+'\n'
    print(todo)
    todos.append(todo)
    functions.put_todos(todos)



st.title("Web app")
st.subheader("This is a todo list")
st.write("you will be better off")
for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        print(checkbox)
        todos.pop(index)
        functions.put_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="label it",
              label_visibility="hidden",placeholder= "enter your todo here",
              on_change=add_todo,
              key="ntodo")
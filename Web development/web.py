import streamlit as st
import function
import time
import os

todos = function.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    function.write_todos(todos)


st.title('My Todo App')
st.subheader('This is my Todo app')
st.write('This app is to increase your productivity')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        function.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label='', placeholder='Add new todo...',
              on_change=add_todo, key='new_todo')


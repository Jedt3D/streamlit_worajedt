import streamlit as st

st.title('My To-Do List Creator')
my_todo_list = ["Learn Markdown", "Learn Python", "Learn Streamlit"]
st.write('My current To-Do list is:', my_todo_list)

new_todo = st.text_input("What do you need to do?")

if st.button('Add the new To-Do item'):
    st.write('Adding a new item to the list')
    my_todo_list.append(new_todo)

st.write('My new To-Do list is:', my_todo_list)

# TODO
# 1. make it save to session state
#    https://docs.streamlit.io/library/api-reference/session-state
# 2. add a number input for number of day for each todo.
#    You may need to change the data structure of `my_todo_list`



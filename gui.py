import FreeSimpleGUI as sg
import functions
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("DarkBlue 17")
text = sg.Text("Write a to-do",font=("Arial",20))
input_text = sg.InputText(font=("Arial",20),key="input_text")

add_button = sg.Button("Add",font=("Arial",20))
edit_button = sg.Button("Edit",font=("Arial",20))
complete_button = sg.Button("Complete",font=("Arial",20))

list_box = sg.Listbox(functions.get_todos(),key="list_box",size=(60,10),font=("Arial",20))

window = sg.Window("TODO APP",[[text,input_text,add_button],[list_box,edit_button],[complete_button]])

while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Add":
        todo= values["input_text"]
        if len(todo) > 0:
            todos_list = functions.get_todos()
            todos_list.append(todo + "\n")
            functions.write_todos(todos_list)
            window["list_box"].update(todos_list)
            window["input_text"].update("")


window.close()
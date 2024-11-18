from http.client import responses
from tkinter.constants import SCROLL
from tkinter.ttk import Label
from traceback import print_tb

import flet as ft
from anyio.abc import value
from flet_core import MainAxisAlignment, ScrollMode, LinearGradient
from flet_core.types import AppView
from pygments.styles.dracula import background

from MyCustomItems import  *





def main(page: ft.Page):
    page.scroll = True
    # page.client_storage.clear()
    tasks = []

    def addTask(e):
        newTaskText = inputText.value
        # if len(newTaskText) >= 1:
        tasks.append([newTaskText,"undo"])
        page.client_storage.set("tasks",tasks)
        taskViewItems.append(Task(text=newTaskText,color="#2c3e50",save=save))
        save()
        page.update()







    page.window_height  = 915
    page.window_width = 412
    page.bgcolor = "#212f3d"


    if page.client_storage.contains_key("tasks"):
        tasks = page.client_storage.get("tasks")
    else:
        page.client_storage.set("tasks",tasks)



    page.add(
        ft.Container(
            height=80
        )
    )

    taskViewItems = []
    # get information from database

    def save():
        taskText = []
        for item in taskViewItems:
            taskText.append([item.text, item.state])


        page.client_storage.set("tasks", taskText)



    for task in tasks:
        new = Task(text=task[0], color="#2c3e50",state=task[1],save=save)






        taskViewItems.append(new)





    tasksView = ft.Container(
        content=ft.Column(
            controls=taskViewItems,
            scroll= ft.ScrollMode.HIDDEN,
            width=417,
            height=650,

        ),
        border_radius=10,
    )
    inputText = ft.TextField(col=8, label="Add your Task",border=ft.InputBorder.NONE,content_padding=20,border_color="#5499c7",max_length=67)
    appView = ft.Column(controls=[
        ft.ResponsiveRow([
            inputText,
            ft.ElevatedButton(col=4, text="Add", height=60, width=2000,bgcolor="#5499c7",color="white",
                              style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),on_click=addTask),
        ]),

        tasksView
    ])

    def test():
        print("hi")

    az = [Task(text="Do my Home work ------",color="#2c3e50"),
          Task(text="Do my Home work ------", color="#2c3e50"),
          Task(text="Do my Home work ------", color="#2c3e50"),
          Task(text="Do my Home work ------", color="#2c3e50"),
          Task(text="Do my Home work ------", color="#2c3e50"),
          ]






    # taskViewItems.append(Task(text="Do my Home work acutlly English HomeWork but I   dd can do someting There is no voluntary",color="#2c3e50"))
    # taskViewItems.append(az)
    # taskViewItems.append(Task(text="Do my Home work acutlly English HomeWork but I   dd can do someting There is no voluntary",color="#2c3e50"))
    # taskViewItems.append(Task(text="Do my Home work acutlly English HomeWork but I   dd can do someting There is no voluntary",color="#2c3e50"))
    # taskViewItems.append(Task(text="Do my Home work acutlly English HomeWork but I   dd can do someting There is no voluntary",color="#2c3e50"))
    # taskViewItems.append(Task(text="Do my Home work acutlly English HomeWork but I   dd can do someting There is no voluntary",color="#2c3e50"))
    # taskViewItems.append(Task(text="Do my Home work acutlly English HomeWork but I   dd can do someting There is no voluntary",color="#2c3e50"))
    # taskViewItems.append(Task(text="Do my Home work acutlly English HomeWork but I   dd can do someting There is no voluntary",color="#2c3e50"))
    page.update()




    page.add(appView)











ft.app(main)

from multiprocessing.managers import Value

import flet as ft
from flet_core import CrossAxisAlignment, MainAxisAlignment
from flet_core.border_radius import horizontal
from pydantic import validate_email
from requests import delete


class Task(ft.Container):
    def __init__(self,text,color = "gray",state = "undo",save = print ):
        super().__init__()
        self.text = text
        self.bgcolor = color
        self.width = 1000
        self.height = 160
        self.btnDoing = ft.ElevatedButton(text="Doing")
        self.btnDone = ft.ElevatedButton(text="Done")
        self.doneColor = "#45b39d"
        self.state = state
        self.save = save

        self.doingColor = "#f5b041"
        # self.doingColor = "#f1c40f"
        self.btnPadding = 30
        self.alignment = ft.alignment.bottom_center
        self.border_radius = 10
        self.animate= ft.animation.Animation(duration=1500,curve="ease")





        self.cDone = ft.Container(
                    width=100,
                    height=80,
                    bgcolor= self.doneColor,
                    on_click=self.change_to_done,
                    padding = ft.padding.only(top=self.btnPadding),
                    content= ft.Text(value="Done",text_align=ft.TextAlign.CENTER,size=15,weight=ft.FontWeight.BOLD),


                )

        self.cDoing = ft.Container(
                    width=100,
                    height=80,
                    bgcolor=self.doingColor,
                    on_click= self.change_to_doing,
                    padding = ft.padding.only(top=self.btnPadding),
                    content=ft.Text(value="Doing", text_align=ft.TextAlign.CENTER, size=15, weight=ft.FontWeight.BOLD)

        )

        self.content =  ft.ResponsiveRow([
            ft.Column(col=8,controls=[
                ft.Container(
                    content=ft.Text(value=self.text,size=25,no_wrap=False,font_family="arial"),
                    padding =10
                )
            ]),
            ft.Column(col=4,controls=[self.cDone,
                                      self.cDoing
            ],horizontal_alignment= CrossAxisAlignment.END,spacing=0),



        ],width=1000)

        if self.state == "done":
            self.done()
        elif self.state=="doing":
            self.doing()


    def change_to_doing(self,e):
        self.bgcolor = self.doingColor
        self.state = "doing"
        self.save()
        self.update()

    def change_to_done(self,e):
        print("green")
        self.cDoing.visible = False
        self.bgcolor = self.doneColor
        self.state = "done"
        self.save()
        self.update()


    def doing(self):
        self.bgcolor = self.doingColor
        self.state = "doing"

        # self.update()

    def done(self):

        self.bgcolor = self.doneColor
        self.state = "done"
        self.cDoing.visible = False
        # self.update()





    def delete(self,e):
        self.opacity = 0
        self.update()



import functools
import os
import time

import PIL.Image
import PIL.ImageTk

from tkinter import *

from common_data import common_data
from window_design import window_design

def invade_poland(invasion_frame: Toplevel) -> None:
    invasion_frame.deiconify()

    invasion_frame.geometry("1500x650")
    invasion_frame.configure(bg = window_design.window_colours[0].colour_code)

    germany_path = os.path.join(common_data.get_root_folder(), "Poland", "germany.png")
    poland_path = os.path.join(common_data.get_root_folder(), "Poland", "poland3.png")
    tank_path = os.path.join(common_data.get_root_folder(), "Poland", "tank.png")

    germany_image = PIL.Image.open(germany_path, "r")
    poland_image = PIL.Image.open(poland_path, "r")
    tank_image = PIL.Image.open(tank_path, "r")

    germany_image = PIL.ImageTk.PhotoImage(germany_image.resize((400, 400)))
    poland_image = PIL.ImageTk.PhotoImage(poland_image.resize((400, 400)))
    tank_image = PIL.ImageTk.PhotoImage(tank_image.resize((80, 80)))

    germany = Label(invasion_frame, image = germany_image, bg = window_design.window_colours[0].colour_code)
    germany.place(x = 50, y = 50, width = 500, height = 500)
    germany.img = germany_image
    
    poland = Label(invasion_frame, image = poland_image, bg = window_design.window_colours[0].colour_code)
    poland.place(x = 850, y = 50, width = 500, height = 500)
    poland.img = poland_image

    tank_list: list[Label] = []

    for i in range(6):
        tank: Label = Label(invasion_frame, image = tank_image, bg = window_design.window_colours[0].colour_code)
        tank.place(x = 400, y = 40 + (i * (80 + 10)))
        tank.img = tank_image
        tank_list.append(tank)

    invade_button = Button(invasion_frame, text = "Invade Poland", bg = window_design.button_colours[0].colour_code, fg = window_design.button_colours[1].colour_code, font = window_design.main_font)
    invade_button.configure(command = functools.partial(invade, invasion_frame, tank_list, invade_button))
    invade_button.place(x = 50, y = 600, width = 150, height = 25)


def invade(invasion_frame, tank_list, invade_button):
    invade_button.destroy()
    
    for i in range(10):
        for tank in tank_list:
            tank.place(x = tank.winfo_x() + 50, y = tank.winfo_y())        

        invasion_frame.update()
        time.sleep(1)
    
    time.sleep(2)
    
    tank_path = os.path.join(common_data.get_root_folder(), "Poland", "tank.png")
    tank_image = PIL.Image.open(tank_path, "r").transpose(PIL.Image.Transpose.FLIP_LEFT_RIGHT)
    tank_image = PIL.ImageTk.PhotoImage(tank_image.resize((80, 80)))

    boom_path = os.path.join(common_data.get_root_folder(), "Poland", "boom.png")
    boom_image = PIL.Image.open(boom_path, "r")
    boom_image = PIL.ImageTk.PhotoImage(boom_image.resize((350, 350)))

    boom = Label(invasion_frame, image = boom_image, bg = window_design.window_colours[0].colour_code)
    boom.place(x = 950, y = 75, width = 300, height = 300)
    boom.img = boom_image

    for tank in tank_list:
        tank.configure(image = tank_image)
    
    for i in range(10):
        for tank in tank_list:
            tank.place(x = tank.winfo_x() - 50, y = tank.winfo_y())
        
            invasion_frame.update()
        time.sleep(1)

    for tank in tank_list:
        tank.img = tank_image

    time.sleep(10)
    invasion_frame.destroy()
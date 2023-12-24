import tkinter
import requests
from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO


def load_image(path="", width=0, height=0):
    image = Image.open(path)
    image = image.resize((width, height))
    image = ImageTk.PhotoImage(image)
    return image


def show(button, all_places):
    button.place_configure(x=all_places[str(button)]["x"], y=all_places[str(button)]["y"])


def hide(button):
    button.place_configure(x=-500, y=-500)


def add_place(places, button, x, y):
    places[str(button)] = {"x": x, "y": y}


def hide_all(buttons):
    for button in buttons:
        hide(button)


class Utils:
    def __init__(self, login_user_button, login_gardener_button, register_button, help_button, info_button, admin_button, all_places):
        self.login_user_button = login_user_button
        self.login_gardener_button = login_gardener_button
        self.register_button = register_button
        self.help_button = help_button
        self.info_button = info_button
        self.admin_button = admin_button
        self.all_the_buttons = [login_user_button, login_gardener_button, register_button,
                                help_button, info_button, admin_button]

        self.all_places = all_places

    def log_in_user(self):
        hide_all(self.all_the_buttons)

    def log_in_gardener(self):
        hide_all(self.all_the_buttons)

    def registration(self):
        pass

    def help(self):
        pass

    def info(self):
        pass

    def log_in_admin(self):
        pass


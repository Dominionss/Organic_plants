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
    button.place_configure(x=4000, y=4000)


def add_place(places, button, x, y):
    places[str(button)] = {"x": x, "y": y}


def hide_all(buttons):
    for button in buttons:
        hide(button)


class Utils:
    def __init__(self, login_user_button, login_gardener_button, register_button, help_button, info_button,
                 admin_button, all_places, enter_username, enter_password, repeat_password, back_button):
        self.login_user_button = login_user_button
        self.login_gardener_button = login_gardener_button
        self.register_button = register_button
        self.help_button = help_button
        self.info_button = info_button
        self.admin_button = admin_button
        self.enter_username = enter_username
        self.enter_password = enter_password
        self.repeat_password = repeat_password
        self.back_button = back_button
        self.all_the_buttons = [login_user_button, login_gardener_button, register_button,
                                help_button, info_button, admin_button, enter_username, enter_password,
                                repeat_password, back_button]

        self.all_places = all_places
        self.state = "main"
        self.previous_state = self.state

    def back(self):
        self.state = self.previous_state
        self.change_state(self.state)

    def change_state(self, state):
        self.state = state
        if state == "main":
            hide_all(self.all_the_buttons)
            show(self.back_button, self.all_places)
            show(self.login_user_button, self.all_places)
            show(self.login_gardener_button, self.all_places)
            show(self.register_button, self.all_places)
            show(self.help_button, self.all_places)
            show(self.info_button, self.all_places)
            show(self.admin_button, self.all_places)
        elif state == "user log" or "gardener log":
            hide_all(self.all_the_buttons)
            show(self.back_button, self.all_places)
            show(self.enter_username, self.all_places)
            show(self.enter_password, self.all_places)
        elif state == "registration":
            hide_all(self.all_the_buttons)
            show(self.enter_username, self.all_places)
            show(self.enter_password, self.all_places)
            show(self.repeat_password, self.all_places)

    def log_in_user(self):
        self.previous_state = self.state
        self.change_state("user log")

    def log_in_gardener(self):
        self.previous_state = self.state
        self.change_state("gardener log")

    def registration(self):
        self.previous_state = self.state
        self.change_state("registration")

    def help(self):
        pass

    def info(self):
        pass

    def log_in_admin(self):
        hide_all(self.all_the_buttons)


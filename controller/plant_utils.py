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


class Utils:
    def __init__(self, login_user_button, login_gardener_button, register_button, help_button, info_button, admin_button):
        self.login_user_button = login_user_button
        self.login_gardener_button = login_gardener_button
        self.register_button = register_button
        self.help_button = help_button
        self.info_button = info_button
        self.admin_button = admin_button

    def show(self, button):
        button.place(x=0, y=0)

    def hide(self, button):
        button.pack_forget()

    def log_in_user(self):
        pass

    def log_in_gardener(self):
        pass

    def registration(self):
        pass

    def help(self):
        pass

    def info(self):
        pass

    def log_in_admin(self):
        pass


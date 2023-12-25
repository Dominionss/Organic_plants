import requests
from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO
from controller import *

window = Tk()
window.state("zoomed")
window.iconbitmap("images/earth.ico")
window.title("Organic plants")

WIDTH, HEIGHT = window.winfo_screenwidth(), window.winfo_screenheight()
MAP = load_image("images/map.jpg", WIDTH + 5, HEIGHT + 5)
BUTTON_WIDTH, BUTTON_HEIGHT = 40, 5
ALL_PLACES = {}

mapLabel = Label(window, image=MAP)
mapLabel.place(x=-5, y=-5)

log_in_user_button = Button(window, text="Log in like User", width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
log_in_user_button.place(x=650, y=200)
add_place(ALL_PLACES, log_in_user_button, 650, 200)

log_in_gardener_button = Button(window, text="Log in like Gardener", width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
log_in_gardener_button.place(x=650, y=300)
add_place(ALL_PLACES, log_in_gardener_button, 650, 300)

register_button = Button(window, text="Register", width=BUTTON_WIDTH, height=BUTTON_HEIGHT)
register_button.place(x=650, y=400)
add_place(ALL_PLACES, register_button, 650, 400)

help_button = Button(window, text="Help", width=10, height=2)
help_button.place(x=10, y=680)
add_place(ALL_PLACES, help_button, 10, 680)

info_button = Button(window, text="Info", width=10, height=2)
info_button.place(x=10, y=730)
add_place(ALL_PLACES, info_button, 10, 730)

admin_button = Button(window, text="Admin", width=10, height=2)
admin_button.place(x=1450, y=730)
add_place(ALL_PLACES, admin_button, 1450, 730)

enter_username = Entry(window, width=30, font=("Arial", 24, "bold"))
enter_username.place(x=4000, y=4000)
add_place(ALL_PLACES, enter_username, 500, 200)

enter_password = Entry(window, width=30, font=("Arial", 24, "bold"), show="*")
enter_password.place(x=4000, y=4000)
add_place(ALL_PLACES, enter_password, 500, 300)

repeat_password = Entry(window, width=30, font=("Arial", 24, "bold"), show="*")
repeat_password.place(x=4000, y=4000)
add_place(ALL_PLACES, repeat_password, 500, 400)

back_button = Button(window, width=10, height=2, image=)
back_button.place(x=1450, y=730)
add_place(ALL_PLACES, back_button, 1450, 730)

utils = Utils(log_in_user_button, log_in_gardener_button, register_button, help_button, info_button,
              admin_button, ALL_PLACES, enter_username, enter_password, repeat_password, back_button)

log_in_user_button.config(command=utils.log_in_user)
log_in_gardener_button.config(command=utils.log_in_gardener)
register_button.config(command=utils.registration)
help_button.config(command=utils.help)
info_button.config(command=utils.info)
admin_button.config(command=utils.log_in_admin)

window.mainloop()

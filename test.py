from tkinter import Tk, Button, PhotoImage

def on_button_click():
    print("Кнопка с изображением нажата!")

root = Tk()

# Загружаем изображение
image = PhotoImage(file="images/back.png")

# Создаем кнопку с изображением
image_button = Button(root, image=image, command=on_button_click)
image_button.place(x=0, y=0)

root.mainloop()




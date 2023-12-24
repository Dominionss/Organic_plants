from tkinter import Tk, Button

def move_button():
    new_x = 100  # Новая координата x
    new_y = 150  # Новая координата y
    button.place_configure(x=new_x, y=new_y)

root = Tk()

# Создаем кнопку
button = Button(root, text="Переместить кнопку")

# Размещаем кнопку с начальными координатами
button.place(x=50, y=50)

# Создаем кнопку для изменения положения
move_button_button = Button(root, text="Изменить положение", command=move_button)
move_button_button.pack()

root.mainloop()




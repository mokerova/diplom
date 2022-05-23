import tkinter as tk
from tkinter import filedialog as fd
from tkinter import Tk, Text
from tkinter import *
from PIL import Image
from PIL import ImageTk

from main import draw_tree

from main import load

import idlelib.tooltip
from idlelib.tooltip import Hovertip


def callback():
    name = fd.askopenfilename()
    print(name)
    text.insert('1.0', name)


def click_button():
    path = text.get("1.0","end-1c")

    print(path)
    
    max_depth = max_depth_text.get("1.0","end-1c")
    min_size = min_size_text.get("1.0","end-1c")
    if max_depth == '':
        max_depth = None
    else:
        max_depth = int(max_depth)
    if min_size == '':
        min_size = 1
    else:
        min_size = float(min_size)
    print(path, max_depth, min_size)
    if path != '':
        score = load(path, max_depth, min_size)
        if score == "Неверный формат файла":
            label_accuracy = tk.Label(win, text=score, font=("Helvetica", 25))
            label_accuracy.pack(ipadx=10, ipady=10)
            text.delete('1.0', END)
        else:
            label_accuracy = tk.Label(win, text="Точность: " + str(score), font=("Helvetica", 14))
            label_accuracy.pack(ipadx=10, ipady=10)
            canvas = tk.Canvas(win, height=600, width=600)
            img = tk.PhotoImage(file='filename.png')
            image = canvas.create_image(0, 0, anchor='nw', image=img)
            # canvas.grid(row=2,column=1)
            canvas.pack()
            text.delete('1.0', END)
    else:
        label_accuracy = tk.Label(win, text='Выберите файл!', font=("Helvetica", 25))
        label_accuracy.pack(ipadx=10, ipady=10)
        text.delete('1.0', END)


# Создаем окно приложения
win = Tk()
win.title('Деревья решений')
win.minsize(800, 500)
win.resizable(True, True)


file_top = tk.Frame(win)
text = tk.Text(file_top, height=1)
text.pack(side='left')
Hovertip(text, 'путь к файлу')
errmsg = 'Error!'
button = tk.Button(file_top, text='Открыть файл',
                   command=callback)
button.pack(side='right')
file_top.pack()

# folds_top = tk.Frame(win)
# folds_text = tk.Text(folds_top, height=1)
# folds_text.pack(side='right')
# folds_label = tk.Label(folds_top, text='n_folds')
# folds_label.pack(side='left')
# folds_top.pack()
# Hovertip(folds_label, '')
# # написать выше

max_depth_top = tk.Frame(win)
max_depth_text = tk.Text(max_depth_top, height=1)
max_depth_text.pack(side='right')
max_depth_label = tk.Label(max_depth_top, text='max_depth')
max_depth_label.pack(side='left')
max_depth_top.pack()
Hovertip(max_depth_label, 'максимальная глубина дерева')


min_size_top = tk.Frame(win)
min_size_text = tk.Text(min_size_top, height=1)
min_size_text.pack(side='right')
min_size_label = tk.Label(min_size_top, text='min_size')
min_size_label.pack(side='left')
min_size_top.pack()
Hovertip(min_size_label, 'минимальное количество выборок, необходимое для нахождения в конечном узле. ')

button = tk.Button(win, text='Начать', command=click_button)
button.pack()

# label_result = tk.Label(win, text='Результат: ', font=("Helvetica", 12))
# label_result.pack(ipadx=10, ipady=10)
# c = tk.Canvas(win, width=400, height=400, bg='white')
# c.pack()
# canvas = tk.Canvas(win, height=600, width=600)
# img = tk.PhotoImage(file='filename.png')
# image = canvas.create_image(0, 0, anchor='nw',image=img)
# # canvas.grid(row=2,column=1)
# canvas.pack()
#
# label_accuracy = tk.Label(win, text='Tут Будет Выводиться Точность', font=("Helvetica", 14))
# label_accuracy.pack(ipadx=10, ipady=10)

win.mainloop()

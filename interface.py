import tkinter as tk
from tkinter import filedialog as fd
from tkinter import Tk, Text
from tkinter import *
from tkinter.ttk import Combobox

from PIL import Image
from PIL import ImageTk

# from main import draw_tree

from main import load
from idlelib.tooltip import Hovertip

def kod(rezult):
    # try:
    from filename1 import funciya

    a = funciya()
    rezult.config(text="Определен класс - " + str(a))

    print(a)
    # except:


def obrabotka_stroki(params, zn_params, rezult):
    a = []
    for param in zn_params:
        a.append(param.get("1.0","end-1c"))
    with open('xyz.txt', 'r') as f1, open('filename1.py', 'w') as f2:
        lines = f1.readlines()
        f2.write('def funciya():\n')
        for i in range(len(params)):
            f2.write('    ' + str(params[i]) + ' = ' + a[i] + '\n')
        for line in lines:
            line1 = line.replace("class:", "clas =")
            line1 = line1.replace("|   ","    ")
            if line1.count('|--- clas = ') != 0:
                line1 = line1.replace("|--- ", "    ")
            else:
                line1 = line1.replace("|--- ", "    if ")
                line1 = line1[:-1] + ':' + line1[-1]
            f2.write(line1)
        f2.write('    return clas')
    kod(rezult)

def create_params(list_param):
    print(list_param)
    label = tk.Label(win, text="Введите параметры для определения класса")
    label.pack()
    all_label = []
    all_text = []
    frame_params = tk.Frame(win)
    for i in range(len(list_param)):
        label = tk.Label(frame_params, text=list_param[i])
        label.grid(row=0, column=i)
        text_params = tk.Text(frame_params, height=1, width=8)
        text_params.grid(row=1, column=i)
        all_label.append(label)
        all_text.append(text_params)
    rezult = tk.Label(frame_params, text='')
    rezult.grid(row=2,columnspan=len(list_param)+1)
    but_param = tk.Button(frame_params, text='Запуск',
                   command=lambda: obrabotka_stroki(list_param, all_text, rezult))
    but_param.grid(row=1, column=len(list_param)+1)

    # rezult.pack()
    frame_params.pack()


def callback():
    name = fd.askopenfilename()
    print(name)
    text.insert('1.0', name)


def click_button():
    global label_accuracy
    canvas.delete("all")
    path = text.get("1.0","end-1c")

    print(path)

    max_depth = max_depth_text.get("1.0","end-1c")
    min_size = min_size_text.get("1.0","end-1c")
    criteri = combo_razb.get()
    splitter = combo_razb1.get()
    if criteri == '' or criteri == 'Индекс Джини':
        criteri = 'gini'
    elif criteri == 'Энтропия':
        criteri = 'entropy'
    if splitter == '' or splitter == 'Наилучшее':
        splitter = 'best'
    elif splitter == 'Случайное наилучшее':
        splitter = 'random'
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
        score,  list_param = load(path, max_depth, min_size, criteri, splitter)
        create_params(list_param)
        if score == "Неверный формат файла":
            label_accuracy.config(text=score)
            # label_accuracy = tk.Label(win, text=score, font=("Helvetica", 25))
            label_accuracy.pack(ipadx=10, ipady=10)
            text.delete('1.0', END)
        else:
            label_accuracy.config(text="Точность: " + str(score))
            # label_accuracy = tk.Label(win, text="Точность: " + str(score), font=("Helvetica", 14))
            label_accuracy.pack(ipadx=10, ipady=10)
            # canvas = tk.Canvas(win, height=600, width=600)
            img = tk.PhotoImage(file='filename.png')
            image = canvas.create_image(0, 0, anchor='nw', image=img)
            # canvas.grid(row=2,column=1)
            canvas.pack()
            text.delete('1.0', END)
    else:
        label_accuracy.config(text="Выберите файл!")
        # label_accuracy = tk.Label(win, text='Выберите файл!', font=("Helvetica", 25))
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

vybor = tk.Frame(win)
label_razb = tk.Label(vybor, text = "Выберите критерий разбиения")
label_razb.pack(side='right',padx=70)
label_razb1 = tk.Label(vybor, text = "Разбиение")
label_razb1.pack(side='left',padx=97)
vybor.pack()

combo_vybor = tk.Frame(win, bd = 5)
combo_razb = Combobox(combo_vybor, values=[
                                    "Индекс Джини",
                                    "Энтропия"], state="readonly")
combo_razb.pack(side='right',padx=45)

combo_razb1 = Combobox(combo_vybor, values=[
                                    "Наилучшее",
                                    "Случайное наилучшее"], state="readonly")
combo_razb1.pack(side='left',padx=45)
combo_vybor.pack()
button = tk.Button(win, text='Начать', command=click_button)
button.pack()
label_accuracy = tk.Label(win, text=" ", font=("Helvetica", 14))
canvas = tk.Canvas(win, height=500, width=500)
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

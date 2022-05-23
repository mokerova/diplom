import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import openpyxl
from sklearn import tree



def load(name_file, max_depth, min_size):
    try:
        df = pd.read_excel(name_file)
        x = df.iloc[:, 1:]
        y = df.iloc[:, :1]
        x.head(3)
        y.head(3)
        return draw_tree(x, y, max_depth, min_size)
    except ValueError:
        return "Неверный формат файла"


def draw_tree(x, y, max_depth, min_size):
    model = tree.DecisionTreeClassifier(criterion="gini", max_depth=max_depth, min_samples_leaf=min_size)
    model.fit(x, y)
    print(model.score(x, y))
    fig = plt.figure(figsize=(6, 6))
    fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)
    tree.plot_tree(model)
    fig.savefig('filename.png')
    return model.score(x, y)

# name_file = 'baza3.xlsx'
# draw_tree(name_file)

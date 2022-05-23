import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import openpyxl
from sklearn import tree


def draw_tree(name_file):
    df = pd.read_excel(name_file)
    x = df.iloc[:, 1:]
    y = df.iloc[:, :1]
    x.head(3)
    y.head(3)

    model = tree.DecisionTreeClassifier(criterion="gini", max_depth=3)
    model.fit(x, y)
    print(model.score(x, y))
    fig = plt.figure(figsize=(6, 6))
    fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)
    tree.plot_tree(model)
    fig.savefig('filename.png')
    return model.score(x, y)

# name_file = 'baza3.xlsx'
# draw_tree(name_file)

import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import openpyxl
from sklearn import tree
from sklearn.tree import export_text
# from interface import create_params



def load(name_file, max_depth, min_size, criteri, splitter):
    try:
        df = pd.read_excel(name_file)
        x = df.iloc[:, 1:]
        y = df.iloc[:, :1]
        print(x)
        x.head(3)
        y.head(3)
        return draw_tree(x, y, max_depth, min_size, criteri, splitter), x.columns
    except ValueError:
        return "Неверный формат файла"


# def obrabotka_stroki(params, zn_params):
#     a = []
#     for param in zn_params:
#         a.append(param.get("1.0","end-1c"))
#     with open('xyz.txt', 'r') as f1, open('filename1.py', 'w') as f2:
#         lines = f1.readlines()
#         f2.write('def funciya():\n')
#         for i in range(len(params)):
#             f2.write('    ' + str(params[i]) + ' = ' + a[i] + '\n')
#         for line in lines:
#             line1 = line.replace("class:", "clas =")
#             line1 = line1.replace("|   ","    ")
#             if line1.count('|--- clas = ') != 0:
#                 line1 = line1.replace("|--- ", "    ")
#             else:
#                 line1 = line1.replace("|--- ", "    if ")
#                 line1 = line1[:-1] + ':' + line1[-1]
#             f2.write(line1)
#         f2.write('    return clas')




def draw_tree(x, y, max_depth, min_size, criteri, splitter):
    model = tree.DecisionTreeClassifier(criterion=criteri, max_depth=max_depth, min_samples_leaf=min_size, splitter=splitter)
    model.fit(x, y)
    print(model.score(x, y))
    fig = plt.figure(figsize=(5, 5))
    fig.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=None, hspace=None)
    print(model.fit(x,y))
    tree.plot_tree(model)
    fig.savefig('filename.png')
    tree_rules = export_text(model, feature_names=list(x.columns))
    f = open('xyz.txt', 'w')
    f.write(tree_rules)
    f.close()
    print(tree_rules)
    print(x.columns)
    # kod()
    return model.score(x, y)

# name_file = 'baza3.xlsx'
# draw_tree(name_file)

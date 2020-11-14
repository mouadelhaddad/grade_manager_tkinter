import matplotlib.pyplot as plt
from SQL import *
import matplotlib
def move_figure(f, x, y):
    """Move figure's upper left corner to pixel (x, y)"""
    backend = matplotlib.get_backend()
    if backend == 'TkAgg':
        f.canvas.manager.window.wm_geometry("+%d+%d" % (x, y))
    elif backend == 'WXAgg':
        f.canvas.manager.window.SetPosition((x, y))
    else:
        # This works for QT and GTK
        # You can also use window.setGeometry
        f.canvas.manager.window.move(x, y)
def statistique():
    names=[]
    notes=[]
    l=get_st()
    for i in range(len(l)):
        names.append(l[i][0])
        notes.append(l[i][1])
    labels = 'reussi','non reussi'
    a=0
    for i in notes:
        if i<11:
            a+=100/len(notes)
    sizes = [100-a,a]

    fig=plt.figure(figsize=(12,6))
    plt.subplot(121)
    plt.bar(names, notes)
    plt.subplot(122)
    explode = (0, 0.1)
    plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',shadow=True, startangle=90)
    fig.suptitle('Les statistiques des notes')
    move_figure(fig, 100, 40)
    plt.show()

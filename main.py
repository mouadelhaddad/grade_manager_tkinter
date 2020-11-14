# coding=utf-8
#gestion des importation
try:
    from tkinter import *
except ImportError:
    from Tkinter import *
from mod import *
from SQL import *
from stats import *
#definition des methodes:
def ajouter():
    name=entry1.get()
    nt=int(entry2.get())
    txt=texte.get("1.0", 'end-1c')
    if selected.get()==1:
        redoub="Oui"
    elif selected.get()==0:
        redoub="Non"
    a=0
    for i in range(len(get_st())):
        if get_st()[i][0]==name:
            a=1
    if a==1:
        confirmation = Toplevel()
        confirmation.geometry('260x100+700+300')
        b1 = Label(confirmation, text="ce eleve existe deja")
        b1.pack()
        Button(confirmation, text="OK", command=confirmation.destroy).pack()
    else:
        confirmation = Toplevel()
        confirmation.geometry('260x100+700+300')
        b1 = Label(confirmation, text="Ajout avec succes")
        b1.pack(ipady=15)
        Button(confirmation, text="OK", command=confirmation.destroy).pack()
        student=eleve(name,nt,redoub,txt)
        insert_student(student)
def modifications():
    def modif():
        name=entry1.get()
        nt=int(entry2.get())
        txt=texte.get("1.0", 'end-1c')
        if selected.get()==1:
            redoub="Oui"
        elif selected.get()==0:
            redoub="Non"
        student=eleve(name,nt,redoub,txt)
        a=0
        for i in range(len(get_st())):
            if get_st()[i][0]==student.nom:
                a=1
        if a==1:
            update_note(student,nt,redoub,txt)
            confirmation = Toplevel()
            confirmation.geometry('260x100+700+300')
            b1 = Label(confirmation, text="Bien modifier")
            b1.pack(ipady=15)
            Button(confirmation, text="OK", command=confirmation.destroy).pack()
        else:
            update_note(student,nt,redoub,txt)
            confirmation = Toplevel()
            confirmation.geometry('260x100+700+300')
            b1 = Label(confirmation, text="Cet eleve n'existe pas")
            b1.pack(ipady=15)
            Button(confirmation, text="OK", command=confirmation.destroy).pack()

    subwindow = Toplevel()
    subwindow.geometry('440x560+400+40')
    subwindow.title("modification")
    #creation des textes explicatifs de chaque section
    lb1 = Label(subwindow,text="Nom et Prénom :")
    lb1.grid(row=0,column=0,padx=10, pady=15)
    lb2 = Label(subwindow,text="Note :")
    lb2.grid(row=2,column=0,padx=10, pady=15)
    lb3 = Label(subwindow,text="Redoublant :")
    lb3.grid(row=3,column=0,padx=10, pady=15)
    lb4 = Label(subwindow,text="Appreciation :")
    lb4.grid(row=4,column=0,padx=10, pady=15)
    #creation des inputs
    entry1=Entry(subwindow,width=40)
    entry1.grid(row=0,column=1,padx=10, pady=10,columnspan=2)
    entry2=Entry(subwindow,width=40)
    entry2.grid(row=2,column=1,padx=10, pady=10,columnspan=2)
    texte = Text(subwindow,height=20,width=30)
    texte.grid(row=4,column=1,columnspan=2,padx=10, pady=10)
    #creation des Radiobuttons
    selected = IntVar()
    w1 = Radiobutton(subwindow,text="Oui",value=1,variable=selected)
    w1.grid(row=3,column=1)
    w2 = Radiobutton(subwindow,text="Non",value=0,variable=selected)
    w2.grid(row=3,column=2)
    sub=Button(subwindow, text="Modifie", command=lambda : [modif(),subwindow.destroy()])
    sub.grid(row=6,column=1,columnspan=2,padx=10, pady=20)
    #configuration des colone
    subwindow.columnconfigure(0, weight=20)
    subwindow.columnconfigure(1, weight=1)
    subwindow.columnconfigure(2, weight=1)
def liste_note():
    # create d'une sub window
    liste = Toplevel()
    liste.geometry('500x570+400+40')
    T=get_st()
    height = len(T) +1
    width = 4
    b1 = Label(liste, text="Non et Prenom")
    b1.grid(row=0, column=0,padx=10, pady=10)
    b2 = Label(liste, text="Note")
    b2.grid(row=0, column=1,padx=10, pady=10)
    b3 = Label(liste, text="Redoublant")
    b3.grid(row=0, column=2,padx=10, pady=10)
    b4 = Label(liste, text="Appreciation")
    b4.grid(row=0, column=3,padx=10, pady=10)
    for i in range(1,height): #Rows
        for j in range(width): #Columns
            b = Label(liste, text=T[i-1][j])
            b.grid(row=i, column=j,padx=10, pady=10)
    B=Button(liste, text="Afficher les statistiques", command=lambda : [liste.destroy(),statistique()])
    a=350-height*10
    B.grid(row=height+1,column=1,columnspan=2,pady=a)
    liste.columnconfigure(0, weight=1)
    liste.columnconfigure(1, weight=1)
    liste.columnconfigure(2, weight=1)
    liste.columnconfigure(3, weight=1)

def dl():
    def rem():
        name = entr.get()
        a=0
        for i in range(len(get_st())):
            if get_st()[i][0]==name:
                a=1
                break
        if a==1:
            st=eleve(get_st()[i][0],get_st()[i][1],get_st()[i][2],get_st()[i][3])
            remove_st(st)
            confirmation = Toplevel()
            confirmation.geometry('260x100+700+300')
            b1 = Label(confirmation, text="Bien supprimer")
            b1.pack(ipady=15)
            Button(confirmation, text="OK", command=confirmation.destroy).pack()
        else:
            confirmation = Toplevel()
            confirmation.geometry('260x100+700+300')
            b1 = Label(confirmation, text="Cet eleve n'existe pas")
            b1.pack(ipady=15)
            Button(confirmation, text="OK", command=confirmation.destroy).pack()
    delet = Toplevel()
    delet.geometry('460x100+400+40')
    lb1 = Label(delet,text="Nom et Prénom :")
    lb1.grid(row=0,column=0,padx=10, pady=15)
    entr = Entry(delet,width=40)
    entr.grid(row=0,column=1,padx=10, pady=10,columnspan=2)
    sub=Button(delet, text="Supprimer", command=lambda : [rem(), delet.destroy()])
    sub.grid(row=3,column=1,padx=10, pady=10)
    delet.columnconfigure(0, weight=1)
    delet.columnconfigure(1, weight=1)
    delet.columnconfigure(2, weight=1)
#creation de la fenetere
mainwindow = Tk()
mainwindow.geometry('440x560+400+40')
mainwindow.title("Application de gestion des notes")
#creation des textes explicatifs de chaque section
lb1 = Label(mainwindow,text="Nom et Prénom :")
lb1.grid(row=0,column=0,padx=10, pady=15)
lb2 = Label(mainwindow,text="Note :")
lb2.grid(row=2,column=0,padx=10, pady=15)
lb3 = Label(mainwindow,text="Redoublant :")
lb3.grid(row=3,column=0,padx=10, pady=15)
lb4 = Label(mainwindow,text="Appreciation :")
lb4.grid(row=4,column=0,padx=10, pady=15)
#creation des inputs
entry1=Entry(mainwindow,width=40)
entry1.grid(row=0,column=1,padx=10, pady=10,columnspan=2)
entry2=Entry(mainwindow,width=40)
entry2.grid(row=2,column=1,padx=10, pady=10,columnspan=2)
texte = Text(mainwindow,height=20,width=30)
texte.grid(row=4,column=1,columnspan=2,padx=10, pady=10)
#creation des Radiobuttons
selected = IntVar()
w1 = Radiobutton(mainwindow,text="Oui",value=1,variable=selected)
w1.grid(row=3,column=1)
w2 = Radiobutton(mainwindow,text="Non",value=0,variable=selected)
w2.grid(row=3,column=2)
#creation des Buttons normals
bt1=Button(mainwindow,text="liste des notes",command=liste_note)
bt1.grid(row=5,column=1,padx=10, pady=10)
bt2=Button(mainwindow,text="ajouter",command=ajouter)
bt2.grid(row=5,column=2,padx=10, pady=10)
#ajoute d'un menu pour la modification et la supression:
menu = Menu(mainwindow)
new_item = Menu(menu)
new_item.add_command(label='Modifier une Note', command=modifications)
new_item.add_separator()
new_item.add_command(label='Supprimer un eleve', command=dl)
menu.add_cascade(label='File', menu=new_item)
mainwindow.config(menu=menu)
#configuration des colone
mainwindow.columnconfigure(0, weight=20)
mainwindow.columnconfigure(1, weight=1)
mainwindow.columnconfigure(2, weight=1)
mainwindow.mainloop()

# coding=utf-8
import sqlite3
from mod import *

conn = sqlite3.connect('note.db')

c = conn.cursor()
try:
    c.execute("""CREATE TABLE eleve (
            nom text,
            note float,
            Redoublant text,
            Appreciation text,
            PRIMARY KEY("nom")
            )""")
except sqlite3.OperationalError:
    pass

def insert_student(st):
    with conn:
        c.execute("INSERT INTO eleve VALUES (:nom, :note, :Redoublant,:Appreciation)", {'nom': st.nom, 'note': st.note, 'Redoublant': st.Redoublant,'Appreciation':st.Appreciation})

def get_st():
    c.execute("SELECT * FROM eleve")
    return c.fetchall()


def update_note(st, note,Redoublant,Appreciation):
    with conn:
        c.execute("""UPDATE eleve SET note = :note ,Redoublant = :Redoublant,Appreciation= :Appreciation
                    WHERE nom = :nom """,
                  {'nom': st.nom,'note': st.note,'Appreciation' : st.Appreciation,'Redoublant':st.Redoublant})


def remove_st(st):
    with conn:
        c.execute("DELETE from eleve WHERE nom = :nom ",
        {'nom': st.nom})

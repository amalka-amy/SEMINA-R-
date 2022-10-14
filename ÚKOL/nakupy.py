
import sqlite3

class SQLite(object):
     ### konstruktor
    def __init__(self, filename):
        self.filename = filename
        self.connection =  sqlite3.connect(filename)
        self.cursor = self.connection.cursor()

    def sql(self, query, data=None):
        if data == None:
            self.cursor.execute(query)  
        else:
            self.cursor.execute(query, data)
        self.connection.commit()
        return self.cursor
        
    def delete(self):
        self.connection.close()

def menu():   
    print(" 'z' - pro zobrazení")
    print(" 'p' - pro přidáni")
    print(" 's' - pro smazání položky")
    print(" 'k' - pro konec")

    vyber = input("Vyber akci: ")
    return vyber

def pridat():
    co = input("Zadej věc: ")
    kolik = input("Zadej pocet: ")
    jcena = input("Zadej cenu za jednotku: ")
    poznamka = input("Poznamka: ")

    koupit = (co, kolik, jcena, poznamka)

    databaze.sql("INSERT INTO nakupy (co, kolik, jcena, poznamka) VALUES (?,?,?,?);", koupit)

def zobrazit():
    kurzor = databaze.sql("SELECT co, kolik, jcena, poznamka, ID FROM nakupy;")
    koupit = 1
    celek = kurzor.fetchall()
    for koupit in celek:
        co, kolik, jcena, poznamka, id = koupit
        print(id, co, kolik, jcena, poznamka) 

def smazat():
    id_smazat = input("Zadej ID: ")
    databaze.sql("DELETE FROM nakupy WHERE ID = ?;", id_smazat)

### 1. OTEVRENI SPOJENI
databaze = SQLite("nakupy.db")
vyber = menu()

while vyber != 0:
    if vyber == "z":
        zobrazit()
        vyber = menu()
    elif vyber == "p":
        pridat()
        vyber = menu()
    elif vyber == "k":
        databaze.delete()
        vyber = 0
    elif vyber == "s":
        smazat()
        vyber = menu()
    else:
        print("Jiné příkazy zatím neumím")
        vyber = menu()















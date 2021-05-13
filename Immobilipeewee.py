import sqlite3
import peewee

#conn = sqlite3.connect('Agenzia.db')
#conn.execute('CREATE TABLE immobile (immobileid INTEGER PRIMARY KEY, rifprop, indirizzo, prezzo, catalogo)')
#conn.execute('CREATE TABLE Catalogo (catalogoid INTEGER PRIMARY KEY, nome, prezzomin, prezzomax)')


class Catalogo():

    def __init__(self,nome,prezzomin,prezzomax):
        self.nome = nome
        self.prezzomin = prezzomin
        self.prezzomax = prezzomax
        self.Lista = []

    def inserisci(self, immobile):
        self.Lista.append(immobile)
        print("L'immobile è stato inserito con successo!\n")


class Immobile():
    
    def __init__(self, rifprop, indirizzo, prezzo, catalogo):
        self.rifprop = rifprop
        self.indirizzo = indirizzo
        self.prezzo = prezzo
        self.catalogo = catalogo
 
    def inserimento(self, lista, catalogo):
        conn.execute('INSERT INTO immobile (rifprop, indirizzo, prezzo, catalogo) values (?,?,?,?)', (self.rifprop,self.indirizzo,self.prezzo,self.catalogo))
        lista.append(self)
        catalogo.Lista.append(self)

        print("L'immobile è stato inserito con successo!\n")


    def modifica(self):
        print("---------------Modifica---------------")
        print("(Lascia vuoto se non vuoi modificare)\n")
        mrifprop = str(input("Inserisci il nuovo riferimento proprietario: "))
        if mrifprop != "":
            self.rifprop = mrifprop
        
        mindirizzo = str(input("Inserisci il nuovo indirizzo: "))
        if mindirizzo != "":
            self.indirizzo = mindirizzo
        
        mprezzo = str(input("Inserisci il nuovo prezzo: "))
        if mprezzo != "":
            self.prezzo = mprezzo
    
    def cancellazione(self, lista):
        lista.remove(self)
        print("L'immobile è stato rimosso con successo!\n")

    def stampa(self):
        print("Riferimento Proprietario: %s \nIndirizzo: %s \nPrezzo: %s"%(self.rifprop, self.indirizzo, self.prezzo))



#--------------MAIN---------------------

ListaImmobili = []

#Creazione Cataloghi e Immobili
Di_Prestigio = Catalogo("di prestigio","1000","4000")
Casa_Vacanza = Catalogo("Casa Vacanza","500","700")
Popolari = Catalogo("Casa","100","500")
myImmobile = Immobile("Mario Rossi","Via Roma 5","1000","Di_Prestigio")
myImmobile2 = Immobile("Luigi Verde","Via Milano 30","300","Popolari")


#Prova funzioni
myImmobile.inserimento(ListaImmobili,Di_Prestigio)
myImmobile2.inserimento(ListaImmobili,Popolari)
myImmobile.modifica()
myImmobile.cancellazione(ListaImmobili)

#ricerca
RicIndirizzo = str(input("Quale indirizzo vuoi ricercare? "))
for im in ListaImmobili:
    if im.indirizzo == RicIndirizzo:
        im.stampa()


#stampa
for im in ListaImmobili:
    im.stampa()


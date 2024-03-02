import os

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Product:
    def __init__(self, root) -> None:
        self.root = root

        #Produit_frame = Frame(self.root, relief=RIDGE, bg="")


        ### En tête de la page
        ## Title
        self.title = Label(self.root, text="Gestion de produits", font=("times new roman", 13, "bold"), fg="#0064d3", bg="#eff5f6")
        #self.title.grid(row=0, column=0, columnspan=2, pady=())
        
        ## Buttons de titre de page
        self.ajouterProduit = Button(self.root, text="Ajouter un produit",  bg="#32cf8e", font=("times new roman", 13), bd=0, fg="white", cursor="hand2", activebackground="#32cd8e")
        self.ajouterProduit.place(x=1100, y=90)

        ### Corps de la page
        self.corps = Frame(self.root, bg="#ffffff", bd=2)
        self.corps.place(x=300, y=150, width=1040, height=350)

        ## Faire le tableau de donnees
        TableauProduit(self.corps)

class TableauProduit:
    def __init__(self, frame, data = []):
        self.frame = frame
        
        ## Table heading and creation
        self.column = ("Code", "Nom", "Categorie", "Prix Unitaire", "Quantite", "Actions")
        self.tableau = ttk.Treeview(self.frame, columns=self.column)
        self.tableau.heading("#0", text="Code")
        self.tableau.heading("#1", text="Nom")
        self.tableau.heading("#2", text="Categorie")
        self.tableau.heading("#3", text="Prix Unitaire")
        self.tableau.heading("#4", text="Quantite")
        self.tableau.heading("#5", text="Actions")

        ## Création du tableau
        # for produit in data:
        #     self.ajouter_entree(produit["ProduxtCode"], produit["ProductName"], produit["ProductCategory"], produit[""])

        

        ## Ajout de quelques données
        self.ajouter_entree("001", "Cahier 50 pages", "Scolaire", 100, 50)
        self.ajouter_entree("002", "Cahier 50 pages", "Scolaire", 100, 50)
        self.ajouter_entree("003", "Cahier 50 pages", "Scolaire", 100, 50)
        self.ajouter_entree("004", "Cahier 50 pages", "Scolaire", 100, 50)
        self.ajouter_entree("005", "Cahier 50 pages", "Scolaire", 100, 50)

        # Affichage du tableau
        self.tableau.pack(pady=20)

    def ajouter_entree(self, code, nom, categorie, prix, Qte):
        self.tableau.insert("", "end", values=(nom, categorie, prix, Qte, "action"), iid=code, text=code)

    def remplir_tableau(self, data, init: BooleanVar):
        if (init) :
            self.tableau.delete(*self.tableau.get_children())
        
        for entry in data:
            self.ajouter_entree(entry["ProductCode"], entry["ProductName"], entry["ProductCategory"], entry["ProductPrice"], entry["ProductQuantity"])

        

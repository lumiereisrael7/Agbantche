import os

from tkinter import *
from PIL import Image, ImageTk

#os.chdir('./frontend')

class Bar:
    def __init__(self, root, title) -> None:
        self.root = root
        self.root.title("Qui Soli Deo Shop")
        self.root.geometry("1366x768")
        self.root.config(bg="#eff5f6")

        icon = PhotoImage(file=os.path.abspath('assets/logo.png'))
        self.root.iconphoto(True, icon)

        ### En tête
        self.entete = Frame(self.root, bg="#009df4")
        self.entete.place(x=250, y=0, width=1200, height=60)
        self.logout = Button(self.entete, text="Deconnecter", bg="#32cf8e", font=("times new roman", 13), bd=0, fg="white", cursor="hand2",activebackground="#32cd8e")
        self.logout.place(x=950, y=15)

        ### Menu 
        self.FrameMenu = Frame(self.root, bg="#ffffff")
        self.FrameMenu.place(x=0, y=0, width=250, height=750)

        original_image = Image.open('assets/logo.png')
        resized_image = self.resize_image(original_image, (170, 170))
        image = ImageTk.PhotoImage(resized_image)
        self.logo = Label(self.FrameMenu, image=image, bg="#ffffff")
        self.logo.image = image
        self.logo.place(x=30, y=30)

        self.Nom = Label(self.FrameMenu, text=title, bg="#ffffff", font=("times new roman", 13, "bold"))
        self.Nom.place(x=70, y=220)

        ### Tableau de bord
        # Mes produits
        original_image = Image.open('assets/prod1.png')
        resized_image = self.resize_image(original_image, (30, 30))
        image = ImageTk.PhotoImage(resized_image)
        self.produit = Label(self.FrameMenu, image=image, bg="#ffffff")
        self.produit.image = image
        self.produit.place(x=35, y=300)

        self.produit_text = Button(self.FrameMenu, text="Mes Produits", bg="#ffffff", font=("times new roman", 13, "bold"), bd=0, cursor="hand2", activebackground="#eff5f6")
        self.produit_text.place(x=90, y=304)

        # Mon stock
        original_image = Image.open('assets/stock1.png')
        resized_image = self.resize_image(original_image, (30, 30))
        image = ImageTk.PhotoImage(resized_image)
        self.stock = Label(self.FrameMenu, image=image, bg="#ffffff")
        self.stock.image = image
        self.stock.place(x=35, y=350)

        self.stock_text = Button(self.FrameMenu, text="Mon Stock", bg="#ffffff", font=("times new roman", 13, "bold"), bd=0, cursor="hand2", activebackground="#eff5f6")
        self.stock_text.place(x=90, y=354)

        # Vente
        original_image = Image.open('assets/vendre.png')
        resized_image = self.resize_image(original_image, (35, 35))
        image = ImageTk.PhotoImage(resized_image)
        self.vente = Label(self.FrameMenu, image=image, bg="#ffffff")
        self.vente.image = image
        self.vente.place(x=33, y=400)

        self.vente_text = Button(self.FrameMenu, text="Vendre", bg="#ffffff", font=("times new roman", 13, "bold"), bd=0, cursor="hand2", activebackground="#eff5f6")
        self.vente_text.place(x=90, y=404)

        ## Footer
        self.copyright_label = Label(self.FrameMenu, text="© LISE GLB Tech", font=("Arial", 8), bg="#35374b", fg="#eff5f6", justify="left")
        self.copyright_label.pack(pady=20, side="bottom", fill="x")

    def resize_image(self, image, size):
        resized_image = image.resize(size)
        return resized_image

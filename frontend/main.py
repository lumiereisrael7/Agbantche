import os

from tkinter import *

from component.bar import Bar
from views.product import Product

os.chdir('./frontend')

root = Tk()
Bar(root, "Qui Soli Deo")
Product(root)
root.mainloop()

import tkinter as tk

def show_developer_info():
    developer_info.config(text="Développeur: John Doe\nEmail: john.doe@example.com\nTéléphone: 123-456-7890")

# Créer la fenêtre principale
root = tk.Tk()
root.title("Exemple Footer avec Coordonnées du Développeur")

# Créer le contenu de la fenêtre
content_frame = tk.Frame(root, padx=10, pady=10)
content_frame.pack()

# Ajouter le contenu principal ici
# (par exemple, des boutons, des entrées, etc.)

# Créer un Frame pour le footer
footer_frame = tk.Frame(root, bg="#e0e0e0", padx=10, pady=5)
footer_frame.pack(side="bottom", fill="x")

# Bouton pour afficher les informations du développeur
developer_button = tk.Button(footer_frame, text="Afficher Coordonnées du Développeur", command=show_developer_info)
developer_button.pack()

# Étiquette pour afficher les informations du développeur
developer_info = tk.Label(footer_frame, text="", bg="#e0e0e0", font=("Arial", 10))
developer_info.pack()

# Démarrer la boucle principale
root.mainloop()

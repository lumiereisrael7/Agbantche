project-root/
│
├── backend/
│   ├── main.py            # Point d'entrée du backend (FastAPI)
│   ├── api/
│   │   ├── __init__.py    # Package pour les routes API
│   │   ├── stock.py       # Module pour les routes liées à la gestion de stock
│   │   └── auth.py        # Module pour les routes liées à l'authentification
│   │
│   ├── models/
│   │   ├── __init__.py    # Package pour les modèles de données
│   │   └── stock.py       # Module pour les modèles liés à la gestion de stock
│   │
│   └── database/
│       ├── __init__.py    # Initialisation de la base de données
│       └── crud.py        # Opérations CRUD sur la base de données
│
└── frontend/
    ├── main.py            # Point d'entrée du frontend (Tkinter)
    ├── views/
    │   ├── __init__.py    # Package pour les vues Tkinter
    │   └── stock.py       # Module pour la gestion de stock avec Tkinter
    │
    ├── controllers/
    │   ├── __init__.py    # Package pour les contrôleurs Tkinter
    │   └── stock.py       # Module pour les contrôleurs liés à la gestion de stock
    │
    └── assets/            # Dossier pour les fichiers statiques (images, etc.)
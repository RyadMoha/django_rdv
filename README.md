# 🛋️ Le Divan – Application de Prise de Rendez-vous

Une application Django pour permettre à des clients de prendre facilement des rendez-vous avec leur coach, et aux coachs de gérer leurs créneaux disponibles.

## ✨ Fonctionnalités

- ✅ Inscription / Connexion / Déconnexion  
- 📅 Prise de rendez-vous (avec choix de l'heure)  
- 📂 Tableau de bord personnel  
- 👥 Espace coach avec liste des réservations  
- ⛔ Créneaux déjà réservés masqués automatiquement  
- 🧾 Affichage des descriptions et noms des clients  
- 🎨 Design personnalisable (CSS)  

## 🛠️ Technologies utilisées

- Python 3.13+  
- Django 5.2+  
- SQLite (par défaut)  
- HTML + CSS  
- Bootstrap (optionnel)

## 🚀 Installation locale

## 1. Cloner le projet

```bash
git clone https://github.com/ton-utilisateur/le-divan.git
cd le-divan
```

## 2. Créer un environnement virtuel

```bash
python -m venv .venv
source .venv/bin/activate  # Windows : .venv\Scripts\activate
```

## 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

## 4. Appliquer les migrations

```bash
python manage.py migrate
```

## 5. Créer un superutilisateur

```bash
python manage.py createsuperuser
```

## 6. Lancer le serveur

```bash
python manage.py runserver
```

## 7. Accéder à l’application

- [http://127.0.0.1:8000/](http://127.0.0.1:8000/) → site  
- [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) → interface admin

## 📁 Arborescence simplifiée

```
le-divan/
├── rdv/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── templates/rdv/
│       ├── prise_rdv.html
│       ├── dashboard.html
│       └── coach_reservations.html
├── static/
│   └── css/
│       └── main.css
├── templates/
│   └── base.html
├── db.sqlite3
├── manage.py
└── README.md
```

## 📄 Licence

Ce projet est sous licence **MIT** — vous êtes libre de le réutiliser, modifier et redistribuer.

---

> *Projet réalisé dans le cadre d’un apprentissage Django personnel.*

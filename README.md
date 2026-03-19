# 🖊️ Des Écrits et des Non-Écrits — Blog Django

**A few words and many silences.**

## Installation

### 1. Prérequis
- Python 3.10+
- pip

### 2. Créer un environnement virtuel
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 4. Initialiser la base de données
```bash
python manage.py migrate
```

### 5. Créer un compte administrateur
```bash
python manage.py createsuperuser
# Entrez votre nom d'utilisateur, email et mot de passe
```

### 6. Lancer le serveur
```bash
python manage.py runserver
```

### 7. Accéder au blog
- **Blog** → http://127.0.0.1:8000/
- **Administration** → http://127.0.0.1:8000/admin/

---

## Structure du projet

```
descrits/
├── manage.py
├── requirements.txt
├── db.sqlite3          (créé automatiquement)
├── media/              (créé automatiquement — vos images)
├── descrits/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── blog/
    ├── models.py       — Post, Comment
    ├── views.py        — Pages
    ├── urls.py         — Routes
    ├── admin.py        — Interface admin
    ├── templates/blog/
    │   ├── base.html
    │   ├── home.html
    │   ├── category.html
    │   ├── post_detail.html
    │   └── about.html
    └── static/blog/
        ├── css/style.css
        └── js/main.js
```

---

## Créer du contenu (via l'administration)

1. Allez sur http://127.0.0.1:8000/admin/
2. Connectez-vous avec vos identifiants
3. Cliquez sur **"Articles"** → **"Ajouter un article"**
4. Remplissez :
   - **Titre** : le titre de l'article / livre
   - **Catégorie** : Carnet de Lecture / Fiction & Confidences / Pensées en vrac
   - **Auteur du livre** : (si résumé de livre)
   - **Note /5** : (si résumé de livre)
   - **Extrait** : résumé court affiché sur les cartes
   - **Contenu** : le texte complet (HTML accepté)
   - **Image de couverture** : optionnelle
   - **Publié** ✅ : cochez pour rendre visible

---

## Modération des commentaires

Les commentaires sont soumis à modération.
1. Admin → **Commentaires**
2. Cochez **"Approuvé"** pour les rendre visibles
3. Sauvegardez

---

## Traduction

La barre de traduction en haut de page utilise Google Translate.
Langues disponibles : Anglais, Espagnol, Arabe, Portugais.

---

## Déploiement (production)

Pour déployer en ligne (Heroku, Railway, PythonAnywhere, etc.) :
1. Changez `SECRET_KEY` dans settings.py (utilisez une variable d'environnement)
2. Mettez `DEBUG = False`
3. Configurez `ALLOWED_HOSTS` avec votre domaine
4. Utilisez WhiteNoise pour les fichiers statiques

---

*Créé avec ❤️ pour Aïva Vital — Des Écrits et des Non-Écrits*

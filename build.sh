#!/usr/bin/env bash


echo "📦  Installation des dépendances..."
pip install -r requirements.txt

echo "🔧  Création des migrations..."
python manage.py makemigrations blog


echo "📁  Collecte des fichiers statiques..."
python manage.py collectstatic --noinput --clear


echo "🗄️  Application des migrations..."
python manage.py migrate



echo "🌱  Chargement des données de démo..."
python manage.py seed_data

echo "✅  Build terminé !"

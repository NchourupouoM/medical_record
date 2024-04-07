# Titre du projet

Medical Record

# Description du projet

# Fonctionnalites

1. Authentification des utilisateurs ( patients et médecin ou infirmier).
   • créer un compte,
   • se connecter,
   • se déconnecter,
   • modifier ces informations.
2. Cas des patients.
   • Consulter leur antécédents médicales,
   • consulter leur ordonnances,
   • consulter leur résultats d’examen,
   • prendre le rendez-vous avec un professionnels de santé,
   • réceptions des notifications pour les rappels de rendez-vous, les résultats d’examen, etc.
   • telecharger le rapport médical. 3. Cas des professionnels médicales.
   • Consulter les dossier médicaux des patients dont il a la charge.
   • Prescription d’ordonnances aux patients,
   • suivi des patients ,
   • communication avec les patients,
   • planification des rendez-vous avec les patients,

# Prérequis

python 3...
Django==5.0.4

# Installation

1. clonner le depot github du projet : `git clone https://github.com/NchourupouoM/medical_record.git` puis `git pull origin main`
2. Installer l'environnement virtuel : `python -m venv env`
3. Activer l'environnement virtuel : `source env\bin\activate`
4. installer django : `pip install django`
5. effectuer des migrations : `python manage.py migrate`
6. Lancer l'application: `python manage.py runserver`

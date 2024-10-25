# health-calculator-service
Projet Python - health-calculator-service

# requirements.txt
# Ce fichier requirements.txt liste les dépendances nécessaires pour exécuter
# le microservice Health Calculator. Chaque dépendance est documentée pour 
# clarifier son rôle dans l'application.

# 1. Flask est le framework principal utilisé pour créer une application web
#    légère en Python qui gère des requêtes HTTP pour le calcul de BMI et BMR.
Flask==2.0.2

# 2. pytest est un framework de tests qui permet d'automatiser et de gérer les tests.
#    Il n'est pas strictement nécessaire si on utilise unittest, mais est utile pour les tests avancés.
# pytest==6.2.5

# 3. gunicorn est un serveur d'application WSGI pour exécuter des applications Flask
#    en production. Il n'est pas nécessaire pour le développement local.
# gunicorn==20.1.0

# 4. requests est une bibliothèque qui peut être utilisée pour envoyer des requêtes HTTP,
#    utile pour tester l'API en local, en envoyant des requêtes POST vers les endpoints.
# requests==2.26.0

# Structure des fichiers du projet :
# - app.py : Point d'entrée de l'application. Ce fichier initialise et configure
#   l'API Flask. Il expose deux endpoints :
#      - /bmi : calcule l'Indice de Masse Corporelle (IMC)
#      - /bmr : calcule le Métabolisme de Base (BMR)
#
# - health_utils.py : Ce fichier contient deux fonctions utilitaires:
#      - calculate_bmi : calcule l'IMC en utilisant le poids (kg) et la taille (m).
#      - calculate_bmr : calcule le BMR en utilisant la taille (cm), le poids (kg),
#        l'âge et le genre, en utilisant l'équation de Harris-Benedict.
#
# - test.py : Script de test unitaire pour vérifier les calculs d'IMC et BMR.
#      - test_calculate_bmi : vérifie la précision de la fonction calculate_bmi.
#      - test_calculate_bmr_male et test_calculate_bmr_female : vérifient la précision
#        de calculate_bmr pour les hommes et les femmes respectivement.
#
# - Dockerfile : Fichier qui définit les étapes de construction de l'image Docker
#   pour containeriser l'application. Il utilise l'image de base Python 3.9 et
#   installe les dépendances définies dans ce fichier requirements.txt.
#
# - Makefile : Fichier d'automatisation permettant de simplifier les commandes courantes :
#      - make init : installe les dépendances.
#      - make run : lance l'application Flask en mode local.
#      - make test : exécute les tests unitaires.
#      - make build : construit l'image Docker pour déployer l'application.
#
# - .github/workflows/ci-cd.yml : Fichier de workflow pour GitHub Actions qui
#   automatise le pipeline CI/CD, incluant :
#      - Installation des dépendances.
#      - Exécution des tests.
#      - Construction de l'image Docker.
#      - Déploiement sur Azure App Service.

# Notes :
# - Flask est essentiel pour cette application ; les autres dépendances peuvent être
#   ajoutées selon les besoins de développement, de test ou de production.
# - Si pytest ou gunicorn sont utilisés, n'oubliez pas de décommenter leur version
#   et de les inclure dans l'environnement de développement et de déploiement.

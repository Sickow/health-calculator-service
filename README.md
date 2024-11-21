#Health Calculator Service
Health Calculator Service est un microservice Python qui calcule des métriques de santé, telles que l'IMC (Indice de Masse Corporelle) et le MB (Métabolisme de Base), via une API REST. Ce projet est conteneurisé avec Docker, géré avec Makefile, et déployé sur Azure à l'aide d'une pipeline CI/CD GitHub Actions.

#Objectif
Créer un microservice performant et facilement déployable pour calculer :

IMC (BMI) : Poids (kg) / Taille (m)^2.
MB (BMR) : Calculé selon l'équation de Harris-Benedict.


#Fonctionnalités
Calculer l'IMC avec l'endpoint /bmi.
Calculer le MB avec l'endpoint /bmr.
Conteneurisation avec Docker.
Gestion automatisée des tâches (initialisation, test, build) via Makefile.
Pipeline CI/CD avec GitHub Actions.
Déploiement sur Azure App Service.


#Prérequis
Python 3.8 ou supérieur.
Docker.
Azure App Service pour le déploiement.


#Installation
Étapes de configuration
Clonez le dépôt :

    git clone <votre-url-github>
    cd health-calculator-service
    
Installez les dépendances :

    pip install -r requirements.txt
    
Conteneurisez l'application avec Docker :


    docker build -t health-calculator-service .

    
#API Endpoints
Calcul de l'IMC
Endpoint : /bmi
Méthode : POST
Payload :

    {
      "weight": 70,
      "height": 1.75
    }
    
Réponse :

    {
      "bmi": 22.86
    }
    
Calcul du MB
Endpoint : /bmr
Méthode : POST
Payload :

    {
      "weight": 70,
      "height": 175,
      "age": 25,
      "gender": "male"
    }
    
Réponse :

    {
      "bmr": 1706.69
    }
    
Tests
Exécutez les tests unitaires :

    python test.py
    
Exemple de Makefile pour automatiser les tâches :

    IMAGE_NAME=health-calculator-service
    PORT=5000

    .PHONY: init run test build clean

init:
    pip install -r requirements.txt

run:
    python app.py

test:
    python -m unittest discover

build:
    docker build -t $(IMAGE_NAME) .

    
#Déploiement
Sur Azure App Service
Créez une application web sur Azure App Service.
Ajoutez le profil de publication Azure en tant que secret AZURE_WEBAPP_PUBLISH_PROFILE sur GitHub.
Configurez un workflow GitHub Actions dans .github/workflows/ci-cd.yml.
Exemple de workflow GitHub Actions :


name: CI/CD Pipeline

on:
  push:
    branches:
      - main

jobs:
  build-test-deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: |
          make init

      - name: Run tests
        run: |
          make test

      - name: Build Docker image
        run: |
          make build

      - name: Deploy to Azure Web App
        uses: azure/webapps-deploy@v2
        with:
          app-name: 'health-calculator-app'
          publish-profile: ${{ secrets.AZURE_WEBAPP_PUBLISH_PROFILE }}
          
#Évaluation
Exactitude : Les endpoints /bmi et /bmr fournissent des résultats corrects.
Conteneurisation : L'application fonctionne correctement dans un conteneur Docker.
Automatisation : Les commandes Makefile exécutent les tâches nécessaires.
CI/CD : Le pipeline GitHub Actions teste et déploie automatiquement l'application.
Documentation : Le code et les commentaires sont clairs et bien organisés.

# Makefile

.PHONY: init run test build clean

# Commande pour installer les dépendances
init:
	@echo "Installing dependencies..."
	pip install -r requirements.txt

# Commande pour exécuter l’application Flask
run:
	@echo "Running the Flask app..."
	python3 app.py

# Commande pour lancer les tests
test:
	@echo "Running tests..."
	python3 -m unittest discover

# Commande pour construire l’image Docker
build:
	@echo "Building the Docker image..."
	docker build -t health-calculator-service .

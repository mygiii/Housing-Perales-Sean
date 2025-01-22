FROM python:3.12-slim

# Définir le répertoire de travail
WORKDIR /app

# Installer Poetry
RUN pip install poetry

# Copier les fichiers nécessaires pour installer les dépendances
COPY pyproject.toml poetry.lock ./

# Installer les dépendances
RUN poetry install --no-root

# Copier le reste de l'application
COPY . .

# Commande par défaut
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

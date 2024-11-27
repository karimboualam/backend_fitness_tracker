FROM python:3.11-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier uniquement les fichiers nécessaires pour installer les dépendances
COPY requirements.txt /app/

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste des fichiers du projet
COPY . /app/

# Exposer le port 8000
EXPOSE 8000

# Démarrer le serveur Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

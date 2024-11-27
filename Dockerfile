FROM python:3.11-slim

# Définir le répertoire de travail dans le container
WORKDIR /app

# Copier uniquement les fichiers nécessaires pour installer les dépendances
COPY requirements.txt /app/

# Installer les dépendances listées dans requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Installer des dépendances supplémentaires
RUN pip install django djangorestframework django-cors-headers

# Copier le reste des fichiers du projet
COPY . /app/

# Exposer le port 8000 pour Django
EXPOSE 8000

# Commande pour démarrer le serveur Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

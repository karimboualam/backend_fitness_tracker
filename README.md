# Fitness Tracker Platform

A comprehensive fitness tracking platform built with Django and Celery, providing a dashboard for tracking progress, exporting training reports, managing custom workout sessions, and sending notifications/reminders.

---

## Features

- **Interactive Dashboard**: Visualize user progress with intuitive charts.
- **Data Storage and Analysis**: Store and analyze user training data.
- **Training Report Export**: Export workout reports as PDFs.
- **Custom Workout Management**: Create, modify, and track user-specific workouts.
- **Automated Notifications**: Send reminders and motivational notifications.
- **Background Tasks**: Asynchronous task management using Celery with Redis.

---

## **Tech Stack**

### **Backend**
- Django (Python)
- Celery
- Redis (Message broker)

### **Frontend**
- ReactJS (future integration for a responsive UI)

### **Database**
- MongoDB (via Djongo)

### **Other Tools**
- Docker, Kubernetes (for deployment)
- Firebase (for push notifications)
- Stripe API (for payment integration)
- Flower (for Celery task monitoring)

---

## **Setup Instructions**

### 1. Clone the Repository
```bash
git clone https://github.com/karimboualam/fitness_tracker.git
cd fitness_tracker


2. Create and Activate a Virtual Environment

python -m venv venv
source venv/Scripts/activate  # On Windows
# OR
source venv/bin/activate      # On macOS/Linux

3. Install Dependencies

pip install -r requirements.txt


4. Configure the Environment
Create a .env file in the root directory.
Add necessary configurations (e.g., DATABASE_URL, REDIS_URL, etc.).

5. Run Migrations

python manage.py makemigrations
python manage.py migrate

6. Start the Development Server


python manage.py runserver

7. Start Celery Worker


celery -A fitness_tracker worker --loglevel=info --pool=solo

8. Monitor Tasks
Use Flower to monitor Celery tasks:

celery -A fitness_tracker flower
Visit Flower at http://localhost:5555.


How to Contribute
1. Fork the repository.
2. Create a new branch for your feature or bugfix:

    git checkout -b feature-name

3. Commit your changes:

    git commit -m "Add feature-name"

4. Push to your branch:

    git push origin feature-name
5. Open a pull request.

Contact
    For questions or suggestions, feel free to reach out:

        Email: karimboualam21@gmail.com
        GitHub: Karim Boualam
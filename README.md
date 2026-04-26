Django Starter Kit 🚀

A ready-to-use Django starter kit with system seeding, Redis, and Celery support for async tasks (like email templates).

📦 Installation Guide

1. Clone the repository: 
command: git clone https://github.com/raazr62/django_starter_kit.git

command: cd django_starter_kit

3. Create virtual environment: 

command: python -m venv venv

Firsy you need to Activate it:

Windows:
command: venv\Scripts\activate

Windows Powershell:
command: .\venv\Scripts\Activate.ps1

Windows CMD:
command: venv\Scripts\activate.bat

Mac/Linux
command: source venv/bin/activate

3. Install dependencies
command: pip install -r requirements.txt

5. Run database migrations: 
command: python manage.py migrate

7. Configure system seed data

Edit the seed configuration according to your project:

File directory: system_seed/seed_data.py

Update:
def seed_system_setting():
    ...
    
6. Seed initial data
command: python manage.py seed

8. Start Redis server
Make sure Redis is installed and running:

redis-server
8. Run Celery worker (for async tasks)

Used for background tasks like email sending:
command: celery -A project worker --loglevel=info --pool=solo

✉️ Features
Django base setup
System seeding support
Redis integration
Celery async task processing
Email template ready architecture

⚙️ Notes
- Ensure Redis is running before starting Celery
- Update project in Celery command if your Django project name differs
- Customize seed_system_setting() before running seed command

# Django Starter Kit 🚀

A ready-to-use Django starter kit with system seeding, Redis, and Celery support for async tasks (like email templates).

## 📦 Installation Guide

### 1. Clone the repository: 

```bash
git clone https://github.com/raazr62/django_starter_kit.git
cd django_starter_kit
```

### 2. Create virtual environment: 

```bash
python -m venv venv
```

#### Firsy you need to Activate it:

##### Windows:
```bash
venv\Scripts\activate
```

##### Windows Powershell:

```bash
.\venv\Scripts\Activate.ps1
```

##### Windows CMD:

```bash
venv\Scripts\activate.bat
```

##### Mac/Linux

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run database migrations: 

```bash
python manage.py migrate
```

### 5. Configure system seed data

Edit the seed configuration according to your project:

File directory: system_seed/seed_data.py

Update:
def seed_system_setting():
    ...
    
### 6. Seed initial data
```bash
command: python manage.py seed
```

### 7. Start Redis server
Make sure Redis is installed and running:

### Install Redis (Message Broker)

**Windows:**

1. Download Redis from: https://github.com/microsoftarchive/redis/releases
2. Or use Docker: `docker run -d -p 6379:6379 redis:alpine`
3. Or use WSL: `sudo apt install redis-server && redis-server`

**Mac:**

```bash
brew install redis
brew services start redis
```

**Linux:**

```bash
sudo apt install redis-server
sudo systemctl start redis
```


Used for background tasks like email sending:

```bash
celery -A project worker --loglevel=info --pool=solo
```

✉️ Features
- Django base setup
- Authentication
- Email template ready, architecture including OTP template
- Complete CMS
- In APP notification & Push Notification
- Stripe Subscription with admin dashboard refund approval
- Customize Admin Dashboard
- Contact Us section
- Terms and Privacy section
- Ready-made Postman collection
- System seeding support
- Redis integration
- Celery async task processing
- Conten Management System
- AWS S3 Setup

⚙️ Notes
- Ensure Redis is running before starting Celery
- Update project in Celery command if your Django project name differs
- Customize seed_system_setting() before running seed command

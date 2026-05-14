# Django Modular Monolith Example

This is a production-style modular monolith starter architecture using Django + PostgreSQL.

## Features
- Modular app structure
- PostgreSQL (Neon/Azure compatible)
- Django REST Framework
- Environment variable configuration

## Setup

### 1. Create virtual environment

```bash
python -m venv venv
```

Activate:

Windows:
```bash
venv\Scripts\activate
```

Linux/macOS:
```bash
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment

Rename:

```bash
.env.example -> .env
```

Fill in your Neon or Azure PostgreSQL credentials.

### 4. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start server

```bash
python manage.py runserver
```

## API Endpoints

Products:
```text
/api/products/
```

Orders:
```text
/api/orders/
```

## Example Neon Database URL

Host:
```text
ep-example.us-east-1.aws.neon.tech
```

SSL mode is already enabled in settings.py.

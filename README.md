# Paystack Payments API

A Django REST Framework API for initializing, verifying, and handling Paystack payment transactions.

## 🚀 Features

- Initialize Paystack payment transactions  
- Verify transaction status by reference  
- Handle Paystack webhook events  
- Auto-generated API documentation with Swagger and ReDoc

## 📥 Getting Started: Download & Run Locally

### Prerequisites

- Python 3.10+  
- pip  
- virtualenv (optional but recommended)  
- PostgreSQL or your preferred DB (adjust settings accordingly)

### Steps

**1. Clone the repo**

```bash
git clone https://github.com/yourusername/paystack-payments-api.git
cd paystack-payments-api
```

**2. Create & activate virtual environment**

```bash
python -m venv .venv
source .venv/bin/activate    # On Windows use `.venv\Scripts\activate`
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Configure environment variables**

Copy `.env.example` to `.env` and edit with your secrets.

```bash
cp .env.example .env
# Edit .env to add your DB credentials, PAYSTACK_SECRET_KEY, etc.
```

**5. Apply migrations**

```bash
python manage.py migrate
```

**6. Run development server**

```bash
python manage.py runserver
```

**7. Access API docs**

- Swagger UI: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)  
- ReDoc: [http://localhost:8000/redoc/](http://localhost:8000/redoc/)

## 🧪 Running Tests

Run the full test suite with:

```bash
python manage.py test
```

## ⚙️ CI/CD Pipeline & Deployment

- Automated pipeline runs tests and deploys on push to `main`.  
- Deployment environment variables:

  - `DJANGO_SECRET_KEY`  
  - `DATABASE_URL`  
  - `PAYSTACK_SECRET_KEY`  
  - `ALLOWED_HOSTS`

- Ensure webhook endpoint security in production.

## 🌐 Live Server URL

Access the live API here:

- Swagger UI: `https://api.yourdomain.com/swagger/`  
- ReDoc: `https://api.yourdomain.com/redoc/`  
- API root: `https://api.yourdomain.com/api/v1/`

## 📄 API Endpoints Overview

| Endpoint                   | Method | Description                  |
|----------------------------|--------|------------------------------|
| `/api/v1/payments/`         | POST   | Initialize a payment          |
| `/api/v1/payments/<ref>/`   | GET    | Verify payment by reference   |
| `/api/v1/payments/webhook/` | POST   | Paystack webhook callback     |

## 👩‍💻 Contributing

Feel free to fork and create PRs. Follow the code style and add tests for new features.

## 📞 Contact

For questions or issues, email paulmison@gmail.com

*Happy coding!* 🚀

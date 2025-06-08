# Paystack Payments API

A Django REST Framework API for initializing, verifying, and handling Paystack payment transactions.

# Live server available on Render at:
[https://https://mastercraft-stage2.onrender.com/api/v1/payments/<str:param>](https://https://mastercraft-stage2.onrender.com/api/v1/payments/<str:param>) 

## Admin panel at:
[https://https://mastercraft-stage2.onrender.com/admin](https://https://mastercraft-stage2.onrender.com/admin)
- User: admin, Password: 1234

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
git clone https://github.com/PaulImison/MasterCraft-Stage2.git
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

## .env.example

# Django secret key (generate your own for production)
- DJANGO_SECRET_KEY=your-secret-key

# PostgreSQL database URL (adjust user, password, db name, host, and port)
- DATABASE_URL=postgres://user:password@localhost:5432/payments_db

# Paystack secret key (from your Paystack dashboard)
- PAYSTACK_SECRET_KEY=sk_test_xxxxxxxxxxxxxxxxxxxxx

# Allowed hosts (comma-separated list)
- ALLOWED_HOSTS=localhost,127.0.0.1
    
## ✅ You should copy .env.example → .env in your project root:

```cp .env.example .env```

✅ Then edit .env with your real secrets:

- Use Django Secret Key Generator or similar to generate a secure DJANGO_SECRET_KEY.
- Add your real PAYSTACK_SECRET_KEY from Paystack dashboard.
- If using Docker or cloud deploy, update DATABASE_URL accordingly.

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

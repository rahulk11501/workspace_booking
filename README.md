# Workspace Booking API (Django + DRF)

## Overview

This project is a simplified Virtual Workspace Room Booking System built with Django and Django REST Framework. It supports booking, cancelling, and fetching rooms, following real-world constraints.

---

## Project Structure

```
workspace_booking/
├── config/                 # Django project settings
│   ├── settings.py
│   └── ...
├── core/                   # Main app
│   ├── __init__.py
│   ├── models/             # ORM models
│   ├── schemas/            # Pydantic schemas
│   ├── management/         # Management commands (seeds, etc.)
│   │   └── commands/
│   │       └── seed_data.py
│   └── tests/              # Tests, factories
├── manage.py
├── requirements.txt
├── Makefile                # Predefined commands for development & testing
└── README.md
```

---

## Tech Stack

* Python 3.12
* Django 5.1
* Django REST Framework
* Pydantic v2 (for data validation)
* SQLite (local development)
* pytest + pytest-django + factory_boy + Faker (testing)
* ruff (linting)

---

## Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/rahulk11501/workspace_booking.git
cd workspace_booking
```

2. **Create a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Run migrations:**

```bash
python manage.py migrate
```

5. **Run server locally:**

```bash
python manage.py runserver
```

6. **Optional: Use Makefile commands**

```bash
make install      # Install dependencies
make migrate      # Apply migrations
make run          # Start local server
make test         # Run all tests
```

---

## Seed Data

Populate the database with initial data (users, teams, rooms) using:

```bash
python manage.py seed_data
```

This command will create:

* **20 users** with random ages and genders
* **5 teams** with 3–5 members each
* **15 rooms**:

  * 8 Private Rooms (capacity = 1)
  * 4 Conference Rooms (capacity = 10)
  * 3 Shared Desks (capacity = 4)

> Note: Bookings are optional and can be added in `seed_data.py` if required. Teams and rooms are created with real IDs, so they can be used immediately for testing and bookings.

---

## Testing

1. **Run tests using pytest:**

```bash
pytest -v
```

2. **Test folder structure:**

```
core/tests/
├── factories/
│   └── user_factory.py
├── models/
│   └── test_user_model.py
└── schemas/
    └── test_user_schema.py
```

3. **pytest.ini configuration:**

```ini
[pytest]
DJANGO_SETTINGS_MODULE = config.settings
python_files = tests.py test_*.py *_tests.py
testpaths = core/tests
```

---

## Notes / Updates So Far

* Django project and `core` app created
* `settings.py` updated and server runs locally
* Pydantic models and schemas implemented
* Tests configured with `pytest` and Faker factories
* Code pushed to GitHub with migrations tracked

---

## Next Steps

* Implement REST API endpoints (Booking, Cancel, Available Rooms)
* Add Docker + docker-compose for local development
* Add API documentation (Swagger/OpenAPI)
* Implement concurrency-safe room booking logic

---

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests.

---

## License

This project does not currently have a license specified.

---

## About

No description, website, or topics provided.

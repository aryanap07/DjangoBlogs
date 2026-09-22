# My Blog

A simple blog built with Django. Posts are written from the admin panel and
shown on a paginated homepage, each with its own page at a clean, slug-based
URL.

## Features

- Homepage listing all posts, newest first, 5 per page
- Individual post pages with pretty URLs (`/post/my-post-title/`)
- Automatic, unique slug generation from the post title
- Django admin for creating and managing posts
- Custom 404 page for missing posts
- Configurable via environment variables for deployment

## Requirements

- Python 3.10+
- pip

## Setup

1. Clone the repository and move into the project folder:

   ```bash
   git clone <your-repo-url>
   cd blog
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Copy the example environment file and adjust it if needed:

   ```bash
   cp .env.example .env
   ```

5. Apply migrations:

   ```bash
   python manage.py migrate
   ```

6. Create an admin account:

   ```bash
   python manage.py createsuperuser
   ```

7. Run the development server:

   ```bash
   python manage.py runserver
   ```

8. Visit `http://127.0.0.1:8000/` for the blog and
   `http://127.0.0.1:8000/admin/` to write posts.

## Running tests

```bash
python manage.py test
```

## Deploying

Before going to production:

- Set `DJANGO_SECRET_KEY` to a new, secret value.
- Set `DJANGO_DEBUG=False`.
- Set `DJANGO_ALLOWED_HOSTS` to your real domain(s).
- Run `python manage.py collectstatic` to gather static files into
  `STATIC_ROOT`, and serve them with your web server or a tool such as
  WhiteNoise.
- Use a production-grade database (e.g. PostgreSQL) instead of SQLite if you
  expect concurrent writers.
- Run the app behind a WSGI server such as Gunicorn, with a reverse proxy
  (e.g. Nginx) in front of it.

## Project structure

```
blog/
├── blog/            # Project settings and root URL configuration
├── posts/           # The blog app: models, views, admin, tests
├── templates/        # HTML templates
├── static/css/       # Stylesheet
└── manage.py
```

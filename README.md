# TechTrendy

A simple Django-based e-commerce learning project (shopping demo).

## Features
- Product listing with categories, offers and trending badges
- Add to cart, update/remove cart items
- Product detail page
- User authentication (register, login, profile, reset password)
- Admin for adding products

## Quickstart (Windows)
1. Clone repository
   ```powershell
   git clone https://github.com/rakesh0709/django-TechTrendy.git
   cd django-TechTrendy
   ```
2. Create and activate virtual environment
   ```powershell
   python -m venv myenv
   myenv\Scripts\Activate.ps1
   ```
3. Install dependencies
   ```powershell
   pip install -r requirements.txt
   ```
   If `requirements.txt` is missing, create it from your environment: `pip freeze > requirements.txt`.

4. Configure environment
   - Copy `.env.example` to `.env` (if you use env files) and set `SECRET_KEY`, `DEBUG`, DB settings, etc.
   - The project uses Django's default SQLite (`db.sqlite3`) by default. Do NOT commit secrets.

5. Migrate and create superuser
   ```powershell
   python manage.py migrate
   python manage.py createsuperuser
   ```

6. Run the dev server
   ```powershell
   python manage.py runserver
   ```

7. Open http://127.0.0.1:8000/ and http://127.0.0.1:8000/admin/ (admin user created above)

## Media & Static files
- Development: media files served from `MEDIA_URL` and `MEDIA_ROOT` configured in `settings.py`.
- In production run `python manage.py collectstatic` and configure your web server to serve static and media files.

## Tests
- No automated tests included yet. Add tests under each app's `tests.py` or a `tests/` package.

## Contributing
- Create a branch `feature/your-feature` and open a PR to `main`.
- Follow PEP8 and write tests where appropriate.

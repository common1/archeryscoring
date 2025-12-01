# archeryscoring

## See also

 [https://docs.wagtail.org/en/stable/getting_started/tutorial.html]

## Chapter 001 - Initial commit, empty Wagtail site

```bash
python -m venv .venv
pip install wagtail
wagtail start scoring .
```

## Chapter 001 - Users app created

```bash
python manage.py startapp users
# Create User model in users.models.py
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
Username: admin
Email address: me@admin.com
Password: changeme
```


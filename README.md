# archeryscoring

## See also

 [https://docs.wagtail.org/en/stable/getting_started/tutorial.html]

## Chapter 001 - Initial commit, empty Wagtail site

```bash
python -m venv .venv
pip install wagtail
wagtail start scoring .
```

## Chapter 002 - Users app created

```bash
# Create users app
python manage.py startapp users
# Add users app to INSTALLED_APPS in base.py
# Create User model in users.models.py
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
Username: admin
Email address: me@admin.com
Password: changeme
```

## Chapter 003 - api app created

```bash
# Create api app
python manage.py startapp api
# Add api app to INSTALLED_APPS in base.py
```

# Chapter 004 - Implementation of BaseModel and ArcherModel in api/models.py

```bash
python manage.py makemigrations
python manage.py migrate
```


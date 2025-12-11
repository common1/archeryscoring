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

## Chapter 004 - Implementation of BaseModel and ArcherModel in api/models.py

[https://wagtail-modeladmin.readthedocs.io/en/latest/usage.html]
[https://docs.wagtail.org/en/latest/advanced_topics/icons.html]

```bash
python manage.py makemigrations
python manage.py migrate
pip install wagtail-modeladmin
```

## Chapter 005 - Create app modeling with models BaseModel, Archer, Clubs, ClubMembership

[https://docs.wagtail.org/en/v2.13.1/reference/contrib/modeladmin/indexview.html]

```bash
```

## Chapter 006 - modeling app, Create models Category and CategoryMembership

```bash
```

## Chapter 007 - modeling app, Create models

```
Models created
Team
TeamMembership
ScoringSheet
```

```bash
```

## Chapter 008 - modeling app add classes to admin.py and wagtail_hooks.py

```
admin.py
class TeamMembershipInline
class TeamAdmin
class TeamMembershipAdmin

wagtail_hooks.py
class TeamAdminWagtailHook
class TeamMembershipAdminWagtailHook
```

```bash
```

## Chapter 009 - modeling app wagtail_hooks.py

```
Hook added to class names
A lot of classes defined
Implementation follows
```

```bash
```

## Chapter 010 - modelling app and archery_materials app

```
```

```bash
```

## Chapter 011 - modelling app and archery_materials app - Add Discipline classes

```
modeling/models.py
class Discipline
class DisciplineMembership

modeling/admin.py
class TeamMembershipInline
class TeamAdmin
class TeamMembershipAdmin

modeling/wagtail_hooks.py
class DisciplineHook
class DisciplineMembershipHook
```

```bash
```

## Chapter 012 - Define a ModelAdminGroup to group all the modeling related admin views

```
modeling\wagtail_hooks.py
```

```bash
```

## Chapter 013 - Create fill_db app - Fill database with default values

```
fill_db\management\commands\fill_db.py
Create sample archers
Create sample clubs
Create sample clubmemberships
Create sample catergories
Create sample categorymemberships
Create sample disciplines
Create sample disciplinememberships
```

```bash
python manage.py startapp fill_db
python manage.py fill_db
```

## Chapter 014 - Migrating from ModelAdmin to Snippets

```
Convert from ModelAdmin to ModelAdminGroup
```

```bash
pip install pyclean
pyclean .
```

## Chapter 015 - fill database

```
...
Part 1
def create_disciplines
Discipline objects defined
Part 2
Discipline objects created
Part 3
def create_sample_archers adjusted(self)
def create_sample_clubs adjusted(self)
def create_sample_club_memberships(self)
def create_sample_disciplines(self)
def create_sample_discipline_memberships(self)
def create_sample_categories(self)
def create_sample_category_memberships(self)
def create_sample_teams(self)
def create_sample_team_memberships(self)
def create_sample_scoringsheets(self)
```

```bash
del db.sqlite3
pyclean .
python manage.py migrate
python manage.py fill_db
```

## Chapter 016 - extend modeling.models

See also:
[https://dev.to/atifwattoo/how-to-create-an-image-model-in-django-with-settings-1le3]

```
Part 1
class TargetDiameters(BaseModel)
class TargetFace(BaseModel)
class Contest(BaseModel)
class ContestMembership(BaseModel)
class Score(BaseModel)
class ScoreMembership(BaseModel)
class Competition(BaseModel)
class CompetitionMembership(BaseModel)
Part 2
Apps: archery_materials, modeling 
Moving panels sections from all models in models.py to admin.py
```

```bash
```


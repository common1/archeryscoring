import random
from decimal import Decimal

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from users.models import User
from django.utils import lorem_ipsum
from modeling.models import (
    Archer, 
    Club,
    ClubMembership,
    Discipline,
    DisciplineMembership,
    Category,
    CategoryMembership,
    Team,
    TeamMembership,
)

SCREEN_OUTPUT = True

class Command(BaseCommand):
    help = 'Populate the database with sample data'
    
    def handle(self, *args, **kwargs):
        # get or create superuser
        user = User.objects.filter(username='admin').first()
        if not user:
            user = User.objects.create_superuser(username='admin', password='changeme', email='me@mail.com')
        if SCREEN_OUTPUT:
            self.stdout.write(self.style.SUCCESS('Superuser "admin" ensured.'))

        # Create sample Archers        
        archers = [
            Archer(
                author=user,
                first_name="Harrie",
                last_name="Smulders",
            ),
            Archer(
                author=user,
                first_name="Piet",
                last_name="Jansen",
            ),
            Archer(
                author=user,
                first_name="Peter",
                last_name="Vanalles",
            ),
        ]
        for _archer in archers:
            # Get or create archer
            archer, created = Archer.objects.get_or_create(
                first_name=_archer.first_name,
                last_name=_archer.last_name,
                defaults={
                    'author': _archer.author,
                }
            )
            if SCREEN_OUTPUT:
                self.stdout.write(self.style.SUCCESS(f'Archer "{archer.first_name} {archer.last_name}" {"created" if created else "already exists"}'))
        # Get all archers
        archers = Archer.objects.all()
        
        # Create sample clubs
        clubs = [
            Club(
                name="De Boogschutters", 
                town="Eindhoven", 
                info=lorem_ipsum.paragraph()
            ),
            Club(
                name="De Pijlen", 
                town="Veldhoven", 
                info=lorem_ipsum.paragraph()
            ),
            Club(
                name="De Schutters", 
                town="Breda", 
                info=lorem_ipsum.paragraph()
            ),
            Club(
                name="De Pijl", 
                town="Tilburg", 
                info=lorem_ipsum.paragraph()
            ),
            Club(
                name="De Boog", 
                town="Den Bosch", 
                info=lorem_ipsum.paragraph()
            ),
        ]
        for _club in clubs:
            # Get or create club
            club, created = Club.objects.get_or_create(
                name=_club.name,
                town=_club.town,
                defaults={
                    'info': _club.info,
                    'author': _club.author,
                }
            )
            if SCREEN_OUTPUT:
                self.stdout.write(self.style.SUCCESS(f'Club "{club.name}" {"created" if created else "already exists"}'))
            
        for archer in archers:
            club = random.choice(Club.objects.all())
            membership, created = ClubMembership.objects.get_or_create(
                archer=archer,
                club=club,
                defaults={
                    'author': user,
                }
            )
            if SCREEN_OUTPUT:
                self.stdout.write(self.style.SUCCESS(f'Archer "{archer.first_name} {archer.last_name}" {"added to" if created else "already in"} Club "{club.name}"'))

        
        disciplines = [
            'Target Archery',
            'Indoor Archery',
            'Field Archery',
            '3D Archery',
            'Flight Archery',
            'Clout Archery',
            'Ski Archery',
            'Para Archery',
            'Run archery',
            'Bowhunting',
        ]
        for _discipline in disciplines:
            # Get or create discipline
            discipline, created = Discipline.objects.get_or_create(
                name=_discipline,
                defaults={
                    'author': user,
                }
            )
            if SCREEN_OUTPUT:
                self.stdout.write(self.style.SUCCESS(f'Discipline "{discipline.name}" {"created" if created else "already exists"}'))

        # Create sample discipline memberships
        for archer in archers:
            discipline = random.choice(Discipline.objects.all())
            membership, created = DisciplineMembership.objects.get_or_create(
                archer=archer,
                discipline=discipline,
                defaults={
                    'author': user,
                }
            )
            if SCREEN_OUTPUT:
                self.stdout.write(self.style.SUCCESS(f'Archer "{archer.first_name} {archer.last_name}" {"added to" if created else "already in"} Discipline "{discipline.name}"'))
        
        # Create sample catergories
        categories = [
            'Olympic Recurve',
            'Compound',
            'Barebow',
            'Longbow',
            'Traditional',
        ]
        for _category in categories:
            # Get or create category
            category, created = Category.objects.get_or_create(
                name=_category,
                defaults={
                    'author': user,
                }
            )
            if SCREEN_OUTPUT:
                self.stdout.write(self.style.SUCCESS(f'Category "{category.name}" {"created" if created else "already exists"}'))
                
        # Create sample category memberships
        for archer in archers:
            category = random.choice(Category.objects.all())
            membership, created = CategoryMembership.objects.get_or_create(
                archer=archer,
                category=category,
                defaults={
                    'author': user,
                }
            )
            if SCREEN_OUTPUT:
                self.stdout.write(self.style.SUCCESS(f'Archer "{archer.first_name} {archer.last_name}" {"added to" if created else "already in"} Category "{category.name}"'))

        self.stdout.write(self.style.SUCCESS('Database population complete.'))

        # Create sample Teams
        teams = [
            'The Archers',
            'Bullseye Squad',
            'Arrow Masters',
            'Target Titans',
            'Precision Crew',
        ]
        for _team in teams:
            # Get or create team
            team, created = Team.objects.get_or_create(
                name=_team,
                defaults={
                    'author': user,
                }
            )
            if SCREEN_OUTPUT:
                self.stdout.write(self.style.SUCCESS(f'Team "{team.name}" {"created" if created else "already exists"}'))
                
        # Create sample team memberships
        for archer in archers:
            team = random.choice(Team.objects.all())
            membership, created = TeamMembership.objects.get_or_create(
                archer=archer,
                team=team,
                defaults={
                    'author': user,
                }
            )
            if SCREEN_OUTPUT:
                self.stdout.write(self.style.SUCCESS(f'Archer "{archer.first_name} {archer.last_name}" {"added to" if created else "already in"} Team "{team.name}"'))
                

import random
from decimal import Decimal
from lorem_text import lorem

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
    ScoringSheet,
)

SCREEN_OUTPUT = True

class Command(BaseCommand):
    user = None   
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # get or create superuser
        self.user = User.objects.filter(username='admin').first()
        if not self.user:
            self.user = User.objects.create_superuser(username='admin', password='changeme', email='me@mail.com')
        if SCREEN_OUTPUT:
            self.stdout.write(self.style.SUCCESS('Superuser "admin" ensured.'))
        
    help = 'Populate the database with sample data'
    
    def handle(self, *args, **kwargs):
        self.create_sample_archers()
        self.create_sample_clubs()
        self.create_sample_club_memberships()

    def create_sample_archers(self):
        archers = [
            Archer(
                author=self.user,
                first_name="Peter",
                last_name="Paulus",
                union_number=111111,
                info=lorem_ipsum.paragraph(),
            ),
            Archer(
                author=self.user,
                first_name="Piet",
                last_name="Jansen",
                union_number=222222,
                info=lorem_ipsum.paragraph(),
            ),
            Archer(
                author=self.user,
                first_name="Peter",
                last_name="Vanalles",
                union_number=333333,
                info=lorem_ipsum.paragraph(),
            ),
        ]
        for _archer in archers:
            new_archer = Archer.objects.filter(union_number=_archer.union_number)
            if not new_archer:
                new_archer = Archer.objects.create(
                    first_name=_archer.first_name,
                    last_name=_archer.last_name,
                    union_number=_archer.union_number,
                    info=_archer.info,
                    author=_archer.author,
                )
                if SCREEN_OUTPUT:
                    self.stdout.write(self.style.SUCCESS(f'Archer - {new_archer.first_name} {new_archer.last_name} created'))

    def create_sample_clubs(self):
        clubs = [
            Club(
                author=self.user,
                name="De Boogschutters", 
                town="Eindhoven", 
                info=lorem_ipsum.paragraph(),
            ),
            Club(
                author=self.user,
                name="De Pijlen", 
                town="Veldhoven", 
                info=lorem_ipsum.paragraph(),
            ),
            Club(
                author=self.user,
                name="De Schutters", 
                town="Breda", 
                info=lorem_ipsum.paragraph(),
            ),
            Club(
                author=self.user,
                name="De Pijl", 
                town="Tilburg", 
                info=lorem_ipsum.paragraph(),
            ),
            Club(
                author=self.user,
                name="De Boog", 
                town="Den Bosch",
                info=lorem_ipsum.paragraph(),
            ),
        ]
        for _club in clubs:
            new_club = Club.objects.filter(name=_club.name)
            if not new_club:
                new_club = Club.objects.create(
                    author=_club.author,
                    name=_club.name,
                    town=_club.town,
                    info=_club.info,
                )
                if SCREEN_OUTPUT:
                    self.stdout.write(self.style.SUCCESS(f'Club "{new_club.name} created" '))

    def create_sample_club_memberships(self):
        for i in range (1,10):
            _club = random.choice(Club.objects.all())
            _archer = random.choice(Archer.objects.all())
            new_club_membership = ClubMembership.objects.filter(
                archer=_archer,
                club=_club,
            )
            if not new_club_membership:
                new_club_membership = ClubMembership.objects.create(
                    author=self.user,
                    club=_club,
                    archer=_archer,
                    info=lorem_ipsum.paragraph(),
                )
                if SCREEN_OUTPUT:
                    self.stdout.write(self.style.SUCCESS(f'New ClubMembership created: Club - {new_club_membership.club.name} ; Archer - {new_club_membership.archer.first_name} {new_club_membership.archer.last_name}'))

    def create_disciplines(self):
        disciplines = [
            Discipline(
                author=self.user,
                name="Target Archery",
                info=lorem_ipsum.paragraph(),
            ),
            Discipline(
                author=self.user,
                name="Indoor Archery",
                info=lorem_ipsum.paragraph(),
            ),
            Discipline(
                author=self.user,
                name="Field Archery",
                info=lorem_ipsum.paragraph(),
            ),
            Discipline(
                author=self.user,
                name="3D Archery",
                info=lorem_ipsum.paragraph(),
            ),
            Discipline(
                author=self.user,
                name="Flight Archery",
                info=lorem_ipsum.paragraph(),
            ),
            Discipline(
                author=self.user,
                name="Clout Archery",
                info=lorem_ipsum.paragraph(),
            ),
            Discipline(
                author=self.user,
                name="Ski Archery",
                info=lorem_ipsum.paragraph(),
            ),
            Discipline(
                author=self.user,
                name="Para Archery",
                info=lorem_ipsum.paragraph(),
            ),
            Discipline(
                author=self.user,
                name="Run archery",
                info=lorem_ipsum.paragraph(),
            ),
            Discipline(
                author=self.user,
                name="Bowhunting",
                info=lorem_ipsum.paragraph(),
            ),
        ]

        # for _discipline in disciplines:
        #     # Get or create discipline
        #     discipline, created = Discipline.objects.get_or_create(
        #         name=_discipline,
        #         defaults={
        #             'author': user,
        #         }
        #     )
        #     if SCREEN_OUTPUT:
        #         self.stdout.write(self.style.SUCCESS(f'Discipline "{discipline.name}" {"created" if created else "already exists"}'))

        # # Create sample discipline memberships
        # for archer in archers:
        #     discipline = random.choice(Discipline.objects.all())
        #     membership, created = DisciplineMembership.objects.get_or_create(
        #         archer=archer,
        #         discipline=discipline,
        #         defaults={
        #             'author': user,
        #         }
        #     )
        #     if SCREEN_OUTPUT:
        #         self.stdout.write(self.style.SUCCESS(f'Archer "{archer.first_name} {archer.last_name}" {"added to" if created else "already in"} Discipline "{discipline.name}"'))
        
        # # Create sample catergories
        # categories = [
        #     'Olympic Recurve',
        #     'Compound',
        #     'Barebow',
        #     'Longbow',
        #     'Traditional',
        # ]
        # for _category in categories:
        #     # Get or create category
        #     category, created = Category.objects.get_or_create(
        #         name=_category,
        #         defaults={
        #             'author': user,
        #         }
        #     )
        #     if SCREEN_OUTPUT:
        #         self.stdout.write(self.style.SUCCESS(f'Category "{category.name}" {"created" if created else "already exists"}'))
                
        # # Create sample category memberships
        # for archer in archers:
        #     category = random.choice(Category.objects.all())
        #     membership, created = CategoryMembership.objects.get_or_create(
        #         archer=archer,
        #         category=category,
        #         defaults={
        #             'author': user,
        #         }
        #     )
        #     if SCREEN_OUTPUT:
        #         self.stdout.write(self.style.SUCCESS(f'Archer "{archer.first_name} {archer.last_name}" {"added to" if created else "already in"} Category "{category.name}"'))

        # self.stdout.write(self.style.SUCCESS('Database population complete.'))

        # # Create sample Teams
        # teams = [
        #     'The Archers',
        #     'Bullseye Squad',
        #     'Arrow Masters',
        #     'Target Titans',
        #     'Precision Crew',
        # ]
        # for _team in teams:
        #     # Get or create team
        #     team, created = Team.objects.get_or_create(
        #         name=_team,
        #         defaults={
        #             'author': user,
        #         }
        #     )
        #     if SCREEN_OUTPUT:
        #         self.stdout.write(self.style.SUCCESS(f'Team "{team.name}" {"created" if created else "already exists"}'))
                
        # # Create sample team memberships
        # for archer in archers:
        #     team = random.choice(Team.objects.all())
        #     membership, created = TeamMembership.objects.get_or_create(
        #         archer=archer,
        #         team=team,
        #         defaults={
        #             'author': user,
        #         }
        #     )
        #     if SCREEN_OUTPUT:
        #         self.stdout.write(self.style.SUCCESS(f'Archer "{archer.first_name} {archer.last_name}" {"added to" if created else "already in"} Team "{team.name}"'))
                









        # # Create sample Scoringsheets        
        # scoringsheets = [
        #     ScoringSheet(
        #         author=user,
        #         name="Indoor 18 meter",
        #         columns=3,
        #         rows=10,
        #         info=lorem.sentence()
        #     ),
        #     ScoringSheet(
        #         author=user,
        #         name="Indoor 25 meter",
        #         columns=5,
        #         rows=5,
        #         info=lorem.sentence()
        #     ),
        #     ScoringSheet(
        #         author=user,
        #         name="Outdoor 30 meter",
        #         columns=3,
        #         rows=12,
        #         info=lorem.sentence()
        #     ),
        #     ScoringSheet(
        #         author=user,
        #         name="Outdoor 30 meter",
        #         columns=3,
        #         rows=12,
        #         info=lorem.sentence()
        #     ),
        #     ScoringSheet(
        #         author=user,
        #         name="Outdoor 50 meter",
        #         columns=3,
        #         rows=12,
        #         info=lorem.sentence()
        #     ),
        # ]
        # for _archer in archers:
        #     # Get or create archer
        #     archer, created = Archer.objects.get_or_create(
        #         first_name=_archer.first_name,
        #         last_name=_archer.last_name,
        #         defaults={
        #             'author': _archer.author,
        #         }
        #     )
        #     if SCREEN_OUTPUT:
        #         self.stdout.write(self.style.SUCCESS(f'Archer "{archer.first_name} {archer.last_name}" {"created" if created else "already exists"}'))
        # # Get all archers
        # archers = Archer.objects.all()

import random
from decimal import Decimal
from lorem_text import lorem

from django.core.management.base import BaseCommand
# from django.contrib.auth.models import User
# from users.models import User
from userauth.models import CustomUser
from django.utils import lorem_ipsum

from modeling.models import (
    Archer, 
    Club,
    ClubMembership,
    Discipline,
    DisciplineMembership,
    Category,
    CategoryMembership,
    TargetFaceNameChoice,
    TargetFace,
    Team,
    TeamMembership,
    ScoringSheet,
    Round,
    RoundMembership,
    Score,
    Competition,
    CompetitionMembership,
)

from archery_materials.models import (
    BowType,
    BowTypeMembership,
)

SCREEN_OUTPUT = True

class Command(BaseCommand):
    user = None   
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # get or create superuser
        self.user = CustomUser.objects.filter(username='admin').first()
        if not self.user:
            self.user = CustomUser.objects.create_superuser(username='admin', password='changeme', email='me@mail.com')
        if SCREEN_OUTPUT:
            self.stdout.write(self.style.SUCCESS('Superuser "admin" ensured.'))
        
    help = 'Populate the database with sample data'
    
    def handle(self, *args, **kwargs):
        # modeling app - begin
        self.create_sample_archers()
        self.create_sample_clubs()
        self.create_sample_club_memberships()
        self.create_sample_disciplines()
        self.create_sample_discipline_memberships()
        self.create_sample_categories()
        self.create_sample_category_memberships()
        self.create_sample_teams()
        self.create_sample_team_memberships()
        self.create_sample_scoringsheets()
        self.create_sample_target_face_name_choices()
        self.create_sample_target_faces()
        self.create_sample_rounds()
        # modeling app - end
        
        # archery_materials app - begin
        self.create_sample_bowtypes()
        self.create_sample_bowtype_memberships()
        # archery_materials app - end      

    # modeling app - begin

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
        for archer in archers:
            if not Archer.objects.filter(union_number=archer.union_number):
                archer.save()
                if SCREEN_OUTPUT:
                    self.stdout.write(self.style.SUCCESS(f'Archer - {archer.first_name} {archer.last_name} created'))

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
        for club in clubs:
            if not Club.objects.filter(name=club.name):
                club.save()
                if SCREEN_OUTPUT:
                    self.stdout.write(self.style.SUCCESS(f'Club "{club.name} created" '))

    def create_sample_club_memberships(self):
        for i in range (1,10):
            _club = random.choice(Club.objects.all())
            _archer = random.choice(Archer.objects.all())
            club_membership = ClubMembership.objects.filter(
                archer=_archer,
                club=_club,
            )
            if not club_membership:
                club_membership = ClubMembership.objects.create(
                    author=self.user,
                    club=_club,
                    archer=_archer,
                    info=lorem_ipsum.paragraph(),
                )
                if SCREEN_OUTPUT:
                    self.stdout.write(self.style.SUCCESS(f'New ClubMembership created: Club - {club_membership.club.name} ; Archer - {club_membership.archer.first_name} {club_membership.archer.last_name}'))

    def create_sample_disciplines(self):
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
        for discipline in disciplines:
            if not Discipline.objects.filter(name=discipline.name):
                discipline.save()
                if SCREEN_OUTPUT:
                    self.stdout.write(self.style.SUCCESS(f'Discipline "{discipline.name} created"'))

    def create_sample_discipline_memberships(self):
        for i in range(1, 10):
            discipline = random.choice(Discipline.objects.all())
            archer = random.choice(Archer.objects.all())
            discipline_membership = DisciplineMembership.objects.filter(
                archer=archer,
                discipline=discipline,
            )
            if not discipline_membership:
                discipline_membership = DisciplineMembership.objects.create(
                    author=self.user,
                    discipline=discipline,
                    archer=archer,
                    info=lorem_ipsum.paragraph(),
                )
                if SCREEN_OUTPUT:
                    self.stdout.write(self.style.SUCCESS(f'New DisciplineMembership created: Discipline - {discipline_membership.discipline.name} ; Archer - {discipline_membership.archer.first_name} {discipline_membership.archer.last_name}'))
                
    def create_sample_categories(self):
        categories = [
            Category(
                author=self.user,
                name="Recurve",
                info=lorem_ipsum.paragraph(),
            ),
            Category(
                author=self.user,
                name="Compound",
                info=lorem_ipsum.paragraph(),
            ),
            Category(
                author=self.user,
                name="Barebow",
                info=lorem_ipsum.paragraph(),
            ),
            Category(
                author=self.user,
                name="Longbow",
                info=lorem_ipsum.paragraph(),
            ),
            Category(
                author=self.user,
                name="Traditional",
                info=lorem_ipsum.paragraph(),
            ),
        ]
        for category in categories:
            if not Category.objects.filter(name=category.name):
                category.save()
                if SCREEN_OUTPUT:
                    self.stdout.write(self.style.SUCCESS(f'Category - {category.name} created'))
       
    def create_sample_category_memberships(self):
        for i in range(1, 10):
            category = random.choice(Category.objects.all())
            archer = random.choice(Archer.objects.all())
            category_membership = CategoryMembership.objects.filter(
                archer=archer,
                category=category,
            )
            if not category_membership:
                category_membership = CategoryMembership.objects.create(
                    author=self.user,
                    category=category,
                    archer=archer,
                    info=lorem_ipsum.paragraph(),
                )
                if SCREEN_OUTPUT:
                    self.stdout.write(self.style.SUCCESS(f'New CategoryMembership created: Category - {category_membership.category.name} ; Archer - {category_membership.archer.first_name} {category_membership.archer.last_name}'))                
        
    def create_sample_teams(self):
        teams = [
            Team(
                author=self.user,
                name='The Archers',
                info=lorem_ipsum.paragraph(),              
            ),
            Team(
                author=self.user,
                name='Bullseye Squad',
                info=lorem_ipsum.paragraph(),              
            ),
            Team(
                author=self.user,
                name='Arrow Masters',
                info=lorem_ipsum.paragraph(),              
            ),
            Team(
                author=self.user,
                name='Target Titans',
                info=lorem_ipsum.paragraph(),              
            ),
            Team(
                author=self.user,
                name='Precision Crew',
                info=lorem_ipsum.paragraph(),              
            ),
        ]
        for team in teams:
            if not Team.objects.filter(name=team.name):
                team.save()
                if SCREEN_OUTPUT:
                    self.stdout.write(self.style.SUCCESS(f'Team "{team.name} created"'))
                         
    def create_sample_team_memberships(self):
        for i in range(1, 10):
            team = random.choice(Team.objects.all())
            archer = random.choice(Archer.objects.all())
            team_membership = TeamMembership.objects.filter(
                archer=archer,
                team=team,
            )
            if not team_membership:
                team_membership = TeamMembership.objects.create(
                    author=self.user,
                    team=team,
                    archer=archer,
                    info=lorem_ipsum.paragraph(),
                )
                if SCREEN_OUTPUT:
                    self.stdout.write(self.style.SUCCESS(f'New TeamMembership created: Discipline - {team_membership.team.name} ; Archer - {team_membership.archer.first_name} {team_membership.archer.last_name}'))
                
    def create_sample_scoringsheets(self):
        scoringsheets = [
            ScoringSheet(
                author=self.user,
                name="Indoor 18 meter",
                columns=3,
                rows=10,
                info=lorem.sentence()
            ),
            ScoringSheet(
                author=self.user,
                name="Indoor 25 meter",
                columns=5,
                rows=5,
                info=lorem.sentence()
            ),
            ScoringSheet(
                author=self.user,
                name="Outdoor 30 meter",
                columns=3,
                rows=12,
                info=lorem.sentence()
            ),
            ScoringSheet(
                author=self.user,
                name="Outdoor 50 meter",
                columns=3,
                rows=12,
                info=lorem.sentence()
            ),
            ScoringSheet(
                author=self.user,
                name="Outdoor 60 meter",
                columns=3,
                rows=12,
                info=lorem.sentence()
            ),
            ScoringSheet(
                author=self.user,
                name="Outdoor 70 meter",
                columns=3,
                rows=12,
                info=lorem.sentence()
            ),
            ScoringSheet(
                author=self.user,
                name="Outdoor 90 meter",
                columns=3,
                rows=12,
                info=lorem.sentence()
            ),
        ]
        for scoringsheet in scoringsheets:
            if not ScoringSheet.objects.filter(name=scoringsheet.name):
                scoringsheet.save()
                if SCREEN_OUTPUT:
                    self.stdout.write(self.style.SUCCESS(f'Scoringsheet - {scoringsheet.name} created'))

    # TODO: Finish create_sample_target_face_name_choices
    def create_sample_target_face_name_choices(self):
        targetfacenamechoices = [
            TargetFaceNameChoice(
                author=self.user,
                environment="Indoor",
                discipline="Target Archery",
                targetsize="40 cm",
                keyfeature="10-Zone",
                info=lorem_ipsum.paragraph(),
            ),
            TargetFaceNameChoice(
                author=self.user,
                environment="Indoor",
                discipline="Target Archery",
                targetsize="60 cm",
                keyfeature="10-Zone",
                info=lorem_ipsum.paragraph(),
            ),
            TargetFaceNameChoice(
                author=self.user,
                environment="Outdoor",
                discipline="Target Archery",
                targetsize="122 cm",
                keyfeature="10-Zone",
                info=lorem_ipsum.paragraph(),
            ),
            TargetFaceNameChoice(
                author=self.user,
                environment="Outdoor",
                discipline="Target Archery",
                targetsize="80 cm",
                keyfeature="10-Zone",
                info=lorem_ipsum.paragraph(),
            ),
            TargetFaceNameChoice(
                author=self.user,
                environment="Outdoor",
                discipline="Field Archery",
                targetsize="80 cm",
                keyfeature="6-Zone",
                info=lorem_ipsum.paragraph(),
            ),
            TargetFaceNameChoice(
                author=self.user,
                environment="Outdoor",
                discipline="Field Archery",
                targetsize="60 cm",
                keyfeature="6-Zone",
                info=lorem_ipsum.paragraph(),
            ),
            TargetFaceNameChoice(
                author=self.user,
                environment="Outdoor",
                discipline="Field Archery",
                targetsize="40 cm",
                keyfeature="6-Zone",
                info=lorem_ipsum.paragraph(),
            ),
            TargetFaceNameChoice(
                author=self.user,
                environment="Outdoor",
                discipline="Field Archery",
                targetsize="20 cm",
                keyfeature="6-Zone",
                info=lorem_ipsum.paragraph(),
            ),
        ]
        for targetfacenamechoice in targetfacenamechoices:
            new_name = f"{targetfacenamechoice.environment} {targetfacenamechoice.discipline} {targetfacenamechoice.targetsize} {targetfacenamechoice.keyfeature}"
            if not TargetFaceNameChoice.objects.filter(name=new_name):
                targetfacenamechoice.name = new_name
                targetfacenamechoice.save()
                if SCREEN_OUTPUT:
                    self.stdout.write(self.style.SUCCESS(f'TargetFaceNameChoice "{new_name} created" '))
    
    # TODO: Finish create_sample_target_faces
    def create_sample_target_faces(self):
        pass

    # January:  1,8,15,22,29
    # February: 5,12,19,26
    def create_sample_rounds(self):
        rounds = [
            Round(
                author = self.user,
                name = "Indoor 18 meter Donderdag 1 Januarie 2026",
                start_date = "2026-01-01",
                start_time = "20:00",
                info=lorem_ipsum.paragraph(),
            ),
            Round(
                author = self.user,
                name = "Indoor 18 meter Donderdag 8 Januarie 2026",
                start_date = "2026-01-08",
                start_time = "20:00",
                info=lorem_ipsum.paragraph(),
            ),
            Round(
                author = self.user,
                name = "Indoor 18 meter Donderdag 15 Januarie 2026",
                start_date = "2026-01-15",
                start_time = "20:00",
                info=lorem_ipsum.paragraph(),
            ),
            Round(
                author = self.user,
                name = "Indoor 18 meter Donderdag 22 Januarie 2026",
                start_date = "2026-01-22",
                start_time = "20:00",
                info=lorem_ipsum.paragraph(),
            ),
            Round(
                author = self.user,
                name = "Indoor 18 meter Donderdag 29 Januarie 2026",
                start_date = "2026-01-29",
                start_time = "20:00",
                info=lorem_ipsum.paragraph(),
            ),
        ]
        for round in rounds:
            if not Round.objects.filter(name=round.name):
                round.save()
                if SCREEN_OUTPUT:
                    self.stdout.write(self.style.SUCCESS(f'Round - {round.name} created'))
            
        

    # modeling app - end

    # archery_materials app - begin

    def create_sample_bowtypes(self):
        bowtypes = [
            BowType(
                author=self.user,
                name="Compound", 
                info=lorem_ipsum.paragraph(),
            ),
            BowType(
                author=self.user,
                name="Crossbow", 
                info=lorem_ipsum.paragraph(),
            ),
            BowType(
                author=self.user,
                name="Longbow", 
                info=lorem_ipsum.paragraph(),
            ),
            BowType(
                author=self.user,
                name="Recurve", 
                info=lorem_ipsum.paragraph(),
            ),
        ]
        for bowtype in bowtypes:
            if not BowType.objects.filter(name=bowtype.name):
                bowtype.save()
                if SCREEN_OUTPUT:
                    self.stdout.write(self.style.SUCCESS(f'BowType "{bowtype.name} created" '))

    def create_sample_bowtype_memberships(self):
        for i in range (1,10):
            bowtype = random.choice(BowType.objects.all())
            archer = random.choice(Archer.objects.all())
            bowtype_membership = BowTypeMembership.objects.filter(
                archer=archer,
                bowtype=bowtype,
            )
            if not bowtype_membership:
                bowtype_membership = BowTypeMembership.objects.create(
                    author=self.user,
                    bowtype=bowtype,
                    archer=archer,
                    info=lorem_ipsum.paragraph(),
                )
                if SCREEN_OUTPUT:
                    self.stdout.write(self.style.SUCCESS(f'New BowTypeMembership created: BowType - {bowtype_membership.bowtype.name} ; Archer - {bowtype_membership.archer.first_name} {bowtype_membership.archer.last_name}'))
    
    # archery_materials app - end      

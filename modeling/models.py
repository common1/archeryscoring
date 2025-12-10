import uuid
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import AutoSlugField
from users.models import User
from wagtail.admin.panels import MultiFieldPanel, FieldPanel, FieldRowPanel
from django.core.validators import MaxValueValidator, MinValueValidator

from wagtail.models import Page

class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Archer(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self._meta.get_field('slug').populate_from = 'last_name'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    last_name = models.CharField(
        max_length=64,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("last name of archer"),
        help_text=_("format: required, max-64")
    )
    first_name = models.CharField(
        max_length=32,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("first name of archer"),
        help_text=_("format: required, max-32")
    )
    middle_name = models.CharField(
        max_length=6,
        null=True,
        unique=False,
        blank=True,
        verbose_name=_("middle name of archer"),
        help_text=_("format: not required, max-6")
    )
    slug = AutoSlugField(populate_from='last_name',editable=True)
    union_number = models.PositiveIntegerField(
        unique=True,
        null=True,
        blank=False,
        verbose_name=_("union number of archer"),
        help_text=_("format: not required")
    )
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("archer information"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        verbose_name=_("author of archer"),
        related_name='archer_author',
        help_text=_("format: not required, default=1 (superuser)"),
    )

    # Contact information
    
    email = models.EmailField(
        max_length=254,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("email address of archer"),
        help_text=_("format: not required, max-254")
    )
    phone = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("phone number of archer"),
        help_text=_("format: not required, max-15")
    )
    address = models.CharField(
        max_length=128,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("address of archer"),
        help_text=_("format: not required, max-128")
    )
    city = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("city of archer"),
        help_text=_("format: not required, max-64")
    )
    zip_code = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("zip code of archer"),
        help_text=_("format: not required, max-6")
    )
    province = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("state or province of archer"),
        help_text=_("format: not required, max-64")
    )

    # Contact information end

    # Extra fields for archer information

    birth_date = models.DateField(
        null=True,
        blank=True,
        editable=True,
        unique=False,
        verbose_name=_("birth date of archer"),
        help_text=_("format: Y-m-d, not required"),
    )
    
    # Extra fields for archer information end
    
    panels = [
        FieldPanel('union_number'),
        FieldPanel('last_name'),
        FieldPanel('first_name'),
        FieldPanel('middle_name'),
        FieldPanel('info'),
        MultiFieldPanel(
            [
                FieldPanel('email'),
                FieldPanel('phone'),
                FieldPanel('address'),
                FieldPanel('city'),
                FieldPanel('zip_code'),
                FieldPanel('province'),
            ],
            heading = "Contact Information",
            classname="collapsible collapsed",
        ),
        MultiFieldPanel(
            [
                FieldPanel('birth_date'),
                FieldPanel('slug'),
                FieldPanel('author'),
            ],
            heading = "Extra Information",
            classname="collapsible collapsed",
        ),
    ]
    
    class Meta:
        db_table = 'archers'
        ordering = ['last_name']
        verbose_name = _("Archer")
        verbose_name_plural = _("Archers")

    def __str__(self):
        s_middle_name = ""
        if self.middle_name:
            s_middle_name = self.middle_name
        return f"{self.last_name} {self.first_name} {s_middle_name}"

    def __unicode__(self):
        s_middle_name = ""
        if self.middle_name:
            s_middle_name = self.middle_name
        return f"{self.last_name} {self.first_name} {s_middle_name}"

# Target Archery
# Indoor Archery
# Field Archery
# 3D Archery
# Flight Archery
# Clout Archery
# Ski Archery
# Para Archery
# Run archery
# Bowhunting
class Discipline(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self._meta.get_field('slug').populate_from = 'name'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=64,
        null=False,
        unique=True,
        blank=False,
        verbose_name=_("discipline name"),
        help_text=_("format: required, max-64")
    )
    slug = AutoSlugField(populate_from='name',editable=True)
    archers = models.ManyToManyField(
        Archer,
        through='DisciplineMembership',
        blank=True,
        help_text=_("format: not required"),
        related_name='disciplines',
        verbose_name=_("archers in discipline"),
    )
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("discipline information"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='discipline_author',
        verbose_name=_("author of discipline"),
        help_text=_("format: required, default=1 (superuser)"),
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('info'),
        FieldPanel('archers'),
        MultiFieldPanel(
            [
                FieldPanel('slug'),
                FieldPanel('author'),
            ],
            heading = "Extra Information",
            classname="collapsible collapsed",
        ),
    ]
    
    class Meta:
        db_table = 'disciplines'
        ordering = ['name']
        verbose_name = _("Discipline")
        verbose_name_plural = _("Disciplines")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class DisciplineMembership(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    discipline = models.ForeignKey(
        Discipline,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("disciplinemembership discipline"),
        help_text=_("format: required"),
        related_name='disciplinememberships'
    )
    archer = models.ForeignKey(
        Archer,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("disciplinemembership archer"),
        help_text=_("format: required"),
        related_name='disciplinemembership_archer'
    )
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("membership information"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='discipline_membership_author',
        verbose_name=_("author of membership"),
        help_text=_("format: required, default=1 (superuser)"),
    )

    class Meta:
        db_table = 'disciplinememberships'
        ordering = ['discipline__name']
        verbose_name = _("Discipline Membership")
        verbose_name_plural = _("Discipline Memberships")

    def __str__(self):
        return f"{str(self.archer)} - {str(self.discipline)}"

    def __unicode__(self):
        return f"{str(self.archer)} - {str(self.discipline)}"

class Club(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self._meta.get_field('slug').populate_from = 'name'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=64,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("club name"),
        help_text=_("format: required, max-64")
    )
    slug = AutoSlugField(populate_from='name',editable=True)
    address = models.CharField(
        max_length=128,
        null=True,
        unique=False,
        blank=True,
        verbose_name=_("address of club"),
        help_text=_("format: not required, max-128")
    )
    zip_code = models.CharField(
        max_length=6,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("zip code of archer"),
        help_text=_("format: not required, max-6")
    )
    town = models.CharField(
        max_length=64,
        null=True,
        unique=False,
        blank=True,
        verbose_name=_("town name"),
        help_text=_("format: not required, max-64")
    )
    archers = models.ManyToManyField(
        Archer,
        through='ClubMembership',
        blank=True,
        help_text=_("format: not required"),
        related_name='clubs',
        verbose_name=_("archers in club"),
    )
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("club information"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='author_club',
        verbose_name=_("author of club"),
        help_text=_("format: not required, default=1 (superuser)"),
    )

    # Extra fields for club information

    email = models.EmailField(
        max_length=254,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("email address of club"),
        help_text=_("format: not required, max-254")
    )
    phone = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("phone number of club"),
        help_text=_("format: not required, max-15")
    )
    website = models.URLField(
        max_length=200,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("website of club"),
        help_text=_("format: not required, max-200")
    )
    social_media = models.CharField(
        max_length=128,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("social media handle of club"),
        help_text=_("format: not required, max-128")
    )
     
    # Extra fields for club information end        

    panels = [
        FieldPanel('name'),
        FieldPanel('info'),
        FieldPanel('archers'),
        MultiFieldPanel(
            [
                FieldPanel('address'),
                FieldPanel('zip_code'),
                FieldPanel('town'),
                FieldPanel('phone'),
                FieldPanel('email'),
                FieldPanel('website'),
                FieldPanel('social_media'),
            ],
            heading = "Contact Information",
            classname="collapsible collapsed",
        ),
        MultiFieldPanel(
            [
                FieldPanel('slug'),
                FieldPanel('author'),
            ],
            heading = "Extra Information",
            classname="collapsible collapsed",
        ),
    ]
    
    class Meta:
        db_table = 'clubs'
        ordering = ['name']
        verbose_name = _("Club")
        verbose_name_plural = _("Clubs")

    def __str__(self):
        return self.name

    def __unicode__(self):       
        return self.name

class ClubMembership(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    club = models.ForeignKey(
        Club,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("club of the member"),
        help_text=_("format: required"),
        related_name='memberships'
    )
    archer = models.ForeignKey(
        Archer,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("archer who is member"),
        help_text=_("format: required"),
        related_name='clubmember_archer'
    )
    slug = AutoSlugField(populate_from=('archer__last_name', 'club__name'), editable=True)
    start_date = models.DateField(
        null=True,
        blank=True,
        editable=True,
        unique=False,
        verbose_name=_("start date of membership"),
        help_text=_("format: Y-m-d, not required"),
    )
    end_date = models.DateField(
        null=True,
        blank=True,
        editable=True,
        unique=False,
        verbose_name=_("end date of membership"),
        help_text=_("format: Y-m-d, not required"),
    )
    
    # Extra fields for membership information
    
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("membership information"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='membership_author',
        verbose_name=_("author of membership"),
        help_text=_("format: required, default=1 (superuser)"),
    )

    # Extra fields for membership information end

    panels = [
        FieldPanel('club'),
        FieldPanel('archer'),
        MultiFieldPanel(
            [
                FieldPanel('start_date'),
                FieldPanel('end_date'),
            ],
            heading = "Information",
            classname="collapsible collapsed",
        ),
        MultiFieldPanel(
            [
                FieldPanel('slug'),
                FieldPanel('author'),
        FieldPanel('info'),
            ],
            heading = "Extra Information",
            classname="collapsible collapsed",
        ),
    ]

    class Meta:
        db_table = 'clubmemberships'
        ordering = ['start_date']
        verbose_name = _("Club Membership")
        verbose_name_plural = _("Club Memberships")

    def __str__(self):
        return f"{str(self.archer)} - {str(self.club)} {self.club.town}"

    def __unicode__(self):
        return f"{str(self.archer)} - {str(self.club)} {self.club.town}"

# Olympic Recurve
# Compound
# Barebow
# Longbow
# Traditional
class Category(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self._meta.get_field('slug').populate_from = 'name'
        
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=64,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("category name"),
        help_text=_("format: required, max-64")
    )
    slug = AutoSlugField(populate_from='name',editable=True)
    archers = models.ManyToManyField(
        Archer,
        through='CategoryMembership',
        blank=True,
        help_text=_("format: not required"),
        related_name='categories',
        verbose_name=_("archers in category"),
    )
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("category information"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        verbose_name=_("author of category"),
        related_name='category_author',
        help_text=_("format: required, default=1 (superuser)"),
    )
    
    panels = [
        FieldPanel('name'),
        FieldPanel('info'),
        FieldPanel('archers'),
        MultiFieldPanel(
            [
                FieldPanel('slug'),
                FieldPanel('author'),
            ],
            heading = "Extra Information",
            classname="collapsible collapsed",
        ),
    ]

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class AgeGroup(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self._meta.get_field('slug').populate_from = 'name'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=32,
        null=False,
        unique=True,
        blank=False,
        verbose_name=_("age group name"),
        help_text=_("format: required, max-32")
    )
    slug = AutoSlugField(populate_from='name',editable=True)
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("agegroup information"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='agegroup_author',
        verbose_name=_("author of agegroup"),
        help_text=_("format: required, default=1 (superuser)"),
    )

    class Meta:
        db_table = 'agegroups'
        ordering = ['name']
        verbose_name = _("Age Group")
        verbose_name_plural = _("Age Groups")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class CategoryMembership(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("categorymembership category"),
        help_text=_("format: required"),
        related_name='categorymemberships'
    )
    archer = models.ForeignKey(
        Archer,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("categorymembership archer"),        
        related_name='categorymembership_archer',
        help_text=_("format: required"),
    )
    agegroup = models.ForeignKey(
        AgeGroup,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("age group of category membership"),
        related_name='categorymembership_agegroup',
        help_text=_("format: required"),
    )

    # Extra fields for membership information

    slug = AutoSlugField(populate_from=('category__name', 'archer__last_name',), editable=True)
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("category information"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='category_membership_author',
        verbose_name=_("author of categorymembership"),
        help_text=_("format: required, default=1 (superuser)"),
    )

    # Extra fields for membership information end

    panels = [
        FieldPanel('category'),
        FieldPanel('archer'),
        FieldPanel('agegroup'),
        FieldPanel('info'),
        MultiFieldPanel(
            [
                FieldPanel('slug'),
                FieldPanel('author'),
            ],
            heading = "Extra Information",
            classname="collapsible collapsed",
        ),
    ]

    class Meta:
        db_table = 'categorymemberships'
        ordering = ['category__name']
        verbose_name = _("Category Membership")
        verbose_name_plural = _("Category Memberships")

    def __str__(self):
        return f"{str(self.archer)} - {str(self.category)}"

    def __unicode__(self):
        return f"{str(self.archer)} - {str(self.category)}"

class Team(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self._meta.get_field('slug').populate_from = 'name'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=64,
        null=False,
        blank=False,
        unique=False,
        verbose_name=_("team name"),
        help_text=_("format: required, max-64")
    )
    slug = AutoSlugField(populate_from='name', editable=True)
    archers = models.ManyToManyField(
        Archer,
        through='TeamMembership',
        blank=True,
        help_text=_("format: not required"),
        related_name='teams',
        verbose_name=_("archers in team"),
    )
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("team information"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='team_author',
        verbose_name=_("author of team"),
        help_text=_("format: required, default=1 (superuser)"),
    )

    class Meta:
        db_table = 'teams'
        ordering = ['name']
        verbose_name = _("Team")
        verbose_name_plural = _("Teams")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class TeamMembership(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    id = models.UUIDField(
        primary_key=True, 
        default=uuid.uuid4, 
        editable=False
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("teammembership team"),
        help_text=_("format: required"),
        related_name='teammemberships'
    )
    archer = models.ForeignKey(
        Archer,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("teammembership archer"),
        help_text=_("format: required"),
        related_name='teammembership_archer'
    )
    slug = AutoSlugField(
        populate_from=('team__name', 'archer__last_name',), 
        editable=True,
    )

    # Extra fields for teammembership information
    
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("teammembership information"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='teammembership',
        verbose_name=_("author of teammembership"),
        help_text=_("format: required, default=1 (superuser)"),
    )

    # Extra fields for teammembership information end

    panels = [
        FieldPanel('team'),
        FieldPanel('archer'),
        FieldPanel('info'),
        MultiFieldPanel(
            [
                FieldPanel('slug'),
                FieldPanel('author'),
            ],
            heading = "Extra Information",
            classname="collapsible collapsed",
        ),
    ]   
    class Meta:
        db_table = 'teammemberships'
        ordering = ['team__name']
        verbose_name = _("Team Membership")
        verbose_name_plural = _("Team Memberships")

    def __str__(self):
        return f"{str(self.archer)} - {str(self.team)}"

    def __unicode__(self):
        return f"{str(self.archer)} - {str(self.team)}"
    
#----------------------------------------
# ScoringSheet Models
#----------------------------------------

class ScoringSheet(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=64,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("scoringsheet name"),
        help_text=_("format: required, max-64")
    )
    slug = AutoSlugField(populate_from='name',editable=True)
    columns = models.PositiveIntegerField(
        unique=False,
        null=False,
        blank=False,
        default=3,
        validators=[MinValueValidator(3), MaxValueValidator(20)],
        verbose_name=_("number of columns"),
        help_text=_("format: required min-3, max-20")
    )
    rows = models.PositiveIntegerField(
        unique=False,
        null=False,
        blank=False,
        default=10,
        validators=[MinValueValidator(3), MaxValueValidator(20)],
        verbose_name=_("number of rows"),
        help_text=_("format: required min-3, max-20")
    )
        
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("scoringsheet information"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='scoringsheet_author',
        verbose_name=_("author of scoring sheet"),
        help_text=_("format: required, default=1 (superuser)"),
    )
    
    panels = [  
        FieldPanel('name'),
        FieldRowPanel([
            FieldPanel('columns'),
            FieldPanel('rows'),            
        ]),
        FieldPanel('info'),
        MultiFieldPanel(
            [
                FieldPanel('slug'),
                FieldPanel('author'),
            ],
            heading = "Extra Information",
            classname="collapsible collapsed",
        ),
    ]
    
    class Meta:
        db_table = 'scoringsheets'
        ordering = ['name']
        verbose_name = _("Scoring Sheet")
        verbose_name_plural = _("Scoring Sheets")

    def __str__(self):
        return f"{self.name} ( rows : {self.rows}, columns : {self.columns} )"

    def __unicode__(self):
        return f"{self.name} ( rows : {self.rows}, columns : {self.columns} )"

class TargetFace(BaseModel):
    pass

class Contest(BaseModel):
    pass

class ContestMembership(BaseModel):
    pass

class Result(BaseModel):
    pass

class ResultMembership(BaseModel):
    pass

class Competition(BaseModel):
    pass

class CompetitionMembership(BaseModel):
    pass

# Wagtail Pages

class GridPage(Page):
    pass

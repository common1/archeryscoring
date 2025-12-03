import uuid
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import AutoSlugField
from users.models import User
from wagtail.admin.panels import MultiFieldPanel, FieldPanel
from django.core.validators import MaxValueValidator, MinValueValidator

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
        null=True,
        unique=True,
        blank=True,
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
        db_table = 'archer'
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
        db_table = 'club'
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
        db_table = 'clubmembership'
        ordering = ['start_date']
        verbose_name = _("Club Membership")
        verbose_name_plural = _("Club Memberships")

    def __str__(self):
        return f"{str(self.archer)} - {str(self.club)} {self.club.town}"

    def __unicode__(self):
        return f"{str(self.archer)} - {str(self.club)} {self.club.town}"

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
        db_table = 'agegroup'
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
        verbose_name=_("author of category membership"),
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
        db_table = 'categorymembership'
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
        db_table = 'team'
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

    class Meta:
        db_table = 'teammembership'
        ordering = ['team__name']
        verbose_name = _("Team Membership")
        verbose_name_plural = _("Team Memberships")

    def __str__(self):
        return f"{str(self.archer)} - {str(self.team)}"

    def __unicode__(self):
        return f"{str(self.archer)} - {str(self.team)}"
    
#----------------------------------------
# Additional Equipment Models
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
        help_text=_("format: not required, max-64")
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
        default=20,
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

    class Meta:
        db_table = 'scoringsheet'
        ordering = ['name']
        verbose_name = _("Scoring Sheet")
        verbose_name_plural = _("Scoring Sheets")

    def __str__(self):
        return f"{self.name} ( {self.dimension} )"

    def __unicode__(self):
        return f"{self.name} ( {self.dimension} )"

# Recurve, Barebow, Longbow, Compound, Crossbow
# class BowStyle(BaseModel):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(
#         max_length=32,
#         null=False,
#         unique=True,
#         blank=False,
#         verbose_name=_("bow style name"),
#         help_text=_("format: required, max-32")
#     )

#     class Meta:
#         db_table = 'bowstyle'
#         ordering = ['name']
#         verbose_name = _("Bow Style")
#         verbose_name_plural = _("Bow Styles")

#     def __str__(self):
#         return self.name

#     def __unicode__(self):
#         return self.name

# Wooden, Carbon, Aluminum, Hybrid
# class BowType(BaseModel):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(
#         max_length=32,
#         null=False,
#         unique=True,
#         blank=False,
#         verbose_name=_("bow type name"),
#         help_text=_("format: required, max-32")
#     )

#     class Meta:
#         db_table = 'bowtype'
#         ordering = ['name']
#         verbose_name = _("Bow Type")
#         verbose_name_plural = _("Bow Types")

#     def __str__(self):
#         return self.name

#     def __unicode__(self):
#         return self.name

# class Bow(BaseModel):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     archer = models.ForeignKey(
#         Archer,
#         on_delete=models.CASCADE,
#         unique=False,
#         verbose_name=_("owner archer"),
#         help_text=_("format: required"),
#         related_name='bows'
#     )
#     bow_style = models.ForeignKey(
#         BowStyle,
#         on_delete=models.PROTECT,
#         unique=False,
#         verbose_name=_("bow style"),
#         help_text=_("format: required"),
#         related_name='bows'
#     )
#     bow_type = models.ForeignKey(
#         BowType,
#         on_delete=models.PROTECT,
#         unique=False,
#         verbose_name=_("bow type"),
#         help_text=_("format: required"),
#         related_name='bows'
#     )

#     class Meta:
#         db_table = 'bow'
#         ordering = ['archer__last_name']
#         verbose_name = _("Bow")
#         verbose_name_plural = _("Bows")

#     def __str__(self):
#         return f"{str(self.archer)} - {self.bow_style.name} {self.bow_type.name}"

#     def __unicode__(self):
#         return f"{str(self.archer)} - {self.bow_style.name} {self.bow_type.name}"

# Carbon, Aluminum, Wood, Fiberglass
# class ArrowMaterial(BaseModel):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(
#         max_length=32,
#         null=False,
#         unique=True,
#         blank=False,
#         verbose_name=_("arrow material name"),
#         help_text=_("format: required, max-32")
#     )

#     class Meta:
#         db_table = 'arrowmaterial'
#         ordering = ['name']
#         verbose_name = _("Arrow Material")
#         verbose_name_plural = _("Arrow Materials")

#     def __str__(self):
#         return self.name

#     def __unicode__(self):
#         return self.name

# # Wood, Plastic, Feather, Carbon
# class ArrowType(BaseModel):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(
#         max_length=32,
#         null=False,
#         unique=True,
#         blank=False,
#         verbose_name=_("arrow type name"),
#         help_text=_("format: required, max-32")
#     )

#     class Meta:
#         db_table = 'arrowtype'
#         ordering = ['name']
#         verbose_name = _("Arrow Type")
#         verbose_name_plural = _("Arrow Types")

#     def __str__(self):
#         return self.name

#     def __unicode__(self):
#         return self.name

# # Nock Types: Plastic, Feather, Pinch, Insert
# class ArrowNock(BaseModel):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(
#         max_length=64,
#         null=False,
#         unique=True,
#         blank=False,
#         verbose_name=_("arrow nock name"),
#         help_text=_("format: required, max-64")
#     )

#     class Meta:
#         db_table = 'arrownock'
#         ordering = ['name']
#         verbose_name = _("Arrow Nock")
#         verbose_name_plural = _("Arrow Nocks")

#     def __str__(self):
#         return self.name

#     def __unicode__(self):
#         return self.name

# class Arrow(BaseModel):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     archer = models.ForeignKey(
#         Archer,
#         on_delete=models.CASCADE,
#         unique=False,
#         verbose_name=_("owner archer"),
#         help_text=_("format: required"),
#         related_name='arrows'
#     )
#     arrow_type = models.ForeignKey(
#         ArrowType,
#         on_delete=models.PROTECT,
#         unique=False,
#         verbose_name=_("arrow type"),
#         help_text=_("format: required"),
#         related_name='arrows'
#     )
#     arrow_material = models.ForeignKey(
#         ArrowMaterial,
#         on_delete=models.PROTECT,
#         null=True,
#         blank=True,
#         unique=False,
#         verbose_name=_("arrow material"),
#         help_text=_("format: required"),
#         related_name='arrows'
#     )
#     arrow_nock = models.ForeignKey(
#         ArrowNock,
#         on_delete=models.PROTECT,
#         null=True,
#         blank=True,
#         unique=False,
#         verbose_name=_("arrow nock"),
#         help_text=_("format: required"),
#         related_name='arrows'
#     )

#     class Meta:
#         db_table = 'arrow'
#         ordering = ['archer__last_name']
#         verbose_name = _("Arrow")
#         verbose_name_plural = _("Arrows")

#     def __str__(self):
#         return f"{str(self.archer)} - {self.arrow_material.name} {self.arrow_type.name}"

#     def __unicode__(self):
#         return f"{str(self.archer)} - {self.arrow_material.name} {self.arrow_type.name}"

# # Quiver Types: Back, Hip, Bow-mounted
# class QuiverType(BaseModel):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(
#         max_length=64,
#         null=False,
#         unique=True,
#         blank=False,
#         verbose_name=_("quiver type name"),
#         help_text=_("format: required, max-64")
#     )

#     class Meta:
#         db_table = 'quivertype'
#         ordering = ['name']
#         verbose_name = _("Quiver Type")
#         verbose_name_plural = _("Quiver Types")

#     def __str__(self):
#         return self.name

#     def __unicode__(self):
#         return self.name

# # Quiver Materials: Leather, Synthetic, Plastic, Metal
# class QuiverMaterial(BaseModel):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(
#         max_length=64,
#         null=False,
#         unique=True,
#         blank=False,
#         verbose_name=_("quiver material name"),
#         help_text=_("format: required, max-64")
#     )

#     class Meta:
#         db_table = 'quivermaterial'
#         ordering = ['name']
#         verbose_name = _("Quiver Material")
#         verbose_name_plural = _("Quiver Materials")

#     def __str__(self):
#         return self.name

#     def __unicode__(self):
#         return self.name

# class Quiver(BaseModel):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     archer = models.ForeignKey(
#         Archer,
#         on_delete=models.CASCADE,
#         unique=False,
#         verbose_name=_("owner archer"),
#         help_text=_("format: required"),
#         related_name='quivers'
#     )
#     quiver_type = models.ForeignKey(
#         QuiverType,
#         on_delete=models.PROTECT,
#         null=True,
#         blank=True,
#         unique=False,
#         verbose_name=_("quiver type"),
#         help_text=_("format: required"),
#         related_name='quivers'
#     )
#     quiver_material = models.ForeignKey(
#         QuiverMaterial,
#         on_delete=models.PROTECT,
#         null=True,
#         blank=True,
#         unique=False,
#         verbose_name=_("quiver material"),
#         help_text=_("format: required"),
#         related_name='quivers'
#     )

#     class Meta:
#         db_table = 'quiver'
#         ordering = ['archer__last_name']
#         verbose_name = _("Quiver")
#         verbose_name_plural = _("Quivers")

#     def __str__(self):
#         return f"{str(self.archer)} - {self.quiver_material.name} {self.quiver_type.name}"

# class TargetFace(BaseModel):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(
#         max_length=64,
#         null=False,
#         unique=True,
#         blank=False,
#         verbose_name=_("target face name"),
#         help_text=_("format: required, max-64")
#     )
#     # Target face diameters in cm: 20, 40, 60, 80, 122
#     diameter_cm = models.FloatField(
#         null=False,
#         unique=False,
#         blank=False,
#         verbose_name=_("target face diameter in cm"),
#         help_text=_("format: required"),
#     )

#     class Meta:
#         db_table = 'targetface'
#         ordering = ['name']
#         verbose_name = _("Target Face")
#         verbose_name_plural = _("Target Faces")

#     def __str__(self):
#         return self.name

#     def __unicode__(self):
#         return self.name

# class Target(BaseModel):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     target_face = models.ForeignKey(
#         TargetFace,
#         on_delete=models.PROTECT,
#         unique=False,
#         verbose_name=_("target face"),
#         help_text=_("format: required"),
#         related_name='targets'
#     )
#     # Target distances in meters: 18, 30, 50, 70, 90, 100, 122
#     distance_m = models.PositiveIntegerField(
#         null=False,
#         unique=False,
#         blank=False,
#         verbose_name=_("target distance in meters"),
#         help_text=_("format: required"),
#     )

#     class Meta:
#         db_table = 'target'
#         ordering = ['target_face__name']
#         verbose_name = _("Target")
#         verbose_name_plural = _("Targets")

#     def __str__(self):
#         return f"{self.target_face.name} - {self.distance_m}m"

#     def __unicode__(self):
#         return f"{self.target_face.name} - {self.distance_m}m"

# class NockingPoint(BaseModel):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(
#         max_length=64,
#         null=False,
#         unique=True,
#         blank=False,
#         verbose_name=_("nocking point name"),
#         help_text=_("format: required, max-64")
#     )

#     class Meta:
#         db_table = 'nockingpoint'
#         ordering = ['name']
#         verbose_name = _("Nocking Point")
#         verbose_name_plural = _("Nocking Points")

#     def __str__(self):
#         return self.name

#     def __unicode__(self):
#         return self.name

# # Sight Types: Pin, Aperture, Scope, Peep
# class Sight(BaseModel):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(
#         max_length=64,
#         null=False,
#         unique=True,
#         blank=False,
#         verbose_name=_("sight name"),
#         help_text=_("format: required, max-64")
#     )

#     class Meta:
#         db_table = 'sight'
#         ordering = ['name']
#         verbose_name = _("Sight")
#         verbose_name_plural = _("Sights")

#     def __str__(self):
#         return self.name

#     def __unicode__(self):
#         return self.name

# # Stabilizer Types: Rod, Bar, Side, V-Bar
# class Stabilizer(BaseModel):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(
#         max_length=64,
#         null=False,
#         unique=True,
#         blank=False,
#         verbose_name=_("stabilizer name"),
#         help_text=_("format: required, max-64")
#     )

#     class Meta:
#         db_table = 'stabilizer'
#         ordering = ['name']
#         verbose_name = _("Stabilizer")
#         verbose_name_plural = _("Stabilizers")

#     def __str__(self):
#         return self.name

#     def __unicode__(self):
#         return self.name

# class Clicker(BaseModel):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(
#         max_length=64,
#         null=False,
#         unique=True,
#         blank=False,
#         verbose_name=_("clicker name"),
#         help_text=_("format: required, max-64")
#     )

#     class Meta:
#         db_table = 'clicker'
#         ordering = ['name']
#         verbose_name = _("Clicker")
#         verbose_name_plural = _("Clickers")

#     def __str__(self):
#         return self.name

#     def __unicode__(self):
#         return self.name

# class Plunger(BaseModel):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(
#         max_length=64,
#         null=False,
#         unique=True,
#         blank=False,
#         verbose_name=_("plunger name"),
#         help_text=_("format: required, max-64")
#     )

#     class Meta:
#         db_table = 'plunger'
#         ordering = ['name']
#         verbose_name = _("Plunger")
#         verbose_name_plural = _("Plungers")

#     def __str__(self):
#         return self.name

#     def __unicode__(self):
#         return self.name

# # Finger Tab Types: Leather, Synthetic, Hybrid
# class FingerTab(BaseModel):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(
#         max_length=64,
#         null=False,
#         unique=True,
#         blank=False,
#         verbose_name=_("finger tab name"),
#         help_text=_("format: required, max-64")
#     )

#     class Meta:
#         db_table = 'fingertab'
#         ordering = ['name']
#         verbose_name = _("Finger Tab")
#         verbose_name_plural = _("Finger Tabs")

#     def __str__(self):
#         return self.name

#     def __unicode__(self):
#         return self.name

# class ArmGuard(BaseModel):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(
#         max_length=64,
#         null=False,
#         unique=True,
#         blank=False,
#         verbose_name=_("arm guard name"),
#         help_text=_("format: required, max-64")
#     )

#     class Meta:
#         db_table = 'armguard'
#         ordering = ['name']
#         verbose_name = _("Arm Guard")
#         verbose_name_plural = _("Arm Guards")

#     def __str__(self):
#         return self.name

#     def __unicode__(self):
#         return self.name

# class ChestGuard(BaseModel):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(
#         max_length=64,
#         null=False,
#         unique=True,
#         blank=False,
#         verbose_name=_("chest guard name"),
#         help_text=_("format: required, max-64")
#     )

#     class Meta:
#         db_table = 'chestguard'
#         ordering = ['name']
#         verbose_name = _("Chest Guard")
#         verbose_name_plural = _("Chest Guards")

#     def __str__(self):
#         return self.name

# class Riser(BaseModel):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(
#         max_length=64,
#         null=False,
#         unique=True,
#         blank=False,
#         verbose_name=_("riser name"),
#         help_text=_("format: required, max-64")
#     )

#     class Meta:
#         db_table = 'riser'
#         ordering = ['name']
#         verbose_name = _("Riser")
#         verbose_name_plural = _("Risers")

#     def __str__(self):
#         return self.name

#     def __unicode__(self):
#         return self.name

# # Limb Types: Upper, Lower, Solid, Takedown
# class LimbType(BaseModel):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(
#         max_length=64,
#         null=False,
#         unique=True,
#         blank=False,
#         verbose_name=_("limb type name"),
#         help_text=_("format: required, max-64")
#     )

#     class Meta:
#         db_table = 'limbtype'
#         ordering = ['name']
#         verbose_name = _("Limb Type")
#         verbose_name_plural = _("Limb Types")

#     def __str__(self):
#         return self.name

#     def __unicode__(self):
#         return self.name

# class Limb(BaseModel):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(
#         max_length=64,
#         null=False,
#         unique=True,
#         blank=False,
#         verbose_name=_("limb name"),
#         help_text=_("format: required, max-64")
#     )
#     limb_type = models.ForeignKey(
#         LimbType,
#         on_delete=models.PROTECT,
#         unique=False,
#         verbose_name=_("limb type"),
#         help_text=_("format: required"),
#         related_name='limbs'
#     )

#     class Meta:
#         db_table = 'limb'
#         ordering = ['name']
#         verbose_name = _("Limb")
#         verbose_name_plural = _("Limbs")

#     def __str__(self):
#         return self.name

#     def __unicode__(self):
#         return self.name

# # Handle Types: Wood, Aluminum, Composite
# class HandleType(BaseModel):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(
#         max_length=64,
#         null=False,
#         unique=True,
#         blank=False,
#         verbose_name=_("handle type name"),
#         help_text=_("format: required, max-64")
#     )

#     class Meta:
#         db_table = 'handletype'
#         ordering = ['name']
#         verbose_name = _("Handle Type")
#         verbose_name_plural = _("Handle Types")

#     def __str__(self):
#         return self.name

#     def __unicode__(self):
#         return self.name

# class Handle(BaseModel):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(
#         max_length=64,
#         null=False,
#         unique=True,
#         blank=False,
#         verbose_name=_("handle name"),
#         help_text=_("format: required, max-64")
#     )
#     handle_type = models.ForeignKey(
#         HandleType,
#         on_delete=models.PROTECT,
#         unique=False,
#         verbose_name=_("handle type"),
#         help_text=_("format: required"),
#         related_name='handles'
#     )

#     class Meta:
#         db_table = 'handle'
#         ordering = ['name']
#         verbose_name = _("Handle")
#         verbose_name_plural = _("Handles")

#     def __str__(self):
#         return self.name

#     def __unicode__(self):
#         return self.name

# # Biwstring Materials: Dacron, Fast Flight, BCY, Flemish Twist
# class BowStringMaterial(BaseModel):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(
#         max_length=64,
#         null=False,
#         unique=True,
#         blank=False,
#         verbose_name=_("string material name"),
#         help_text=_("format: required, max-64")
#     )

#     class Meta:
#         db_table = 'stringmaterial'
#         ordering = ['name']
#         verbose_name = _("String Material")
#         verbose_name_plural = _("String Materials")

#     def __str__(self):
#         return self.name

#     def __unicode__(self):
#         return self.name

# class BowString(BaseModel):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(
#         max_length=64,
#         null=False,
#         unique=True,
#         blank=False,
#         verbose_name=_("string name"),
#         help_text=_("format: required, max-64")
#     )
#     string_material = models.ForeignKey(
#         BowStringMaterial,
#         on_delete=models.PROTECT,
#         null=True,
#         blank=True,
#         unique=False,
#         verbose_name=_("bowstring material"),
#         help_text=_("format: required"),
#         related_name='bowstrings'
#     )

#     class Meta:
#         db_table = 'bowstring'
#         ordering = ['name']
#         verbose_name = _("Bow String")
#         verbose_name_plural = _("Bow Strings")

#     def __str__(self):
#         return self.name

#     def __unicode__(self):
#         return self.name

# # Arrow Rest Types: Shelf, Drop-away, Plunger
# class ArrowRestType(BaseModel):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(
#         max_length=64,
#         null=False,
#         unique=True,
#         blank=False,
#         verbose_name=_("arrow rest type name"),
#         help_text=_("format: required, max-64")
#     )

#     class Meta:
#         db_table = 'arrowresttype'
#         ordering = ['name']
#         verbose_name = _("Arrow Rest Type")
#         verbose_name_plural = _("Arrow Rest Types")

#     def __str__(self):
#         return self.name

#     def __unicode__(self):
#         return self.name

# class ArrowRest(BaseModel):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(
#         max_length=64,
#         null=False,
#         unique=True,
#         blank=False,
#         verbose_name=_("arrow rest name"),
#         help_text=_("format: required, max-64")
#     )
#     arrow_rest_type = models.ForeignKey(
#         ArrowRestType,
#         on_delete=models.PROTECT,
#         unique=False,
#         verbose_name=_("arrow rest type"),
#         help_text=_("format: required"),
#         related_name='arrowrests'
#     )

#     class Meta:
#         db_table = 'arrowrest'
#         ordering = ['name']
#         verbose_name = _("Arrow Rest")
#         verbose_name_plural = _("Arrow Rests")

#     def __str__(self):
#         return self.name

# ## Nocking Point Types: Brass, Plastic, Rubber
# class NockingPoint(BaseModel):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(
#         max_length=64,
#         null=False,
#         unique=True,
#         blank=False,
#         verbose_name=_("nocking point name"),
#         help_text=_("format: required, max-64")
#     )

#     class Meta:
#         db_table = 'nockingpoint'
#         ordering = ['name']
#         verbose_name = _("Nocking Point")
#         verbose_name_plural = _("Nocking Points")

#     def __str__(self):
#         return self.name

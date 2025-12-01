import uuid
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import AutoSlugField
from users.models import User
from wagtail.admin.panels import MultiFieldPanel, FieldPanel

class BaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Archer(BaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._meta.get_field('slug').populate_from = 'last_name'

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
    province = models.CharField(
        max_length=64,
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("state or province of archer"),
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
        FieldPanel('last_name'),
        FieldPanel('first_name'),
        FieldPanel('middle_name'),
        MultiFieldPanel(
            [
                FieldPanel('email'),
                FieldPanel('phone'),
                FieldPanel('address'),
                FieldPanel('city'),
                FieldPanel('zip_code'),
            ],
            heading = "Contact Information",
            classname="collapsible collapsed",
        ),
        MultiFieldPanel(
            [
                FieldPanel('birth_date'),
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
        self._meta.get_field('slug').populate_from = 'name'

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

    class Meta:
        db_table = 'membership'
        ordering = ['start_date']
        verbose_name = _("Membership")
        verbose_name_plural = _("Memberships")

    def __str__(self):
        return f"{str(self.archer)} - {str(self.club)} {self.club.town}"

    def __unicode__(self):
        return f"{str(self.archer)} - {str(self.club)} {self.club.town}"

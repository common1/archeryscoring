import uuid
from django.db import models
from django.utils import timezone
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from users.models import User
from wagtail.admin.panels import MultiFieldPanel, FieldPanel, FieldRowPanel
from django.core.validators import MaxValueValidator, MinValueValidator
from modeling.models import Archer

class ArcheryMaterialsBaseModel(models.Model):
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    modified_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    
    class Meta:
        abstract = True

#Wooden, Recurve, Longbow, Compound
class BowType(ArcheryMaterialsBaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=32,
        null=False,
        unique=True,
        blank=False,
        verbose_name=_("bow type name"),
        help_text=_("format: required, max-32")
    )
    slug = AutoSlugField(populate_from='name',editable=True)
    archers = models.ManyToManyField(
        Archer,
        through='BowTypeMembership',
        blank=True,
        help_text=_("format: not required"),
        related_name='bowtypes',
        verbose_name=_("archers in bowtype"),
    )
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("bowtype information"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='bowtype_author',
        verbose_name=_("author of bowtype"),
        help_text=_("format: required, default=1 (superuser)"),
    )

    class Meta:
        db_table = 'bowtype'
        ordering = ['name']
        verbose_name = _("Bow Type")
        verbose_name_plural = _("Bow Types")

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class BowTypeMembership(ArcheryMaterialsBaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    bowtype = models.ForeignKey(
        BowType,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("bowtypemembership bowtype"),
        help_text=_("format: required"),
        related_name='BowTypeMembership'
    )
    archer = models.ForeignKey(
        Archer,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("bowtypemembership archer"),        
        related_name='bowtypemembership_archer',
        help_text=_("format: required"),
    )

    # Extra fields for membership information

    slug = AutoSlugField(populate_from=('bowtype__name', 'archer__last_name',), editable=True)
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("bowtype information"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='bowtype_membership_author',
        verbose_name=_("author of bowtypemembership"),
        help_text=_("format: required, default=1 (superuser)"),
    )

    class Meta:
        db_table = 'bowtypemembership'
        ordering = ['bowtype__name']
        verbose_name = _("Bow Type Membership")
        verbose_name_plural = _("Bow Type Memberships")
    def __str__(self):
        return f"{str(self.archer)} - {str(self.bowtype)}"

    def __unicode__(self):
        return f"{str(self.archer)} - {str(self.bowtype)}"


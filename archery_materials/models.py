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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    created_at = models.DateTimeField(default=timezone.now, editable=False)
    modified_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    
    class Meta:
        abstract = True

# Compound, Recurve, Longbow, Crossbow
class BowType(ArcheryMaterialsBaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    name = models.CharField(
        max_length=32,
        null=False,
        unique=True,
        blank=False,
        verbose_name=_("Name"),
        help_text=_("format: required, max-32")
    )
    slug = AutoSlugField(populate_from='name',editable=True)
    archers = models.ManyToManyField(
        Archer,
        through='BowTypeMembership',
        blank=True,
        help_text=_("format: not required"),
        related_name='bowtypes',
        verbose_name=_("Archers"),
    )
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Info"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='bowtype_author',
        verbose_name=_("Author"),
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

    bowtype = models.ForeignKey(
        BowType,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("Bow type"),
        help_text=_("format: required"),
        related_name='BowTypeMembership'
    )
    archer = models.ForeignKey(
        Archer,
        on_delete=models.PROTECT,
        unique=False,
        verbose_name=_("Archer"),        
        related_name='bowtypemembership_archer',
        help_text=_("format: required"),
    )

    # Extra fields for membership information

    slug = AutoSlugField(populate_from=('bowtype__name', 'archer__last_name',), editable=True)
    info = models.TextField(
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("Info"),
        help_text=_("format: not required"),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        default=1,
        related_name='bowtype_membership_author',
        verbose_name=_("Author"),
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

class Sight(ArcheryMaterialsBaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Stabilizer(ArcheryMaterialsBaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Clicker(ArcheryMaterialsBaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Plunger(ArcheryMaterialsBaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class FingerTab(ArcheryMaterialsBaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ArmGuard(ArcheryMaterialsBaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ChestGuard(ArcheryMaterialsBaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

# Back quiver
# Hip Quiver
# Field Quiver
# Detachable Quiver
# Bow-Mounted Quiver
class QuiverType(ArcheryMaterialsBaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Quiver(ArcheryMaterialsBaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class LimbType(ArcheryMaterialsBaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Limb(ArcheryMaterialsBaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class RiserType(ArcheryMaterialsBaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Riser(ArcheryMaterialsBaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Bow(ArcheryMaterialsBaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class StringMaterial(ArcheryMaterialsBaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ArrowRestType(ArcheryMaterialsBaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class ArrowRest(ArcheryMaterialsBaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class NockingPoint(ArcheryMaterialsBaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class Equipment(ArcheryMaterialsBaseModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


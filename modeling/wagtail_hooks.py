from wagtail.admin.views.bulk_action import BulkAction
from wagtail import hooks
from wagtail_modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register
from django.utils.translation import gettext_lazy as _


from .models import (
    Archer,
    Club,
    ClubMembership,
    Category,
    CategoryMembership,
    Discipline,
    DisciplineMembership,
    Team,
    TeamMembership,
    ScoringSheet,
)


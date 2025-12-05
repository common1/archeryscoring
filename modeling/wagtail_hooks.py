from wagtail_modeladmin.options import ModelAdmin, modeladmin_register
from .models import (
    Archer,
    Club,
    ClubMembership,
    Category,
    CategoryMembership,
    Team,
    TeamMembership,
    ScoringSheet,
)

class ArcherHook(ModelAdmin):
    model = Archer
    base_url_path = "archerhook"
    menu_label = "Archer"
    menu_icon = "user"
    menu_order = 200
    add_to_settings_menu = True
    add_to_admin_menu = True
    list_display = ('union_number', 'last_name', 'first_name', 'middle_name',)
modeladmin_register(ArcherHook)

class ClubHook(ModelAdmin):
    model = Club
    base_url_path = "clubhook"
    menu_label = "Club"
    menu_icon = "home"
    menu_order = 210
    add_to_settings_menu = True
    add_to_admin_menu = True
    list_display = ('name', 'town',)
modeladmin_register(ClubHook)

class ClubMembershipHook(ModelAdmin):
    model = ClubMembership
    base_url_path="clubmembershiphook"
    menu_label = "ClubMembership"
    menu_icon = "list-ul"
    menu_order = 220
    add_to_settings_menu = True
    add_to_admin_menu = True
    list_display = ('archer', 'club',)
modeladmin_register(ClubMembershipHook)

class CategoryHook(ModelAdmin):
    model = Category
    base_url_path = "categoryhook"
    menu_label = "Category"
    menu_icon = "home"
    menu_order = 230
    add_to_settings_menu = True
    add_to_admin_menu = True
    list_display = ('name',)
modeladmin_register(CategoryHook)

class CategoryMembershipHook(ModelAdmin):
    model = CategoryMembership
    base_url_path = "categorymembershiphook"
    menu_label = "Category Membership"
    menu_icon = "list-ul"
    menu_order = 240
    add_to_settings_menu = True
    add_to_admin_menu = True
    list_display = ('category', 'archer', 'age_group',)
modeladmin_register(CategoryMembershipHook)

class TeamHook(ModelAdmin):
    model = Team
    base_url_path = "teamhook"
    menu_label = "Team"
    menu_icon = "group"
    menu_order = 250
    add_to_settings_menu = True
    add_to_admin_menu = True
    list_display = ('name',)
modeladmin_register(TeamHook)

class TeamMembershipHook(ModelAdmin):
    model = TeamMembership
    base_url_path = "teammembershiphook"
    menu_label = "Team Membership"
    menu_icon = "list-ul"
    menu_order = 260
    add_to_settings_menu = True
    add_to_admin_menu = True
    list_display = ('team', 'archer',)
modeladmin_register(TeamMembershipHook)

class ScoringSheetHook(ModelAdmin):
    model = ScoringSheet
    base_url_path = "scoringsheethook"
    menu_label = "Scoring Sheet"
    menu_icon = "doc-full"
    menu_order = 270
    add_to_settings_menu = True
    add_to_admin_menu = True
    list_display = ('name', 'date',)
modeladmin_register(ScoringSheetHook)

from wagtail_modeladmin.options import ModelAdmin, ModelAdminGroup, modeladmin_register

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

# class ArcherHook(ModelAdmin):
#     model = Archer
#     base_url_path = "archerhook"
#     menu_label = "Archer"
#     menu_icon = "user"
#     menu_order = 200
#     add_to_settings_menu = False
#     add_to_admin_menu = False
#     list_display = ('union_number', 'last_name', 'first_name', 'middle_name',)

# class ClubHook(ModelAdmin):
#     model = Club
#     base_url_path = "clubhook"
#     menu_label = "Club"
#     menu_icon = "home"
#     menu_order = 210
#     add_to_settings_menu = False
#     add_to_admin_menu = False
#     list_display = ('name', 'town',)

# class ClubMembershipHook(ModelAdmin):
#     model = ClubMembership
#     base_url_path="clubmembershiphook"
#     menu_label = "ClubMembership"
#     menu_icon = "list-ul"
#     menu_order = 220
#     add_to_settings_menu = False
#     add_to_admin_menu = False
#     list_display = ('archer', 'club',)

# class CategoryHook(ModelAdmin):
#     model = Category
#     base_url_path = "categoryhook"
#     menu_label = "Category"
#     menu_icon = "home"
#     menu_order = 230
#     add_to_settings_menu = False
#     add_to_admin_menu = False
#     list_display = ('name',)

# class CategoryMembershipHook(ModelAdmin):
#     model = CategoryMembership
#     base_url_path = "categorymembershiphook"
#     menu_label = "Category Membership"
#     menu_icon = "list-ul"
#     menu_order = 240
#     add_to_settings_menu = False
#     add_to_admin_menu = False
#     list_display = ('category', 'archer', 'age_group',)

# class TeamHook(ModelAdmin):
#     model = Team
#     base_url_path = "teamhook"
#     menu_label = "Team"
#     menu_icon = "group"
#     menu_order = 250
#     add_to_settings_menu = False
#     add_to_admin_menu = False
#     list_display = ('name',)

# class TeamMembershipHook(ModelAdmin):
#     model = TeamMembership
#     base_url_path = "teammembershiphook"
#     menu_label = "Team Membership"
#     menu_icon = "list-ul"
#     menu_order = 260
#     add_to_settings_menu = False
#     add_to_admin_menu = False
#     list_display = ('team', 'archer',)

# class ScoringSheetHook(ModelAdmin):
#     model = ScoringSheet
#     base_url_path = "scoringsheethook"
#     menu_label = "Scoring Sheet"
#     menu_icon = "doc-full"
#     menu_order = 270
#     add_to_settings_menu = False
#     add_to_admin_menu = False
#     list_display = ('name', 'date',)

# class DisciplineHook(ModelAdmin):
#     model = Discipline
#     base_url_path = "disciplinehook"
#     menu_label = "Discipline"
#     menu_icon = "list-ul"
#     menu_order = 280
#     add_to_settings_menu = False
#     add_to_admin_menu = False
#     list_display = ('name',)

# class DisciplineMembershipHook(ModelAdmin):
#     model = DisciplineMembership
#     base_url_path = "disciplinemembershiphook"
#     menu_label = "Discipline Membership"
#     menu_icon = "list-ul"
#     menu_order = 290
#     add_to_settings_menu = False
#     add_to_admin_menu = False
#     list_display = ('discipline', 'archer',)

# Define a ModelAdminGroup to group all the modeling related admin views

# class ModelingAdminGroup(ModelAdminGroup):
#     menu_label = "Modeling"
#     menu_icon = "folder-open-inverse"
#     menu_order = 200
#     items = (
#         ArcherHook,
#         ClubHook,
#         ClubMembershipHook,
#         CategoryHook,
#         CategoryMembershipHook,
#         TeamHook,
#         TeamMembershipHook,
#         ScoringSheetHook,
#         DisciplineHook,
#         DisciplineMembershipHook,
#     )
# modeladmin_register(ModelingAdminGroup)

# ------------------
# Snippet section
# ------------------


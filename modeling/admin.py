from django.contrib import admin
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

@admin.register(Archer)
class ArcherAdmin(admin.ModelAdmin):
    list_display = ('union_number', 'last_name', 'first_name', 'middle_name')
    list_display_links = ('last_name', 'first_name')
    list_per_page = 20
    ordering = ('last_name', 'first_name')
    fieldsets = (
        (None, {
            'fields': ( 'union_number', 'last_name', 'first_name', 'middle_name', 'info',)
        }),
        ('Contact Information', {
            'classes': ['collapse'],
            'fields': ('email', 'phone', 'address', 'city', 'zip_code', 'province',),
        }),
        ('Extra Information', {
            'classes': ['collapse'],
            'fields': ('birth_date', 'slug', 'author'),
        }),
    )
    search_fields = ('last_name', 'first_name', 'middle_name')

class ClubMembershipInline(admin.TabularInline):
    model = ClubMembership
    extra = 1
    fields = ('archer', 'start_date', 'end_date')
    can_delete = False
    show_change_link = True

@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    inlines = [
        ClubMembershipInline
    ]
    list_display = ('name', 'town')
    list_display_links = ('name', 'town')
    list_per_page = 20
    ordering = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'info')
        }),
        ('Contact Information', {
            'classes': ['collapse'],
            'fields': (
                'address', 
                'zip_code', 
                'town',
                'phone',
                'email',
                'website',
                'social_media',
            ),
        }),
        ('Extra Information', {
            'classes': ['collapse'],
            'fields': ('slug', 'author'),
        }),
    )
    search_fields = ('name', 'town')

@admin.register(ClubMembership)
class ClubMembershipAdmin(admin.ModelAdmin):
    list_display = ('archer', 'club', 'start_date', 'end_date')
    list_display_links = ('archer',)
    list_per_page = 20
    ordering = ('club', 'archer',)
    fieldsets = (
        (None, {
            'fields': ('club','archer', 'info')
        }),
        ('Extra Information', {
            'classes': ['collapse'],
            'fields': (
                'slug', 
                'author',
                'start_date', 
                'end_date',
            ),
        }),
    )
    search_fields = ('archer__last_name', 'club__name')

class CategoryMembershipInline(admin.TabularInline):
    model = CategoryMembership
    extra = 1
    fields = ('category', 'archer', 'agegroup')
    can_delete = False
    show_change_link = True

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        CategoryMembershipInline
    ]
    list_display = ('name',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'info',)
        }),
        ('Extra Information', {
            'classes': ['collapse'],
            'fields': (
                'slug', 
                'author', 
            ),
        }),
    )
    search_fields = ('name', 'info')

@admin.register(CategoryMembership)
class CategoryMembershipAdmin(admin.ModelAdmin):
    list_display = ('category', 'archer', 'agegroup',)
    list_display_links = ('category', 'archer',)
    list_per_page = 20
    ordering = ('category', 'archer')
    fieldsets = (
        (None, {
            'fields': (
                'category', 
                'archer', 
                'agegroup', 
                'info', 
            )
        }),
        ('Extra Information', {
            'classes': ['collapse'],
            'fields': ('slug', 'author'),
        }),
    )
    search_fields = ('category__name', 'archer__name')

class DisciplineMembershipInline(admin.TabularInline):
    model = DisciplineMembership
    extra = 1
    fields = ('discipline', 'archer',)
    can_delete = False
    show_change_link = True
    
@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    inlines = [
        DisciplineMembershipInline
    ]
    list_display = ('name',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'info',)
        }),
        ('Extra Information', {
            'classes': ['collapse'],
            'fields': (
                'slug', 
                'author', 
            ),
        }),
    )
    search_fields = ('name', 'info')
    
@admin.register(DisciplineMembership)
class DisciplineMembershipAdmin(admin.ModelAdmin):
    list_display = ('discipline', 'archer',)
    list_display_links = ('discipline', 'archer',)
    list_per_page = 20
    ordering = ('discipline', 'archer',)
    fieldsets = (
        (None, {
            'fields': (
                'discipline', 
                'archer', 
                'info', 
            )
        }),
        ('Extra Information', {
            'classes': ['collapse'],
            'fields': ('slug', 'author'),
        }),
    )
    search_fields = ('discipline__name', 'archer__name')
    
class TeamMembershipInline(admin.TabularInline):
    model = TeamMembership
    extra = 1
    fields = ('team', 'archer',)
    can_delete = False
    show_change_link = True

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    inlines = [
        TeamMembershipInline
    ]
    list_display = ('name',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'info',)
        }),
        ('Extra Information', {
            'classes': ['collapse'],
            'fields': ('slug', 'author',),
        }),
    )
    search_fields = ('name',)

@admin.register(TeamMembership)
class TeamMembershipAdmin(admin.ModelAdmin):
    list_display = ('team', 'archer',)
    list_display_links = ('team', 'archer',)
    list_per_page = 20
    ordering = ('team', 'archer',)
    fieldsets = (
        (None, {
            'fields': ('team', 'archer', 'info',)
        }),
        ('Extra Information', {
            'classes': ['collapse'],
            'fields': ('slug', 'author',),
        }),
    )
    search_fields = ('team__name', 'archer__name')
    
@admin.register(ScoringSheet)
class ScoringSheetAdmin(admin.ModelAdmin):
    list_display = ('name', 'columns', 'rows')
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'columns', 'rows', 'info',)
        }),
        ('Extra Information', {
            'classes': ['collapse'],
            'fields': ('slug', 'author',),
        }),
    )
    search_fields = ('name', 'info')
    
# Snippets

from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from wagtail.snippets.models import register_snippet
from wagtail.admin.ui.tables import BooleanColumn   

class ArcherSnippetViewSet(SnippetViewSet):
    model = Archer
    menu_label = "Archer"
    menu_icon = "user"
    menu_order = 10
    add_to_settings_menu = False
    add_to_admin_menu = False
    list_display = ('union_number', 'last_name', 'first_name', 'middle_name', BooleanColumn('is_active'),)

class ClubSnippetViewSet(SnippetViewSet):
    model = Club
    menu_label = "Club"
    menu_icon = "home"
    menu_order = 20
    add_to_settings_menu = False
    add_to_admin_menu = False
    list_display = ('name', 'town', BooleanColumn('is_active'),)

class ClubMembershipViewSet(SnippetViewSet):
    model = ClubMembership
    base_url_path="clubmembershiphook"
    menu_label = "ClubMembership"
    menu_icon = "list-ul"
    menu_order = 30
    add_to_settings_menu = False
    add_to_admin_menu = False
    list_display = ('archer', 'club',)

class CategoryViewSet(SnippetViewSet):
    model = Category
    menu_label = "Category"
    menu_icon = "home"
    menu_order = 40
    add_to_settings_menu = False
    add_to_admin_menu = False
    list_display = ('name',)

class CategoryMembershipViewSet(SnippetViewSet):
    model = CategoryMembership
    menu_label = "Category Membership"
    menu_icon = "list-ul"
    menu_order = 50
    add_to_settings_menu = False
    add_to_admin_menu = False
    list_display = ('category', 'archer', 'agegroup',)

class TeamViewSet(SnippetViewSet):
    model = Team
    menu_label = "Team"
    menu_icon = "group"
    menu_order = 60
    add_to_settings_menu = False
    add_to_admin_menu = False
    list_display = ('name',)

class TeamMembershipViewSet(SnippetViewSet):
    model = TeamMembership
    menu_label = "Team Membership"
    menu_icon = "list-ul"
    menu_order = 70
    add_to_settings_menu = False
    add_to_admin_menu = False
    list_display = ('team', 'archer',)

class ScoringSheetViewSet(SnippetViewSet):
    model = ScoringSheet
    menu_label = "Scoring Sheet"
    menu_icon = "doc-full"
    menu_order = 80
    add_to_settings_menu = False
    add_to_admin_menu = False
    list_display = ('name', 'columns', 'rows',)

class DisciplineViewSet(SnippetViewSet):
    model = Discipline
    menu_label = "Discipline"
    menu_icon = "list-ul"
    menu_order = 280
    add_to_settings_menu = False
    add_to_admin_menu = False
    list_display = ('name',)

class DisciplineMembershipViewSet(SnippetViewSet):
    model = DisciplineMembership
    menu_label = "Discipline Membership"
    menu_icon = "list-ul"
    menu_order = 290
    add_to_settings_menu = False
    add_to_admin_menu = False
    list_display = ('discipline', 'archer',)

class ModelingSnippetViewSetGroup(SnippetViewSetGroup):
    menu_label = "Modeling Snippets"
    menu_icon = "folder-open-inverse"
    menu_order = 300
    items = (
        ArcherSnippetViewSet,
        ClubSnippetViewSet,
        ClubMembershipViewSet,
        CategoryViewSet,
        CategoryMembershipViewSet,
        TeamViewSet,
        TeamMembershipViewSet,
        ScoringSheetViewSet,
        DisciplineViewSet,
        DisciplineMembershipViewSet,
    )
register_snippet(ModelingSnippetViewSetGroup)    

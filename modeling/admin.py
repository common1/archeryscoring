from django.contrib import admin
from .models import (
    Archer,
    AgeGroup,
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
    list_display = ('last_name', 'first_name', 'middle_name', 'union_number',)
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

@admin.register(AgeGroup)
class AgeGroupAdmin(admin.ModelAdmin):
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
    
# Wagtail Snippets

from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from wagtail.snippets.models import register_snippet
from wagtail.admin.ui.tables import BooleanColumn
from wagtail.admin.panels import MultiFieldPanel, FieldPanel, FieldRowPanel

class ArcherSnippetViewSet(SnippetViewSet):
    model = Archer
    menu_label = "Archers"
    menu_icon = "user"
    menu_order = 10
    add_to_settings_menu = False
    add_to_admin_menu = False
    list_display = ('last_name', 'first_name', 'middle_name', 'union_number', BooleanColumn('is_active'),)

    panels = [
        FieldPanel('last_name'),
        FieldPanel('first_name'),
        FieldPanel('middle_name'),
        FieldPanel('union_number'),
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

class AgeGroupSnippetViewSet(SnippetViewSet):
    model = AgeGroup
    menu_label = "Age Groups"
    menu_icon = "user"
    menu_order = 20
    add_to_settings_menu = False
    add_to_admin_menu = False
    list_display = ('name', BooleanColumn('is_active'),)

    panels = [
        FieldPanel('name'),
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

class ClubSnippetViewSet(SnippetViewSet):
    model = Club
    menu_label = "Clubs"
    menu_icon = "home"
    menu_order = 30
    add_to_settings_menu = False
    add_to_admin_menu = False
    list_display = ('name', 'town', BooleanColumn('is_active'),)

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

class ClubMembershipSnippetViewSet(SnippetViewSet):
    model = ClubMembership
    base_url_path="clubmembershiphook"
    menu_label = "Club Memberships"
    menu_icon = "list-ul"
    menu_order = 40
    add_to_settings_menu = False
    add_to_admin_menu = False
    list_display = ('archer', 'club', BooleanColumn('is_active'),)

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

class CategorySnippetViewSet(SnippetViewSet):
    model = Category
    menu_label = "Categories"
    menu_icon = "home"
    menu_order = 50
    add_to_settings_menu = False
    add_to_admin_menu = False
    list_display = ('name', BooleanColumn('is_active'),)

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

class CategoryMembershipSnippetViewSet(SnippetViewSet):
    model = CategoryMembership
    menu_label = "Category Memberships"
    menu_icon = "list-ul"
    menu_order = 60
    add_to_settings_menu = False
    add_to_admin_menu = False
    list_display = ('category', 'archer', 'agegroup', BooleanColumn('is_active'),)

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

class TeamSnippetViewSet(SnippetViewSet):
    model = Team
    menu_label = "Teams"
    menu_icon = "group"
    menu_order = 70
    add_to_settings_menu = False
    add_to_admin_menu = False
    list_display = ('name', BooleanColumn('is_active'),)

class TeamMembershipSnippetViewSet(SnippetViewSet):
    model = TeamMembership
    menu_label = "Team Memberships"
    menu_icon = "list-ul"
    menu_order = 80
    add_to_settings_menu = False
    add_to_admin_menu = False
    list_display = ('team', 'archer', BooleanColumn('is_active'),)

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

class ScoringSheetSnippetViewSet(SnippetViewSet):
    model = ScoringSheet
    menu_label = "Scoring Sheets"
    menu_icon = "doc-full"
    menu_order = 90
    add_to_settings_menu = False
    add_to_admin_menu = False
    list_display = ('name', 'columns', 'rows', BooleanColumn('is_active'),)

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
    
class DisciplineSnippetViewSet(SnippetViewSet):
    model = Discipline
    menu_label = "Disciplines"
    menu_icon = "list-ul"
    menu_order = 100
    add_to_settings_menu = False
    add_to_admin_menu = False
    list_display = ('name', BooleanColumn('is_active'),)

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

class DisciplineMembershipSnippetViewSet(SnippetViewSet):
    model = DisciplineMembership
    menu_label = "Discipline Memberships"
    menu_icon = "list-ul"
    menu_order = 110
    add_to_settings_menu = False
    add_to_admin_menu = False
    list_display = ('discipline', 'archer', BooleanColumn('is_active'),)

    panels = [
        FieldPanel('discipline'),
        FieldPanel('archer'),
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

class ModelingSnippetViewSetGroup(SnippetViewSetGroup):
    menu_label = "Modeling Snippets"
    menu_icon = "folder-open-inverse"
    menu_order = 300
    items = (
        AgeGroupSnippetViewSet,
        ArcherSnippetViewSet,
        CategorySnippetViewSet,
        CategoryMembershipSnippetViewSet,
        ClubSnippetViewSet,
        ClubMembershipSnippetViewSet,
        DisciplineSnippetViewSet,
        DisciplineMembershipSnippetViewSet,
        ScoringSheetSnippetViewSet,
        TeamSnippetViewSet,
        TeamMembershipSnippetViewSet,
    )
register_snippet(ModelingSnippetViewSetGroup)    

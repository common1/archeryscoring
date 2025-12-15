from django.contrib import admin

from .models import (
    BowType,
    BowTypeMembership,
)

from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from wagtail.snippets.models import register_snippet
from wagtail.admin.ui.tables import BooleanColumn
from wagtail.admin.panels import MultiFieldPanel, FieldPanel, FieldRowPanel

@admin.action(description="Activate selected Bow Types")
def activate_bowtypes(modeladmin, request, queryset):
    queryset.update(is_active=True)

@admin.action(description="Deactivate selected Bow Types")
def deactivate_bowtypes(modeladmin, request, queryset):
    queryset.update(is_active=False)

class BowTypeMembershipInline(admin.TabularInline):
    model = BowTypeMembership
    extra = 1
    fields = ('archer',)
    can_delete = False
    show_change_link = True
    
@admin.register(BowType)
class BowTypeAdmin(admin.ModelAdmin):
    actions=[activate_bowtypes, deactivate_bowtypes]
    inlines = [
        BowTypeMembershipInline
    ]
    list_display = ('name', 'is_active',)
    list_filter = ('is_active',)
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
        ('Special', {
            'classes': ['collapse'],
            'fields': ('is_active',),
        }),
    )
    search_fields = ('name',)

@admin.action(description="Activate selected Bow Type Memberships")
def activate_bowtype_memberships(modeladmin, request, queryset):
    queryset.update(is_active=True)

@admin.action(description="Deactivate selected Bow Type Memberships")
def deactivate_bowtype_memberships(modeladmin, request, queryset):
    queryset.update(is_active=False)

@admin.register(BowTypeMembership)
class BowTypeMembershipAdmin(admin.ModelAdmin):
    actions=[activate_bowtype_memberships, deactivate_bowtype_memberships]
    list_display = ('bowtype', 'archer', 'is_active',)
    list_filter = ('is_active',)
    list_display_links = ('bowtype', 'archer',)
    list_per_page = 20
    ordering = ('bowtype', 'archer',)
    fieldsets = (
        (None, {
            'fields': ('bowtype', 'archer', 'info',)
        }),
        ('Extra Information', {
            'classes': ['collapse'],
            'fields': ('slug', 'author',),
        }),
        ('Special', {
            'classes': ['collapse'],
            'fields': ('is_active',),
        }),
    )
    search_fields = ('bowtype__name', 'archer__name')
    
# Wagtail Snippets

class BowTypeSnippetViewSet(SnippetViewSet):
    actions=[activate_bowtypes, deactivate_bowtypes]
    model = BowType
    menu_label = "Bow Types"
    menu_icon = "folder-open-inverse"
    menu_order = 10
    add_to_settings_menu = False
    add_to_admin_menu = False
    list_display = ('name', BooleanColumn('is_active'),)
    list_filter = ('is_active',)

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
        MultiFieldPanel(
            [
                FieldPanel('is_active'),
            ],
            heading = "Special",
            classname="collapsible collapsed",
        ),
    ]

class BowTypeMembershipSnippetViewSet(SnippetViewSet):
    model = BowTypeMembership
    menu_label = "Bow Type Memberships"
    menu_icon = "folder-open-inverse"
    menu_order = 20
    add_to_settings_menu = False
    add_to_admin_menu = False
    list_display = ('bowtype', 'archer', BooleanColumn('is_active'),)
    list_filter = ('is_active',)

    panels = [
        FieldPanel('bowtype'),
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
        MultiFieldPanel(
            [
                FieldPanel('is_active'),
            ],
            heading = "Special",
            classname="collapsible collapsed",
        ),
    ]

class MaterialSnippetViewSetGroup(SnippetViewSetGroup):
    menu_label = "Material Snippets"
    menu_icon = "folder-open-inverse"
    menu_order = 310
    items = (
        BowTypeSnippetViewSet,
        BowTypeMembershipSnippetViewSet,
    )
register_snippet(MaterialSnippetViewSetGroup)    

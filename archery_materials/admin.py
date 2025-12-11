from django.contrib import admin

from .models import (
    BowType,
    BowTypeMembership,
)

class BowTypeMembershipInline(admin.TabularInline):
    model = BowTypeMembership
    extra = 1
    fields = ('archer',)
    can_delete = False
    show_change_link = True
    
@admin.register(BowType)
class BowTypeAdmin(admin.ModelAdmin):
    inlines = [
        BowTypeMembershipInline
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

@admin.register(BowTypeMembership)
class BowTypeMembershipAdmin(admin.ModelAdmin):
    list_display = ('bowtype', 'archer',)
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
    )
    search_fields = ('bowtype__name', 'archer__name')
    
# Wagtail Snippets

from wagtail.snippets.views.snippets import SnippetViewSet, SnippetViewSetGroup
from wagtail.snippets.models import register_snippet
from wagtail.admin.ui.tables import BooleanColumn   
from wagtail.admin.panels import MultiFieldPanel, FieldPanel, FieldRowPanel

class BowTypeSnippetViewSet(SnippetViewSet):
    model = BowType
    menu_label = "Bow Types"
    menu_icon = "folder-open-inverse"
    menu_order = 10
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

class BowTypeMembershipSnippetViewSet(SnippetViewSet):
    model = BowTypeMembership
    menu_label = "Bow Type Memberships"
    menu_icon = "folder-open-inverse"
    menu_order = 20
    add_to_settings_menu = False
    add_to_admin_menu = False
    list_display = ('bowtype', 'archer', BooleanColumn('is_active'),)

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

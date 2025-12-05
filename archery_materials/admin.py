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
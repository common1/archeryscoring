from django.contrib import admin
from .models import (
    Archer,
    Club,
    ClubMembership
)

@admin.register(Archer)
class ArcherAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name')
    list_display_links = ('last_name', 'first_name')
    list_per_page = 20
    ordering = ('last_name', 'first_name')
    fieldsets = (
        (None, {
            'fields': ('first_name', 'middle_name', 'last_name', )
        }),
        ('Contact Information', {
            'classes': ['collapse'],
            'fields': ('email', 'phone', 'address', 'city', 'zip_code',),
        }),
        ('Extra Information', {
            'classes': ['collapse'],
            'fields': ('birth_date',),
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
            'fields': ('name', 'town')
        }),
    )

@admin.register(ClubMembership)
class ClubMembershipAdmin(admin.ModelAdmin):
    list_display = ('archer', 'club', 'start_date', 'end_date')
    list_display_links = ('archer',)
    list_per_page = 20
    ordering = ('archer', 'club')
    fieldsets = (
        (None, {
            'fields': ('archer', 'club', 'start_date', 'end_date')
        }),
    )
    search_fields = ('archer__last_name', 'club__name')

from django.contrib import admin
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
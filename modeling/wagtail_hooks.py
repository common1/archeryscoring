from wagtail_modeladmin.options import ModelAdmin, modeladmin_register
from .models import (
    Archer,
    Club,
    ClubMembership,
    Category,
    CategoryMembership,
)

class ArcherAdmin(ModelAdmin):
    model = Archer
    base_url_path = "archeradmin"
    menu_label = "Archer"
    menu_icon = "user"
    menu_order = 200
    add_to_settings_menu = True
    add_to_admin_menu = True
    list_display = ('union_number', 'last_name', 'first_name', 'middle_name',)

modeladmin_register(ArcherAdmin)

class ClubAdmin(ModelAdmin):
    model = Club
    base_url_path = "clubadmin"
    menu_label = "Club"
    menu_icon = "home"
    menu_order = 210
    add_to_settings_menu = True
    add_to_admin_menu = True
    list_display = ('name', 'town',)
modeladmin_register(ClubAdmin)

class ClubMembershipAdmin(ModelAdmin):
    model = ClubMembership
    base_url_path="clubmembershipadmin"
    menu_label = "ClubMembership"
    menu_icon = "list-ul"
    menu_order = 220
    add_to_settings_menu = True
    add_to_admin_menu = True
    list_display = ('archer', 'club',)
modeladmin_register(ClubMembershipAdmin)

class CategoryAdmin(ModelAdmin):
    model = Category
    base_url_path = "categoryadmin"
    menu_label = "Category"
    menu_icon = "home"
    menu_order = 230
    add_to_settings_menu = True
    add_to_admin_menu = True
    list_display = ('name',)
modeladmin_register(CategoryAdmin)

class CategoryMembershipAdmin(ModelAdmin):
    model = CategoryMembership
    base_url_path = "categorymembershipadmin"
    menu_label = "Category Membership"
    menu_icon = "list-ul"
    menu_order = 240
    add_to_settings_menu = True
    add_to_admin_menu = True
    list_display = ('category', 'archer', 'age_group',)
modeladmin_register(CategoryMembershipAdmin)

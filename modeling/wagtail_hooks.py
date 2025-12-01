from wagtail_modeladmin.options import ModelAdmin, modeladmin_register
from .models import (
    Archer,
    Club
)

class ArcherAdmin(ModelAdmin):
    model = Archer
    base_url_path = "archeradmin"
    menu_label = "Archer"
    menu_icon = "user"
    menu_order = 200
    add_to_settings_menu = True
    add_to_admin_menu = True
modeladmin_register(ArcherAdmin)

class ClubAdmin(ModelAdmin):
    model = Club
    base_url_path = "clubadmin"
    menu_label = "Club"
    menu_icon = "home"
    menu_order = 210
    add_to_settings_menu = True
    add_to_admin_menu = True
modeladmin_register(ClubAdmin)



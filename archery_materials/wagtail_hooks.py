from wagtail_modeladmin.options import ModelAdmin, modeladmin_register

from .models import (
    BowType,
    BowTypeMembership,
)

class BowTypeHook(ModelAdmin):
    model = BowType
    base_url_path = "bowtypehook"
    menu_label = "Bow Type"
    menu_icon = "folder-open-inverse"
    menu_order = 240
    add_to_settings_menu = True
    add_to_admin_menu = True
    list_display = ('name',)
modeladmin_register(BowTypeHook)

class BowTypeMembershipHook(ModelAdmin):
    model = BowTypeMembership
    base_url_path = "bowtypemembershiphook"
    menu_label = "Bow Type Membership"
    menu_icon = "folder-open-inverse"
    menu_order = 241
    add_to_settings_menu = True
    add_to_admin_menu = True
    list_display = ('bowtype', 'archer',)
modeladmin_register(BowTypeMembershipHook)


from django.contrib import admin

from .models import Grid_10x3, Grid_5x5

@admin.register(Grid_10x3)
class Grid_10x3Admin(admin.ModelAdmin):
    fieldsets = (
        ('Serie 1', {
            'fields': (('x1y1', 'x2y1', 'x3y1'),),
        }),
        ('Serie 2', {
            'fields': (('x1y2', 'x2y2', 'x3y2'),),
        }),
        ('Serie 3', {
            'fields': (('x1y3', 'x2y3', 'x3y3'),),
        }),
        ('Serie 4', {
            'fields': (('x1y4', 'x2y4', 'x3y4'),),
        }),
        ('Serie 5', {
            'fields': (('x1y5', 'x2y5', 'x3y5'),),
        }),
        ('Serie 6', {
            'fields': (('x1y6', 'x2y6', 'x3y6'),),
        }),
        ('Serie 7', {
            'fields': (('x1y7', 'x2y7', 'x3y7'),),
        }),
        ('Serie 8', {
            'fields': (('x1y8', 'x2y8', 'x3y8'),),
        }),
        ('Serie 9', {
            'fields': (('x1y9', 'x2y9', 'x3y9'),),
        }),
        ('Serie 10', {
            'fields': (('x1y10', 'x2y10', 'x3y10'),),
        }),
    )

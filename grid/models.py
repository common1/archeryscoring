from django.db import models

class BaseCell(models.Model):
    value = models.PositiveIntegerField(default=0, blank=False, null=False)

class Grid_10x3(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # Serie 1
    x1y1 = BaseCell()
    x2y1 = BaseCell()
    x3y1 = BaseCell()
    # Serie 2
    x1y2 = BaseCell()
    x2y2 = BaseCell()
    x3y2 = models.PositiveIntegerField()
    # Serie 3
    x1y3 = BaseCell()
    x2y3 = BaseCell()
    x3y3 = BaseCell()
    # Serie 4
    x1y4 = BaseCell()
    x2y4 = BaseCell()
    x3y4 = BaseCell()
    # Serie 5
    x1y5 = BaseCell()
    x2y5 = BaseCell()
    x3y5 = BaseCell()
    # Serie 6
    x1y6 = BaseCell()
    x2y6 = BaseCell()
    x3y6 = BaseCell()
    # Serie 7
    x1y7 = BaseCell()
    x2y7 = BaseCell()
    x3y7 = BaseCell()
    # Serie 8
    x1y8 = BaseCell()
    x2y8 = BaseCell()
    x3y8 = BaseCell()
    # Serie 9
    x1y9 = BaseCell()
    x2y9 = BaseCell()
    x3y9 = BaseCell()
    # Serie 10
    x1y10 = BaseCell()
    x2y10 = BaseCell()
    x3y10 = BaseCell()

    class Meta:
        db_table = "grid_10x3"
        verbose_name = "10x3 Grid"
        verbose_name_plural = "10x3 Grids"

class Grid_5x5(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    # Serie 1
    x1y1 = BaseCell()
    x2y1 = BaseCell()
    x3y1 = BaseCell()
    x4y1 = BaseCell()
    x5y1 = BaseCell()
    # Serie 2
    x1y2 = BaseCell()
    x2y2 = BaseCell()
    x3y2 = BaseCell()
    x4y2 = BaseCell()
    x5y2 = BaseCell()
    # Serie 3
    x1y3 = BaseCell()
    x2y3 = BaseCell()
    x3y3 = BaseCell()
    x4y3 = BaseCell()
    x5y3 = BaseCell()
    # Serie 4
    x1y4 = BaseCell()
    x2y4 = BaseCell()
    x3y4 = BaseCell()
    x4y4 = BaseCell()
    x5y4 = BaseCell()
    # Serie 5
    x1y5 = BaseCell()
    x2y5 = BaseCell()
    x3y5 = BaseCell()
    x4y5 = BaseCell()
    x5y5 = BaseCell()

    class Meta:
        db_table = "grid_5x5"
        verbose_name = "5x5 Grid"
        verbose_name_plural = "5x5 Grids"


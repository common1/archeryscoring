from django.db import models

class GridItem(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.position_x = self.x
        self.position_y = self.y
        self.value = self.value

    x = models.PositiveIntegerField()
    y = models.PositiveIntegerField()
    value = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.value}"
    
class AbstractGrid(models.Model):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    name = models.CharField(max_length=64)
    items = models.ManyToManyField(GridItem)

    def __str__(self):
        return self.name

    def add_item(self, item):
        self.items.add(item)

    def remove_item(self, item):
        self.items.remove(item)

    def get_items(self):
        return self.items.all()

    def clear_items(self):
        self.items.clear()

    def get_item_at_position(self, x, y):
        return self.items.filter(position_x=x, position_y=y).first() or None
    
    def move_item(self, item, new_x, new_y):
        if item in self.items.all():
            item.position_x = new_x
            item.position_y = new_y
            item.save()
            
    class Meta:
        abstract = True

class Indoor18MetersGrid(AbstractGrid):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def create_grid(self):
        for y in range(10):
            for x in range(3):
                item = GridItem.objects.create(x=x, y=y, value=0)
                self.add_item(item)

    class Meta:
        verbose_name = "Indoor 18 Meters Grid"
        verbose_name_plural = "Indoor 18 Meters Grids"

class Indoor25MetersGrid(AbstractGrid):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def create_grid(self):
        for y in range(5):
            for x in range(5):
                item = GridItem.objects.create(x=x, y=y, value=0)
                self.add_item(item)

    class Meta:
        verbose_name = "Indoor 25 Meters Grid"
        verbose_name_plural = "Indoor 25 Meters Grids"

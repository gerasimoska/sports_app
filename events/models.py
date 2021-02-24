from django.db import models
from django.utils import timezone


class CommonInfo(models.Model):
    start = models.DateTimeField(blank=True, default=timezone.now)
    end = models.DateTimeField(blank=True, default=timezone.now)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500)

    class Meta:
        abstract = True

    def __str__(self):
        return f"({self.title}, {self.description}) ({self.start} - {self.end})"


class Training(CommonInfo):
    pass


class Meal(CommonInfo):
    pass

from django.db import models


# Create your models here.
class Task(models.Model):
    """
    Task model for the API, created following the ERD diagram loacted in README.md
    """

    title = models.CharField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    status = models.BooleanField(default=False)
    due_date = models.DateField()
    due_time = models.TimeField()

    class Meta:
        ordering = ["due_date"]

    def __str__(self):
        return f"{self.title} | due: {self.due_date}"

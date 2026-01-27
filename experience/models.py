from django.db import models


class Experience(models.Model):
    EXP_TYPES = [
        ('ACAD', 'Academic Experience'),
        ('PROF', 'Professional Experience'),
    ]

    title = models.CharField(max_length=200)  # e.g., Junior Developer or Research Assistant
    company = models.CharField(max_length=200)  # e.g., Tech Corp or University Lab
    category = models.CharField(max_length=10, choices=EXP_TYPES, default='PROF')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  # Leave blank for "Present"
    description = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.company}"
from django.db import models

class Skill(models.Model):
        name = models.CharField(max_length=100)
        proficiency = models.IntegerField(default=100,help_text="Enter value between 1 and 100")

        # New field to distinguish skill types
        CATEGORY_CHOICES = [
            ('tech', 'Technical'),
            ('prof', 'Professional'),
        ]
        category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='tech')

        def __str__(self):
            return self.name
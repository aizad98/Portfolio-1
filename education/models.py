from django.db import models

class Education(models.Model):
    institute = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_year = models.IntegerField()
    # End year is CharField to allow "Present"
    end_year = models.CharField(max_length=20, default="Present")
    description = models.TextField()

    def __str__(self):
        return f"{self.degree} at {self.institute}"
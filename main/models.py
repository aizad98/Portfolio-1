from django.db import models

class HeroSection(models.Model):
    greeting = models.CharField(max_length=100, default="Hello, I'm Aiza Dawood")
    main_title = models.CharField(max_length=200, default="CRAFTING DIGITAL EXPERIENCES")
    sub_text = models.TextField()

    def __str__(self):
        return self.greeting
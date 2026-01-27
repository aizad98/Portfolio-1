from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # Stack can be a CharField where you list techs (e.g., "Django, SQLite, Bootstrap")
    stack = models.CharField(max_length=200)
    image = models.ImageField(upload_to='project_images/')
    link = models.URLField(blank=True, null=True) # Optional: Link to GitHub or Live site

    def __str__(self):
        return self.title
from django.db import models

# Create your models here.
class Bugs(models.Model):
    project_title= models.TextField(max_length=20, blank=True, default=None)
    bug_title = models.TextField(max_length=20, blank=True, default=None)
    bug_description = models.TextField(max_length=200, blank=True, default=None)
    bug_pic = models.ImageField(default='default.png', blank=True)



    def __str__(self):
        return self.bug_title

from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(blank=True)
    description = models.TextField(default='hello')
    image = models.ImageField(blank=True, upload_to='questions/images')

    # date = models.DateField(default=date.today)

    def __str__(self):
        return self.title

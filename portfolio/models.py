from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    framework = models.ForeignKey(to='Framework', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Framework(models.Model):
    framework = models.CharField(max_length=30, verbose_name='Name', default='name')

    def __str__(self):
        return self.framework

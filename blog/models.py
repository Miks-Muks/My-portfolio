from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

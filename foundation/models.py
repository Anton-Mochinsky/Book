from django.db import models

class Case(models.Model):
    title = models.CharField(max_length=255)
    teg = models.TextField(blank=True)
    images = models.ImageField(upload_to='photos/%Y/%m/%d')
    content = models.TextField(blank=True)
    grade_num = models.IntegerField()
    language = models.CharField(max_length=255)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
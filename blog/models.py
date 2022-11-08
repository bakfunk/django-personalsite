from django.db import models

# Create your models here.
from django.db import models


class Article(models.Model):
    def __str__(self):
        return self.text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    title = models.CharField(max_length=200)
    text = models.TextField()
    pub_date = models.DateTimeField('date published')



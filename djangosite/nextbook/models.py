from django.db import models

# Create your models here.

class RandomManager(models.Manager):

    def get_query_set(self):
        return super(RandomManager, self).get_query_set().order_by('?')



class Book(models.Model):
    book_number = models.IntegerField(default=1, unique=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)

    objects = models.Manager()
    randoms = RandomManager()

    def __str__(self):
        return self.title

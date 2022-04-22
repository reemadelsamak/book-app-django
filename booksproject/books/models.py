from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=250)


class Book(models.Model):

    ISBN = models.IntegerField(unique=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    publish_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    price = models.FloatField()
    appropriate = models.CharField(max_length=250, choices=[(
        'un', 'Under 18'), ('bt', 'Between 8-15'), ('ad', 'Adults')], default='bt')
    poster = models.ImageField(upload_to="books/static/books")

    def __str__(self):
        return self.title

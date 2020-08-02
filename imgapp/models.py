from django.db import models

# Create your models here.

class sortByCategories(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


# create Image model
class Image(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='pics')
    category = models.ForeignKey(sortByCategories, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
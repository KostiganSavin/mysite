from django.db import models

# Create your models here.


class CustomerCommentModel(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    text = models.TextField()
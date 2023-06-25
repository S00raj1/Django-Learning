from django.db import models

# Create your models here.

class ContactUs(models.Model):
    name = models.CharField(max_length=50,null=False)
    email = models.CharField(max_length=100,null=False)
    message = models.TextField(null= False)

    def __str__(self):
        return self.name
from django.db import models
from datetime import date

# Create your models here.


class Add_location(models.Model):
    location_choices = [
        ('Kathmandu','Kathmandu'),
        ('Bhaktapur','Bhaktapur'),
        ('Lalitpur','Lalitpur'),
        ('Outside','Outside Valley')
    ]
    name = models.CharField(max_length = 100,null = False)
    location = models.CharField(max_length=100,choices = location_choices)
    description = models.TextField(max_length = 1000,null = False)
    image = models.ImageField(upload_to = 'location/')
    price = models.TextField(null=False)

    def __str__(self):
        return self.name

class Guide(models.Model):
    name = models.CharField(max_length=50,null= False)
    number = models.CharField(max_length=15,null=False)
    address = models.CharField(max_length=20,null=False)
    experience = models.IntegerField(null=False)
    language = models.CharField(max_length=250,null=False)
    
    def __str__(self):
        return self.name


class Book_location(models.Model):
    name = models.ForeignKey(Add_location,null =True ,on_delete=models.CASCADE)
    guide = models.ManyToManyField(Guide , related_name='guide')
   
    Name = models.CharField(max_length=100)
    People = models.IntegerField(null=False)
    StartingDate = models.DateField(default= date.today,null= False)
    EndingDate = models.DateField(default= date.today,null=False)
   
    
    def __str__(self):
        return self.Name


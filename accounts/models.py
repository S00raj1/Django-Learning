from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='profile_images')
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)


    def save(self,*args,**kwargs):
        super().save()
        img = Image.open(self.avatar.path)

        if img.height > 100 or img.width > 100:
            new_img = (100,100)
            img.thumbnail(new_img)
            img.save(self.avatar.path)



    def __str__(self):
        return self.user.username


from django.db import models
<<<<<<< HEAD

# Create your models here.
=======
<<<<<<< HEAD
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
=======
from django.contrib.auth.models import AbstractUser
from datetime import date
from dateutil.relativedelta import relativedelta

class CustomUser(AbstractUser):
    # These are the fields we want on top of the fields included
    #  with the built-in Django User Model that come with:
    #  username, first_name, last_name, email, password, ....
    gender = models.CharField(max_length=255, blank=True, null=True)
    dob = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.username

    def age(self):
        if self.dob == None:
            return None
        age = relativedelta(date.today(), self.dob)
        return age.years
>>>>>>> dd8e683bf902422332c15d70d55d3d53b3553e2d
>>>>>>> c915ff6c59d82525151f3696c383766d57fd83e2

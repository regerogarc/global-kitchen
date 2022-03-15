# Authored by: Michael Twaddle(2541816t), 

from django.db import models
from django.contrib.auth.models import User

def user_image_dir(instance, filename):
    return "user_images/user_{0}/{1}".format(instance.user.id,filename)
def user_image_dir(instance, filename):
    return "recipe_images/recipe_{0}/{1}".format(instance.id,filename)


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favourites = models.ManyToManyField('Recipe', blank = True)
    picture = models.ImageField(upload_to= 'user_image_dir', blank=True)

    def __str__(self):
        return self.user.username



class Recipe(models.Model):

    author = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    recipe_text = models.CharField(max_length=4096)
    country = models.CharField(max_length = 60)
    likes = models.IntegerField(default = 0)
    picture = models.ImageField(upload_to= 'user_image_dir', blank=True)
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name


from django.db import models
from django.contrib.auth.models import User
<<<<<<< HEAD
from django.template.defaultfilters import slugify


class MyAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=20)
    country = models.CharField(max_length=60, null=True)
    likes = models.ManyToManyField('Recipe', blank=True)
    picture = models.ImageField(upload_to='user_image_dir', blank=True)

    class Meta:
        verbose_name_plural = 'MyAccount'

    def __str__(self):
        return str(self.user)
=======

def user_image_dir(instance, filename):
    return "user_images/user_{0}/{1}".format(instance.user.id,filename)
def user_image_dir(instance, filename):
    return "recipe_images/recipe_{0}/{1}".format(instance.id,filename)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=60, null=True)
    favourites = models.ManyToManyField('Recipe', blank = True)
    picture = models.ImageField(upload_to= 'user_image_dir', blank=True)
    """
    liked = models.ManytoMany(Recipe)
    """

    def __str__(self):
        return self.user.username
>>>>>>> finlay


class Recipe(models.Model):

<<<<<<< HEAD
    author = models.ForeignKey(MyAccount, on_delete = models.CASCADE)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    description = models.CharField(max_length=4096)
    country = models.CharField(max_length = 60)
    picture = models.ImageField(upload_to= 'user_image_dir', blank=True)
    name = models.CharField(max_length = 100)
    ingredients = models.CharField(max_length=1000)
    steps = models.CharField(max_length=3000)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Recipe, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Recipes'
=======
    author = models.ForeignKey(UserProfile, on_delete = models.CASCADE)
    likes = models.IntegerField(default = 0)
    views = models.IntegerField(default = 0)
    recipe_text = models.CharField(max_length = 4096)
    country = models.CharField(max_length = 60)
    picture = models.ImageField(upload_to = 'user_image_dir', blank = True)
    name = models.CharField(max_length = 100)
>>>>>>> finlay

    def __str__(self):
        return self.name

<<<<<<< HEAD


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    picture = models.ImageField(upload_to='user_image_dir', blank=True)

    def __str__(self):
        return self.user.username
=======
    """
    ingredients = models.CharField(max_length = 1000)
    text = models.CharField(max_length = 3000)

    """
>>>>>>> finlay

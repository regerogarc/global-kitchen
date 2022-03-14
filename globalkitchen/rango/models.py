from django.db import models
from django.contrib.auth.models import User
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


class Recipe(models.Model):

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

    def __str__(self):
        return self.name



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    picture = models.ImageField(upload_to='user_image_dir', blank=True)

    def __str__(self):
        return self.user.username

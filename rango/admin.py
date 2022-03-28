from django.contrib import admin
from .models import UserProfile, Recipe

admin.site.register(UserProfile)

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('Text', 'Country', 'author', 'views', 'likes')

admin.site.register(Recipe)


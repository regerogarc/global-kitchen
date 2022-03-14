import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'globalkitchen.settings')
import django

django.setup()
from rango.models import UserProfile, Recipe
from django.contrib.auth.models import User
import random
import string
import os


def get_random_string(length, stringset=string.ascii_letters):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


def populate():
    usernames = ["User" + str(i) + chr(3*i) for i in range(5)]
    print(usernames)
    user_list = []

    for i in range(5):
        user = User.objects.create(username=usernames[i])
        user_list.append(user)
        user.save()

    pizza_text = [{'Ingredients': 'eggs, flour, water, tomaotes, sugar, cheese',
                   'Instructions': 'Use ingredients to make pizza',
                   'description': 'a pizza'}]
    soup_text = [{'Ingredients': 'vegetables, water',
                  'Instructions': 'cook vegetables in water',
                  'description': 'a soup'}]
    sushi_text = [{'Ingredients': 'fish',
                   'Instructions': 'train for 20 years',
                   'description': 'a sushi'}]
    haggis_text = [{'Ingredients': 'sheeps intestines',
                    'Instructions': 'Dont',
                    'description': 'a haggis'}]
    borscht_text = [{'Ingredients': 'beetroot, meat, vegetables',
                     'Instructions': 'combine and cook',
                     'description': 'a borscht'}]
    hotpot_text = [{'Ingredients': 'Meat, vegetables',
                    'Instructions': 'throw in pot and add hot',
                    'description': 'a hot pot'}]

    recipes = {
        "Recipe1": {"name": "Pizza", "Text": pizza_text, "Country": "Italy", "author": user_list[0], "likes": 100,
                    "views": 150},
        "Recipe2": {"name": "Soup", "Text": soup_text, "Country": "France", "author": user_list[1], "likes": 10,
                    "views": 20},
        "Recipe3": {"name": "Sushi", "Text": sushi_text, "Country": "Japan", "author": user_list[2], "likes": 44,
                    "views": 50},
        "Recipe4": {"name": "Haggis", "Text": haggis_text, "Country": "Scotland", "author": user_list[3], "likes": 1000,
                    "views": 1000},
        "Recipe5": {"name": "Borscht", "Text": borscht_text, "Country": "Ukrain", "author": user_list[4], "likes": 1000,
                    "views": 1000},
        "Recipe6": {"name": "HotPot", "Text": hotpot_text, "Country": "China", "author": user_list[5], "likes": 1000,
                    "views": 1000},
    }

    # for k, v in recipes.items():
    #     #UserProfile = UserProfile.objects.get_or_create(user = v["author"])[0]
    #     #UserProfile.save()
    #
    #     recipe = Recipe.objects.get_or_create(author = UserProfile)[0]
    #     recipe.name = k
    #     recipe.recipe_text = v["Text"]
    #     recipe.country = v["Country"]
    #     recipe.likes = v["likes"]
    #     recipe.views = v["views"]
    #     recipe.save()

    for recipes, recipe_data, in recipes.items():
        add_recipe(recipes, recipe_data['Text'], recipe_data['Country'], recipe_data['author'],
                       recipe_data['views'], recipe_data['likes'])



def add_recipe(name, text, country, author, views, likes):
    r = Recipe.objects.get_or_create(name=name, text=text, country=country, author=author)[0]
    r.views = views
    r.likes = likes
    r.save()
    return r


# def add_author(username):
#     a = UserProfile.object.get_or_create(username=username)[0]
#     a.save
#     return a


if __name__ == "__main__":
    populate()

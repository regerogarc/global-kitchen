

### You may need to change the project settings I made this within the tango_with_django project but if you made a new one for global kitchen then you'll need to alter this.

project_settings = 'tango_with_django_project.settings'


import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', project_settings )
import django 
django.setup()
from global_kitchen.models import UserProfile, Recipe
from django.contrib.auth.models import User
import random
import string
import os



def get_random_string(length, stringset=string.ascii_letters):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k = length))   

def populate():
    usernames = ["User" + str(i) + chr(3*i) for i in range(6)]
    print(usernames)
    user_list = []


    for i in range(6):
        user = User.objects.create(username = usernames[i],first_name=get_random_string(10),last_name=get_random_string(10))
        user_list.append(user)
        user.save()

    recipes = { "Pizza": {"Text": "{'Ingredients': 'eggs, flour, water, tomaotes, sugar, cheese', 'Instructions' : 'Use ingredients to make pizza'}", "Country":"Italy", "author": user_list[0],"likes": 100},
               "Soup": {"Text": "{'Ingredients': 'vegetables, water', 'Instructions' : 'cook vegetables in water'}", "Country":"France", "author": user_list[1],"likes": 10},
               "Sushi": {"Text": "{'Ingredients': 'fish', 'Instructions' : 'train for 20 years'}", "Country":"Japan", "author": user_list[2],"likes": 44},
               "Haggis": {"Text": "{'Ingredients': 'sheeps intestines', 'Instructions' : 'Don't'}", "Country":"Scotland", "author": user_list[3],"likes": 1000},
               "Borscht": {"Text": "{'Ingredients': 'beetroot, meat, vegetables', 'Instructions' : 'combine and cook'}", "Country":"Ukrain", "author": user_list[4],"likes": 1000},
               "Hot pot": {"Text": "{'Ingredients': 'Meat, vegetables', 'Instructions' : 'throw in pot and add hot'}", "Country":"China", "author": user_list[5],"likes": 1000},
        }

    for k,v in recipes.items():
        userprofile = UserProfile.objects.get_or_create(user = v["author"])[0]
        userprofile.save()

        recipe = Recipe.objects.get_or_create(author = userprofile)[0]
        recipe.name = k
        recipe.recipe_text = v["Text"]
        recipe.country = v["Country"]
        recipe.likes = v["likes"]
        recipe.save()

if __name__ == "__main__":
    populate()






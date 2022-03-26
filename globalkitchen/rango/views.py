from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from .models import UserProfile, Recipe, User
from .forms import RecipeForm, UserForm, UserProfileForm
import json


def show_recipe(request, recipeID):
    context_dict = {}

    try:
        recipe = Recipe.objects.get(id=recipeID)

        # pages = Recipe.objects.filter(category=category)

        context_dict['recipe'] = recipe
        print(recipe.recipe_text)
        context_dict['recipe_text'] = json.loads(recipe.recipe_text)
        print(context_dict['recipe_text'])
        # context_dict['category'] = category
    except Recipe.DoesNotExist:
        # context_dict['category'] = None
        context_dict['recipe'] = None
        context_dict['recipe_text'] = None
    print(context_dict)
    return render(request, 'rango/recipe.html', context_dict)


def cookbook(request):
    recipe_list = Recipe.objects.order_by('-likes')[:6]
    context_dict = {}
    context_dict["recipes"] = recipe_list
    return render(request, 'rango/CookBook.html',context=context_dict)

def profiles(request):
    return None

@login_required
def userpage(request, username_slug):

    # Get logged in user
    current_user = request.user
    context_dict = {}

    try:
        user_page = User.objects.get(username=username_slug)
    except User.DoesNotExist:
        # The user does not exist.
        # Do nothing for now - 
        pass
    
    # Check if the user is trying to view their own account page
    if current_user.username == user_page.username:
        return render(request, 'rango/Userpage.html')
    else:
        return render(request, 'rango/Userpage.html', context_dict)

def index(request):

    recipe_list_1 = Recipe.objects.order_by('-likes')[:6]
    recipe_list_2 = Recipe.objects.order_by('-views')[:6]

    context_dict = {}

    context_dict['recipe_likes'] = recipe_list_1
    context_dict['recipe_views'] = recipe_list_2
    response = render(request, 'rango/homepage.html', context_dict)
    return response

@login_required

def upload_recipe(request, username_slug):

    try:
        user_profile = UserProfile.objects.get(user = request.user)
    except UserProfile.DoesNotExist:
        print("Failed")

    for filename, file in request.FILES.items():
        print(request.FILES[filename].name)

    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.author = user_profile
            rec = form.save(commit=False)
            rec.author = user_profile
            rec.save() # Save first sp recipe get an ID.
            if  'picture' in request.FILES:
                rec.picture = request.FILES['picture']
            rec.save()
            return redirect(reverse('rango:upload_recipe',kwargs={"username_slug":username_slug}))
        else:
            print(form.errors)

        if not request.user.is_authenticated:
            return reverse('rango:Login')

    if request.user.is_authenticated:
        reverse('rango:upload_recipe',kwargs={"username_slug":username_slug})

    return render(request, 'rango/Uploadrecipe.html', {'form': form})


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
            print(registered)
            return redirect(reverse('rango:login'))
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
    return render(request, 'rango/Signup.html',
                  context={'user_form': user_form,
                           'profile_form': profile_form,
                           'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('rango:homepage'))
            else:
                return HttpResponse("Your global kitchen account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'rango/Login.html')


def some_view(request):
    if not request.user.is_authenticated():
        return HttpResponse("You are logged in.")
    else:
        return HttpResponse("You are not logged in.")

@login_required
def restricted(request):
    return render(request, 'rango/restricted.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('rango:homepage'))

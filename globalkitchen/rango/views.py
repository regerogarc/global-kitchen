from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from .models import UserProfile, Recipe, MyAccount
from .forms import RecipeForm, UserForm, UserProfileForm



def show_recipe(request, recipe_name_slug):
    context_dict = {}

    try:
        recipe = Recipe.objects.get(slug=recipe_name_slug)

        # pages = Recipe.objects.filter(category=category)

        context_dict['recipe'] = recipe
        # context_dict['category'] = category
    except Recipe.DoesNotExist:
        # context_dict['category'] = None
        context_dict['recipe'] = None
    return render(request, 'rango/recipe.html', context_dict)

@login_required
def myaccount(request, user, email, country):
    context_dict = {}
    try:
        username = MyAccount.objects.get(user=user)
        email=MyAccount.obkects.get(email=email)
        country=MyAccount.objects.get(country=country)
        context_dict['username'] = username
        context_dict['email'] = email
        context_dict['country'] = country
    except MyAccount.DoesNotExist:
        context_dict['username'] = None
        context_dict['email'] =  None
        context_dict['country'] =  None


    return render(request, 'rango/CookBook.html', context_dict)

def index(request):

    recipe_list_1 = Recipe.objects.order_by('-likes')[:6]
    recipe_list_2 = Recipe.objects.order_by('-views')[:6]

    context_dict = {}

    context_dict['recipe_likes'] = recipe_list_1
    context_dict['recipe_views'] =recipe_list_2
    response = render(request, 'rango/homepage.html')
    return response

@login_required
def upload_recipe(request, recipe_name_slug):
    form = RecipeForm()
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            rec = form.save(commit=True)
            print(rec, rec.slug)
            return redirect(reverse('rango:Uploadrecipe',kwargs={'recipe_name_slug': recipe_name_slug}))
        else:
            print(form.errors)

        if not request.user.is_authenticated:
            return reverse('rango:Login')

    if request.user.is_authenticated:
        reverse('rango:Uploadrecipe')

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
from django.urls import path
from rango import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='homepage'),
<<<<<<< HEAD
    path('recipe/<slug:recipe_name_slug>/', views.show_recipe, name='show_recipe'),
    path('upload_recipe/', views.upload_recipe, name='upload_recipe'),
    path('Myaccount/', views.myaccount, name='Userpage'),

=======
    path('recipe/<int:recipeID>/', views.show_recipe, name='show_recipe'),
    path('profiles', views.profiles, name='profiles'),
    path('profiles/<slug:username_slug>/', views.userpage, name='userpage'),
    path('profiles/<slug:username_slug>/UploadRecipe/', views.upload_recipe, name='upload_recipe'),
    path('CookBook/', views.cookbook, name='cookbook'),
>>>>>>> finlay
    path('Signup/', views.register, name='signup'),
    path('login/', views.user_login, name='login'),
    path('restricted/', views.restricted, name='restricted'),
    path('logout/', views.user_logout, name='logout'),


]

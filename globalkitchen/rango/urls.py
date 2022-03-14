from django.urls import path
from rango import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'rango'

urlpatterns = [
    path('', views.index, name='homepage'),
    path('recipe/<slug:recipe_name_slug>/', views.show_recipe, name='show_recipe'),
    path('upload_recipe/', views.upload_recipe, name='upload_recipe'),
    path('Myaccount/', views.myaccount, name='Userpage'),

    path('Signup/', views.register, name='signup'),
    path('login/', views.user_login, name='login'),
    path('restricted/', views.restricted, name='restricted'),
    path('logout/', views.user_logout, name='logout'),


]

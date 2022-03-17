from django import forms
from django.contrib.auth.models import User

from .models import Recipe,UserProfile




class RecipeForm(forms.ModelForm):
    name = forms.CharField(max_length=128,help_text="Please enter the recipe name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    author = forms.CharField(max_length=60)
    country = forms.CharField(max_length=60)
    picture = forms.ImageField()#upload_to='user_image_dir', blank=True)
    ingredients = forms.CharField(max_length=1000)
    description = forms.CharField(max_length=4096)
    instructions = forms.CharField(max_length=3000)

    class Meta:
        model = Recipe
        fields = ('name',)



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)
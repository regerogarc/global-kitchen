# Authored by: Michael Twaddle(2541816t),

from django import forms
from rango.models import UserProfile, Recipe
from django.contrib.auth.models import User
from rango.Countries import COUNTRY_CHOICES
import json

class RecipeTextWidget(forms.MultiWidget):
    def __init__(self, *args, **kwargs):
        self.widgets = [
            forms.TextInput(),
            forms.TextInput(),
            forms.TextInput(),
            ]
        super(RecipeTextWidget, self).__init__(*args,widgets = self.widgets,**kwargs)

    def decompress(self, value):
        if value:
            return value.split(' ')
        return [None, None]

class RecipeTextField(forms.MultiValueField):

    widget = RecipeTextWidget

    def __init__(self, **kwargs):

        fields = (
            forms.CharField(max_length = 1000, help_text = "Enter ingredients"),
            forms. CharField(max_length = 2048, help_text = "Enter instructions"),
            forms. CharField(max_length = 300, help_text = "Enter description")
            )
        super().__init__(fields=fields, **kwargs)

    def compress(self, data_lst):
        dic = {
            "ingredients": data_lst[0],
            "Text": data_lst[1],
            "description": data_lst[2]
            }

        return json.dumps(dic)



class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile 
        fields = ('picture',)
     

class RecipeForm(forms.ModelForm):
    name = forms.CharField(max_length = 100, help_text="Enter the name of the recipe.", required = True)
    recipe_text = RecipeTextField()
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    views = forms.IntegerField(widget = forms.HiddenInput(),initial = 0)
    country = forms.ChoiceField(choices = COUNTRY_CHOICES, label = "Country", widget = forms.Select(),required = True )

    class Meta:
        model = Recipe
        exclude = ("author",)






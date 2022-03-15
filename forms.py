from django import forms
from global_kitchen.models import UserProfile, Recipe
import json

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password')

class RecipeForm(forms.ModelForm):
    name = forms.CharField(max_length = 100, help_text="Enter the name of the recipe.")
    recipe_text = RecipeTextField()
    #country = 

    class Meta:
        model = Recipe
        exclude = ("country", )





class RecipeTextField(forms.MultiValueField):

    widget = RecipeTextWidget


    def __init__(self, **kwargs):

        fields = (
            forms.CharField(max_length = 1000, help_text = "Enter ingredients"),
            forms. CharField(max_length = 3048, help_text = "Enter instructions")
            )
        super().__init__(fields=fields, **kwargs)

    def compress(self, data_lst):
        dic = {
            "ingredients": data_lst[0],
            "Text": data_lst[1]
            }

        return json.dumps(dic)


class RecipeTextWidget(forms.MultiWidget):
    def __init__(self, *args, **kwargs):
        super(RecipeTextWidget, self).__init__(*args,**kwargs)
        self.widgets = [
            forms.TextInput(),
            forms.TextInput(),
            ]

        def decompress(self, value):
            if value:
                return value.split(' ')
            return [None, None]


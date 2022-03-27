import os
import re
from rango.models import Recipe
from django.test import TestCase
from django.urls import reverse
from populate_gk import populate
from django.test import Client
from django.db.models.query import QuerySet
from django.test.utils import setup_test_environment
from django.conf import settings

setup_test_environment()
client = Client()

class TestPopulationScript(TestCase):

    def setUp(self):
        populate()

    def test_recipe_objects_have_views_and_likes(self):

        recipes = Recipe.objects.filter()

        for recipe in recipes:
            self.assertTrue(recipe.views > 0,"populate script views test fail")
            self.assertTrue(recipe.likes > 0, "populate script likes test fail" )

class ShowRecipeViewTests(TestCase):
    def setUp(self):
        populate()
        self.response = self.client.get(reverse('rango:recipe'))
        self.content = self.response.content.decode()

        expected_recipe_list = list(Recipe.objects)
        self.assertTrue('expected_recipe_list' in self.response.context,"no recipe_list in the context dictionary within the show_recipe view")




class CookBookViewTests(TestCase):
    def setUp(self):
        populate()
        self.response = self.client.get(reverse('rango:index'))
        self.content = self.response.content.decode()

        expected_recipe_likes_order = list(Recipe.objects.order_by('-likes')[:6])
        self.assertTrue('expected_recipe_likes_order' in self.response.context,"no recipe_likes varible in the context dictionary within the cookbook view")




class IndexViewTests(TestCase):

    def setUp(self):
        populate()
        self.response = self.client.get(reverse('rango:homepage'))
        self.content = self.response.content.decode()

    def test_homepage_context_dictionary(self):

        expected_recipe_likes_order = list(Recipe.objects.order_by('-likes')[:6])
        expected_recipe_views_order = list(Recipe.objects.order_by('-views')[:6])

        self.assertTrue('expected_recipe_likes_order ' in self.response.context,"no recipe_likes varible in the context dictionary within the Index view")
        self.assertTrue('expected_recipe_views_order' in self.response.context,"no recipe_views varible in the context dictionary within the Index view")
        self.assertEqual(type(self.response.context['recipe_likes']), QuerySet,"test failed, index view doesnt return data type query set")
        self.assertEqual(type(self.response.context['recipe_views']), QuerySet,"test failed, index view doesnt return data type query set")
        self.assertEqual(expected_recipe_likes_order, list(self.response.context['recipe_likes']),"test failed")
        self.assertEqual(expected_recipe_views_order, list(self.response.context['recipe_views']),"test failed")



class UploadRecipeViewTests(TestCase):

    def setUp(self):
        populate()
        self.response = self.client.get(reverse('rango:upload_recipe'))
        self.content = self.response.content.decode()


class RegisterViewTests(TestCase):

    def setUp(self):
        populate()
        self.response = self.client.get(reverse('rango:register'))
        self.content = self.response.content.decode()


class TemplateTests(TestCase):

    def get_template(self, path_to_template):

        f = open(path_to_template, 'r')
        template_str = ""
        for line in f:
            template_str = f"{template_str}{line}"
        f.close()
        return template_str


    def test_base_template_exists(self):

        template_base_path = os.path.join(settings.TEMPLATE_DIR, 'rango', 'base.html')
        self.assertTrue(os.path.exists(template_base_path),"No base template exists")


    def test_base_title_block(self):

        template_base_path = os.path.join(settings.TEMPLATE_DIR, 'rango', 'base.html')
        template_str = self.get_template(template_base_path)

        title_pattern = r'<title>(\s*|\n*){% block title_block %}(\s*|\n*)Global kitchen(\s*|\n*){% (endblock|endblock title_block) %}(\s*|\n*)</title>'
        self.assertTrue(re.search(title_pattern, template_str),"No title block exists")


    def test_template_usage(self):

        populate()

        urls = [reverse('rango:homepage'),
                reverse('rango:show_recipe'),
                reverse('rango:profiles'),
                reverse('rango:upload_recipe'),
                reverse('rango:Userpage'),
                reverse('rango:signup'),
                reverse('rango:login'),
                reverse('rango:restriced'),
                reverse('rango:logout'),]

        templates = ['rango/Homepgae.html',
                     'rango/show_recipe.html',
                     'rango/upload_recipe.html',
                     'rango/Userpage.html',
                     'rango/Signup.html',
                     'rango/LogIn.html',
                     'rango/restricted.html',
                     'rango/Homepage.html',]

        for url, template in zip(urls, templates):
            response = self.client.get(url)
            self.assertTemplateUsed(response, template)

    def test_for_links_in_base(self):

        template_str = self.get_template(os.path.join(settings.TEMPLATE_DIR, 'rango', 'base.html'))

    def test_title_blocks(self):
        """
        Tests whether the title blocks in each page are the expected values.
        This is probably the easiest way to check for blocks.
        """
        populate()
        template_base_path = os.path.join(settings.TEMPLATE_DIR, 'rango')

        mappings = {
            reverse('rango:homepage'): {'full_title_pattern': r'<title>(\s*|\n*)Global Kitchen(\s*|\n*)-(\s*|\n*)Homepage(\s*|\n*)</title>',
                                        'block_title_pattern': r'{% block title_block %}(\s*|\n*)Homepgae(\s*|\n*){% (endblock|endblock title_block) %}',
                                        'template_filename': 'Hompepage.html'},
            reverse('rango:CookBook'): {'full_title_pattern': r'<title>(\s*|\n*)Global Kitchen(\s*|\n*)-(\s*|\n*)cookbook(\s*|\n*)</title>',
                                        'block_title_pattern': r'{% block title_block %}(\s*|\n*)cookbook(\s*|\n*){% (endblock|endblock title_block) %}',
                                        'template_filename': 'CookBook.html'},
            reverse('rango:login'): {'full_title_pattern': r'<title>(\s*|\n*)Global Kitchen(\s*|\n*)-(\s*|\n*)LogIn(\s*|\n*)</title>',
                                     'block_title_pattern': r'{% block title_block %}(\s*|\n*)LogIn(\s*|\n*){% (endblock|endblock title_block) %}',
                                     'template_filename': 'LogIn.html'},
            reverse('rango:show_recipe'): {'full_title_pattern': r'<title>(\s*|\n*)Global Kitchen(\s*|\n*)-(\s*|\n*)recipe(\s*|\n*)</title>',
                                           'block_title_pattern': r'{% block title_block %}(\s*|\n*)recipe(\s*|\n*){% (endblock|endblock title_block) %}',
                                           'template_filename': 'recipe.html'},
            reverse('rango:signup'): {'full_title_pattern': r'<title>(\s*|\n*)Global Kitchen(\s*|\n*)-(\s*|\n*)SignUp(\s*|\n*)</title>',
                                      'block_title_pattern': r'{% block title_block %}(\s*|\n*)SignUp(\s*|\n*){% (endblock|endblock title_block) %}',
                                      'template_filename': 'Signup.html'},
            reverse('rango:login'): {'full_title_pattern': r'<title>(\s*|\n*)Global Kitchen(\s*|\n*)-(\s*|\n*)LogIn(\s*|\n*)</title>',
                                     'block_title_pattern': r'{% block title_block %}(\s*|\n*)LogIn(\s*|\n*){% (endblock|endblock title_block) %}',
                                     'template_filename': 'LogIn.html'},
            reverse('rango:userpage'): {'full_title_pattern': r'<title>(\s*|\n*)Global Kitchen(\s*|\n*)-(\s*|\n*)UserPage(\s*|\n*)</title>',
                                        'block_title_pattern': r'{% block title_block %}(\s*|\n*)UserPage(\s*|\n*){% (endblock|endblock title_block) %}',
                                        'template_filename': 'Userpage.html'},
            reverse('rango:userpage'): {'full_title_pattern': r'<title>(\s*|\n*)Global Kitchen(\s*|\n*)-(\s*|\n*)UserPage(\s*|\n*)</title>',
                                        'block_title_pattern': r'{% block title_block %}(\s*|\n*)UserPage(\s*|\n*){% (endblock|endblock title_block) %}',
                                        'template_filename': 'Userpage.html'}}

from django import forms
from blogs.models import Category, Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# creates the form for adding a new category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'category', 'featured_image',
                  'short_description', 'blog_body', 'status', 'is_featured')

# UserCreationForm is also used in the User Registration: Blog_main\forms.py
# User model is a default or automatic table in Django


class AddUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_active',
                  'is_staff', 'is_superuser', 'groups', 'user_permissions')


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        # limits the form into these fields minus the password1  & password2
        fields = ('username', 'email', 'first_name', 'last_name', 'is_active',
                  'is_staff', 'is_superuser', 'groups', 'user_permissions')

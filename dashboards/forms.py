from django import forms
from blogs.models import Category

# creates the form for adding a new category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

from django.contrib import admin
from .models import Category, Blog

# prepopulates the blog slug based on the title


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'author', 'status', 'is_featured')
    # search by the following fields. Category is a FK, so to call the category_name from the other
    # table we use the format wth the double underscore: fkffield__fieldname
    search_fields = ('id', 'title', 'category__category_name', 'status')
    # make the list editable using the is_featured field
    list_editable=('is_featured',)

# Register your models here.
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)

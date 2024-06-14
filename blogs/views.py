from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import HttpResponse
from .models import Blog, Category
# allows for complex query/filter using OR
from django.db.models import Q

# Create your views here.


def posts_by_category(request, category_id):
    # Fetch the posts under the category using the category_id or you can use category as
    # Django appends ID to this FK
    posts = Blog.objects.filter(status='Published', category_id=category_id)

    # METHODS to handle record not found: you can use get_object_or_404 OR you can use TRY .. EXCEPT
    # use 404 error page if you want this instead to show when the category does not exist.
    category = get_object_or_404(Category, pk=category_id)

    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts_by_category.html', context)


def blogs(request, blog_slug):
    single_post = get_object_or_404(Blog, slug=blog_slug, status='Published')

    context = {
        'single_post': single_post,

    }
    return render(request, 'blogs.html', context)


def search(request):
    # gets the form's GET value
    keyword = request.GET.get('keyword')
    # print("keyword:", keyword)
    # find all blog titles with the keyword
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(
        short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published')
    context = {
        'blogs': blogs,
        'keyword': keyword,
    }
    return render(request, 'search.html', context)

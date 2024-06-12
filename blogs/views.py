from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import HttpResponse
from .models import Blog, Category

# Create your views here.


def posts_by_category(request, category_id):
    # Fetch the posts under the category using the category_id or you can use category as
    # Django appends ID to this FK
    posts = Blog.objects.filter(status='Published', category_id=category_id)

    # METHODS to handle record not found: you can use get_object_or_404 OR you can use TRY .. EXCEPT
    
    # use 404 error page if you want this instead to show when the category does not exist.
    category = get_object_or_404(Category, pk=category_id)
    
    # use try/except when we want to do some custome action if the category does not exist
    # try:
    #     category = Category.objects.get(pk=category_id)
    # except:
    #     # redirect the user to homepage
    #     return redirect('home')

    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts_by_category.html', context)

from django.shortcuts import render, redirect, get_object_or_404
from blogs.models import Category, Blog
from django.contrib.auth.decorators import login_required

from .forms import CategoryForm, BlogPostForm
from django.template.defaultfilters import slugify

# adding a decorator as a restriction and forcing the user to go to login page


@login_required(login_url='login')
def dashboard(request):
    # counts all the categories and posts
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count
    # print(category_count,blogs_count)
    context = {
        'category_count': category_count,
        'blogs_count': blogs_count,
    }

    return render(request, 'dashboard/dashboard.html', context)


# CRUD FUNCTIONS for Category
def categories(request):
    return render(request, 'dashboard/categories.html')


def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('categories')
    form = CategoryForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_category.html', context)


def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        # get the new value and replace the current instance
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')

    # gets the category record and pass this as instance to the form
    form = CategoryForm(instance=category)
    context = {
        'form': form,
        'category': category,
    }
    return render(request, 'dashboard/edit_category.html', context)


def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')

# CRUD FUNCTIONS for Posts


def posts(request):
    posts = Blog.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'dashboard/posts.html', context)


def add_post(request):
    if request.method == 'POST':
        # get the user entry of new values for new post and handles the images or other files
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  # temporarily saving the form
            # assigns the logged user as the author
            post.author = request.user
            # saves now the form named as post
            post.save()
            # print('form is valid')
            # gets the title from the form
            title = form.cleaned_data['title']
            # creates an automatic slug based on the title & to make it unique, we append the PK of this post
            # post.id is generated only when we first save the post.
            post.slug = slugify(title)+'-'+str(post.id)  # this-is-a-new-post-1
            # save again to ignore slug duplicates.
            post.save()
            return redirect('posts')
        else:
            print('form is invalid')
            print(form.errors)

    form = BlogPostForm()
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_post.html', context)


def edit_post(request, pk):
    # gets the database record details and show these on the form
    post = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        # get the form with updated values including the images
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid:
            post = form.save()  # gets the form instance
            # in case title was changed
            title = form.cleaned_data['title']
            post.slug = slugify(title)+'-'+str(post.id)
            post.save()
            return redirect('posts')
    form = BlogPostForm(instance=post)
    context = {
        'form': form,
        'post': post,
    }
    return render(request, 'dashboard/edit_post.html', context)


def delete_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    post.delete()
    return redirect('posts')

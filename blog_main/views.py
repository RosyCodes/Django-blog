# from django.http import HttpResponse
from django.shortcuts import render, redirect
from blogs.models import Category, Blog
from blog_profile.models import About, SocialLink
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


def home(request):
    featured_posts = Blog.objects.filter(
        is_featured=True, status='Published').order_by('-updated_at')
    posts = Blog.objects.filter(is_featured=False, status='Published')
    # Fetch about us //  Instead of this, we used a context processor for about us
    # try:
    #     about = About.objects.get()
    # except:
    #     about = None

    context = {
        'featured_posts': featured_posts,
        'posts': posts,
        # 'about': about,
    }
    # return HttpResponse('<h1>HomePage</h1>')
    return render(request, 'home.html', context)


def register(request):
    if request.method == 'POST':
        # pass the form user entry to the form
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # gets the user entry values
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # checks if username/password is found and then login
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('dashboard')

    form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('home')

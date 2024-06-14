# from django.http import HttpResponse
from django.shortcuts import render
from blogs.models import Category, Blog
from blog_profile.models import About, SocialLink


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

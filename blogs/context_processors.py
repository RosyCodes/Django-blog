# this is a context processor file that allows the Category menu items to be
# availabe on every page

from .models import Category
from blog_profile.models import SocialLink, About


def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)


def get_social_links(request):
    social_links = SocialLink.objects.all()
    return dict(social_links=social_links)


def get_about_us(request):
    try:
        about = About.objects.get()
    except:
        about = None
    return dict(about=about)

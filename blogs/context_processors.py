# this is a context processor file that allows the Category menu items to be
# availabe on every page

from .models import Category


def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)

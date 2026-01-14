

from category.models import Category


def menu_links(request):
    category_links = Category.objects.all()
    return dict(links=category_links)

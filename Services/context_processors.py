from .models import *

def menu_links(request):
    links = ServiceCategory.objects.all()
    return dict(links=links)
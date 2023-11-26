from django.shortcuts import render
from django.http import HttpResponse
from products.models import Item

# Create your views here.

def index(request):
    itemlist = Item.objects.all()
    
    context = {
        'itemlist':itemlist
    }
    
    return render(request, 'products/index.html', context)

def detail(request, item_id):
    return HttpResponse('item_id: {}'.format(item_id))
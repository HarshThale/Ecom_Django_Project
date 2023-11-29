from django.shortcuts import render, redirect
from django.http import HttpResponse
from products.models import Item
from products.forms import ItemForm

# Create your views here.

def index(request):
    itemlist = Item.objects.all()
    
    context = {
        'itemlist':itemlist
    }
    
    return render(request, 'products/index.html', context)

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)

    context = {
        'item':item
    }
    
    return render(request, 'products/detail.html', context)

def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('products:index')

    context = {
        'form':form
    }

    return render(request, 'products/item-form.html', context)

def update_item(request, id):
    item = Item.objects.get(pk=id)
    form = ItemForm(request.POST or None, instance=item)

    context = {
        'form':form
    }
    
    if form.is_valid():
        form.save()
        return redirect('products:index')
    
    return render(request, 'products/item-form.html', context)

def delete_item(request, id):
    item = Item.objects.get(pk=id)

    context = {
        'item':item
    }

    if request.method == 'POST':
        item.delete()
        return redirect('products:index')

    return render(request, 'products/item-delete.html', context)
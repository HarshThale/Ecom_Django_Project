from django.shortcuts import render, redirect
from django.http import HttpResponse
from products.models import Item
from products.forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

# Create your views here.
# -------------------------------------------------------------------------------


# function based index view
# -------------------------------------------------------------------------------

def index(request):
    
    itemlist = Item.objects.all()
    
    context = {
        'itemlist':itemlist
    }
    
    return render(request, 'products/index.html', context)


# class based index view
# -------------------------------------------------------------------------------

class IndexClassView(ListView):

    model = Item
    context_object_name = 'itemlist'
    template_name = 'products/index.html'


# function based detail view
# -------------------------------------------------------------------------------

def detail(request, item_id):
    
    item = Item.objects.get(pk=item_id)

    context = {
        'item':item
    }
    
    return render(request, 'products/detail.html', context)


# class based detail view
# -------------------------------------------------------------------------------

class ProductsDetail(DetailView):

    model = Item
    context_object_name = 'item'
    template_name = 'products/detail.html'


# function based create item view
# -------------------------------------------------------------------------------

def create_item(request):
    
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('products:index')

    context = {
        'form':form
    }

    return render(request, 'products/item-form.html', context)


#class based create item view
# -------------------------------------------------------------------------------

class CreateItem(CreateView):

    model = Item
    fields = ['prod_code', 'for_user', 'item_name', 'item_desc', 'item_price', 'item_image']
    template_name = 'products/item-form.html'
    success_url = reverse_lazy('products:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# function based update item view
# -------------------------------------------------------------------------------

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


# function based delete item view
# -------------------------------------------------------------------------------

def delete_item(request, id):
    
    item = Item.objects.get(pk=id)

    context = {
        'item':item
    }

    if request.method == 'POST':
        item.delete()
        return redirect('products:index')

    return render(request, 'products/item-delete.html', context)
from django.shortcuts import render, redirect
from django.http import HttpResponse
from products.models import Item
from products.forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from products.models import History
from users.models import CusOrders, CusRatingFeedback
from django.core.paginator import Paginator

# Create your views here.
# -------------------------------------------------------------------------------


# function based index view
# -------------------------------------------------------------------------------

def index(request):
    
    if request.user.is_superuser:
        itemlist = Item.objects.all()
        
        # for search functionality
        item_name = request.GET.get('item_name')
        if item_name != '' and item_name is not None:
            itemlist = Item.objects.filter(item_name__icontains=item_name)
            
        # For Pagination 
        paginator = Paginator(itemlist, 3)
        page = request.GET.get('page')
        itemlist = paginator.get_page(page)

    elif request.user.is_authenticated and request.user.profile.user_type=='store':
        itemlist = Item.objects.filter(for_user=request.user.username)
        
        # for search functionality
        item_name = request.GET.get('item_name')
        if item_name != '' and item_name is not None:
            itemlist = Item.objects.filter(item_name__icontains=item_name)
            
        # For Pagination 
        paginator = Paginator(itemlist, 3)
        page = request.GET.get('page')
        itemlist = paginator.get_page(page)

    elif request.user.is_authenticated and request.user.profile.user_type=='Cust':
        itemlist = Item.objects.all()
        
        # for search functionality
        item_name = request.GET.get('item_name')
        if item_name != '' and item_name is not None:
            itemlist = Item.objects.filter(item_name__icontains=item_name)
            
        # For Pagination 
        paginator = Paginator(itemlist, 3)
        page = request.GET.get('page')
        itemlist = paginator.get_page(page)

    else:
        itemlist = Item.objects.all()
        
        # for search functionality
        item_name = request.GET.get('item_name')
        if item_name != '' and item_name is not None:
            itemlist = Item.objects.filter(item_name__icontains=item_name)
            
        # For Pagination 
        paginator = Paginator(itemlist, 3)
        page = request.GET.get('page')
        itemlist = paginator.get_page(page)
    
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
    
    hist = History.objects.filter(
        prod_ref = item.prod_code
    )
    # store and admin
    if request.user.profile.user_type == 'store' or request.user.is_superuser:
        Obj_CusOrd = CusOrders.objects.filter(
            prod_code = item.prod_code
        )
        
    # customer
    elif request.user.profile.user_type == 'Cust':
        Obj_CusOrd = CusOrders.objects.filter(
            prod_code = item.prod_code,
            user = request.user.username
        )

    crf = CusRatingFeedback.objects.filter(
        prod_code=item.prod_code
    )

    context = {
        'item':item,
        'hist':hist,
        'oco': Obj_CusOrd,
        'crf':crf
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
        
        Obj_History = History(
            user_name = self.request.user.username,
            prod_ref = form.instance.prod_code,
            item_name = self.request.POST.get('item_name'),      # form.instance.item_name
            op_type = 'Created'
        )

        Obj_History.save()
        
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
        
        Obj_History = History(
            user_name = request.user.username,
            prod_ref = form.instance.prod_code,
            item_name = request.POST.get('item_name'),      # form.instance.item_name
            op_type = 'Updated'
        )

        Obj_History.save()
        
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
        
        Obj_History = History(
            user_name = request.user.username,
            prod_ref = item.prod_code,
            item_name = item.item_name,
            op_type = 'Deleted'
        )

        Obj_History.save()
        
        item.delete()
        return redirect('products:index')

    return render(request, 'products/item-delete.html', context)


def category(request, val):
    items = Item.objects.filter(
        category = val
    )
    
    context = {
        'items':items
    }
    
    return render(request, 'products/category.html', context)